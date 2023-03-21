from ui_files import UI_Products
from PyQt5.QtWidgets import QWidget
from FinalWindow import FinalWindow


class Products(QWidget, UI_Products.Products_UI):
    def __init__(self, parametrs: list) -> None:
        super().__init__()
        self.setupUi(self)
        self.parametrs = parametrs

        self.cancel_btn.clicked.connect(self.back)
        self.ok_btn.clicked.connect(self.ok)

    def ok(self):
        products = [["proteins"], ["vegetable"], ["milk"], ["porige"]]
        # sdfsdf
        products[0].append(self.proteins_cb1.currentText())
        products[0].append(self.proteins_cb2.currentText())
        products[1].append(self.vegetables_cb1.currentText())
        products[1].append(self.vegetables_cb2.currentText())
        products[2].append(self.milk_cb1.currentText())
        products[2].append(self.milk_cb2.currentText())
        products[3].append(self.porige_cb.currentText())

        for category in products:
            while "-" in category:
                category.remove("-")

        self.finwindow = FinalWindow(self.parametrs, products)
        self.finwindow.show()

    def back(self):
        self.hide()
