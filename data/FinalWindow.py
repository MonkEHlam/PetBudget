import sys
import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication
from PyQt5.QtCore import Qt
from ui_files import UI_FinalWindow

DELTA_DEVITATIONS = 10 #permissible deviation


class FinalWindow(QWidget, UI_FinalWindow.FinalWindow_UI):
    def __init__(self, parametrs: list, products: list) -> None:
        super().__init__()
        self.dog_mass, self.type_of_food = parametrs
        self.products = products
        self.setupUi(self)

        #change dog mass in a form acceptable for database
        if self.dog_mass > 10:
            for mass in range(15, 51, 5):
                if self.dog_mass <= mass:
                    if self.dog_mass == mass:
                        break
                    elif self.dog_mass > mass - 3:
                        self.dog_mass = mass
                        break
                    else:
                        self.dog_mass = mass - 5
                        break

        if self.type_of_food == "Готовые корма":
            pass
        else:
            self.natural_calculation()

    def natural_calculation(self) -> None:
        result_price = 0
        product_mass_per_day = {}
        proteinsfatscarbon_per_day = [0, 0, 0]
        product_ids = {}
        position_names = {}

        shop_db = sqlite3.connect("Shop.db")
        cur = shop_db.cursor()

        #params_per_day == [kj, proteins, fats, cbhs]
        params_per_day = cur.execute(
            """SELECT * FROM DogFoodValuePerDay
                    WHERE Kg = ?""",
            (self.dog_mass,),
        ).fetchall()[0][1:]
        print(params_per_day)

        # prices = [(id, title, cost, weight), (id, title, cost, weight)]
        prices = cur.execute("""SELECT * FROM PriceList""").fetchall()

        for category in self.products:
            for product in category[1:]:
                for position in prices:
                    if product != None:
                        if product.lower() in position[1].lower():
                            product_ids[product] = position[0]
                            position_names[product] = position[1]

        # products == [[category_name, product_name, product_name]]

        # This cycle add into the dictonary product_mass_per_day mass(in gramms) of every product that user have selected in window before 
        # and calculate how many protein, fats, carbonyhydrates in day food
        for category in self.products:
            kj_fraction = 0
            if category[0] == "proteins":
                kj_fraction = 0.3
            elif category[0] == "vegetable":
                kj_fraction = 0.075
            elif category[0] == "milk":
                kj_fraction = 0.05
            elif category[0] == "porige":
                kj_fraction = 0.075

            for product in category[1:]:
                required_kj = 0
                if len(category[1:]) == 1:
                    required_kj = params_per_day[0] * kj_fraction * 2
                elif len(category[1:]) == 2:
                    required_kj = params_per_day[0] * kj_fraction
                
                #product_values == [kJ, proteins, fats, cbhs]
                product_values = list(cur.execute(
                        """SELECT * FROM PriceList LEFT JOIN FoodValue ON FoodValue.id = PriceList.id WHERE PriceList.id = ?""",
                        (product_ids[product],),
                    ).fetchall()[0])[5:]
                
                product_mass_per_day[product] =  product_mass_per_day.get(product, 0) + required_kj // (int(product_values.pop(0)) / 100)
                print(product_mass_per_day[product])
                for i in range(len(product_values)):
                    proteinsfatscarbon_per_day[i] += product_mass_per_day[product] * (product_values[i] / 100)
        
        #calculating devitations using parametrs from params_per_day
        value_deviations = []
        for i in range(len(proteinsfatscarbon_per_day)):
            if proteinsfatscarbon_per_day[i] - DELTA_DEVITATIONS <= params_per_day[i + 1] <= proteinsfatscarbon_per_day[i] + DELTA_DEVITATIONS:
                value_deviations.append(0)
            else:
                devitation = ''
                if int(params_per_day[i + 1]) - int(proteinsfatscarbon_per_day[i]) < 0:
                    devitation = '+' + str(int(params_per_day[i + 1]) - int(proteinsfatscarbon_per_day[i]) - DELTA_DEVITATIONS)
                else:
                    devitation = '-' + str(int(params_per_day[i + 1]) - int(proteinsfatscarbon_per_day[i]) + DELTA_DEVITATIONS)
                value_deviations.append(devitation)
        
        self.proteins_lcd.display(value_deviations[0])
        self.fats_lcd.display(value_deviations[1])
        self.cbhs_lcd.display(value_deviations[2])

        #creating final text with
        #it is considered that there are 30 days in a month
        text = ""
        for key in product_mass_per_day.keys():
            text += f"\n{position_names[key]}: {product_mass_per_day[key] * 30} грамм({product_mass_per_day[key]} в день)"
            position_values = cur.execute("""SELECT PriceList.cost, PriceList.netweight FROM PriceList where PriceList.title = ?""", (position_names[key],)).fetchall()[0]
            result_price += ((product_mass_per_day[key] * 30  // position_values[1])) * position_values[0]

        text += "\n\nИтоговая цена" + str(result_price)
        self.textBrowser.setText(f"Не забывайте о сроке годности!\n{text}")
        
        cur.close()
