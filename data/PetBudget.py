from DialogWithoutBudget import DialogWithoutBudget
from ShopList import ShopList
from ui_files import UI_WelcomeWindow
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys


class WelcomeWindow(UI_WelcomeWindow.WelcomeWindow_UI, QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.products_without_budget_btn.clicked.connect(self.run_dialog_without_budget)
        self.shoplist_btn.clicked.connect(self.show_prieces)

    # params form
    def run_dialog_without_budget(self):
        self.dialog_window = DialogWithoutBudget()
        self.dialog_window.show()

    # Shop prices form
    def show_prieces(self):
        self.shoplist = ShopList()
        self.shoplist.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WelcomeWindow()
    ex.show()
    sys.exit(app.exec())
