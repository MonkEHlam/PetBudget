from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication
from PyQt5.QtCore import Qt

from ui_files import UI_ShopList


class ShopList(QWidget, UI_ShopList.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase("QSQLITE")
        # Укажем имя базы данных
        db.setDatabaseName("Shop.db")
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        model = QSqlQueryModel()
        model.setQuery("SELECT title, cost, netweight FROM PriceList")
        model.setHeaderData(0, Qt.Orientation.Horizontal, "Наименование")
        model.setHeaderData(1, Qt.Orientation.Horizontal, "Цена")
        model.setHeaderData(2, Qt.Orientation.Horizontal, "Масса Нетто")
        self.view.setModel(model)
