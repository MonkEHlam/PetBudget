# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

WINDOW_SIZE = 650, 350


class WelcomeWindow_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(WINDOW_SIZE[0], WINDOW_SIZE[1])
        Form.setMinimumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        Form.setMaximumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 603, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 67, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.title = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.products_without_budget_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.products_without_budget_btn.setFont(font)
        self.products_without_budget_btn.setObjectName("products_without_budget_btn")
        self.verticalLayout.addWidget(self.products_without_budget_btn)
        self.shoplist_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.shoplist_btn.setFont(font)
        self.shoplist_btn.setObjectName("shoplist_btn")
        self.verticalLayout.addWidget(self.shoplist_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PetBudget"))
        self.title.setText(_translate("Form", "                  Pet Budget"))
        self.products_without_budget_btn.setText(_translate("Form", "Составить список покупок"))
        self.shoplist_btn.setText(_translate("Form", "Посмотреть цены в супермаркетах"))
