from ui_files import UI_DialogWithoutBudget
from PyQt5.QtWidgets import QWidget, QMessageBox
from Products import Products


class DialogWithoutBudget(UI_DialogWithoutBudget.DialogWithoutBudget_UI, QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.cancel_btn.clicked.connect(self.back)
        self.ok_btn.clicked.connect(self.ok)

        self.food_id = ""
        self.radiobtns.buttonClicked.connect(self.set_food_id)

    def ok(self):
        if self.food_id == "":
            form = QMessageBox.information(
                self, "Ошибка", "Заполните все поля", QMessageBox.Ok
            )
        else:
            #transfer params in a next form
            if self.food_id == "Натуральное питание":
                self.products_window = Products([self.dog_mass_scroll.valueFromText((self.dog_mass_scroll.text())), self.food_id])
                self.products_window.show()
            else:
                form = QMessageBox.information(
                    self, "Ошибка", "Не реализовано", QMessageBox.Ok
            )


    def back(self):
        self.hide()

    def set_food_id(self, btn):
        self.food_id = btn.text()
