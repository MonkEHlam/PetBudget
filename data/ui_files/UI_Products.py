from PyQt5 import QtCore, QtGui, QtWidgets

WINDOW_SIZE = (310, 430)


class Products_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(WINDOW_SIZE[0], WINDOW_SIZE[1])
        Form.setMinimumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        Form.setMaximumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 291, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.proteins_cb1 = QtWidgets.QComboBox(self.layoutWidget)
        self.proteins_cb1.setObjectName("proteins_cb1")
        self.proteins_cb1.addItem("")
        self.proteins_cb1.addItem("")
        self.proteins_cb1.addItem("")
        self.proteins_cb1.addItem("")
        self.proteins_cb1.addItem("")
        self.verticalLayout.addWidget(self.proteins_cb1)
        self.proteins_cb2 = QtWidgets.QComboBox(self.layoutWidget)
        self.proteins_cb2.setObjectName("proteins_cb2")
        self.proteins_cb2.addItem("")
        self.proteins_cb2.addItem("")
        self.proteins_cb2.addItem("")
        self.proteins_cb2.addItem("")
        self.proteins_cb2.addItem("")
        self.proteins_cb2.addItem("")
        self.verticalLayout.addWidget(self.proteins_cb2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.milk_cb1 = QtWidgets.QComboBox(self.layoutWidget)
        self.milk_cb1.setObjectName("milk_cb1")
        self.milk_cb1.addItem("")
        self.milk_cb1.addItem("")
        self.milk_cb1.addItem("")
        self.verticalLayout_2.addWidget(self.milk_cb1)
        self.milk_cb2 = QtWidgets.QComboBox(self.layoutWidget)
        self.milk_cb2.setObjectName("milk_cb2")
        self.milk_cb2.addItem("")
        self.milk_cb2.addItem("")
        self.milk_cb2.addItem("")
        self.milk_cb2.addItem("")
        self.verticalLayout_2.addWidget(self.milk_cb2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.vegetables_cb1 = QtWidgets.QComboBox(self.layoutWidget)
        self.vegetables_cb1.setObjectName("vegetables_cb1")
        self.vegetables_cb1.addItem("")
        self.vegetables_cb1.addItem("")
        self.vegetables_cb1.addItem("")
        self.vegetables_cb1.addItem("")
        self.verticalLayout_3.addWidget(self.vegetables_cb1)
        self.vegetables_cb2 = QtWidgets.QComboBox(self.layoutWidget)
        self.vegetables_cb2.setObjectName("vegetables_cb2")
        self.vegetables_cb2.addItem("")
        self.vegetables_cb2.addItem("")
        self.vegetables_cb2.addItem("")
        self.vegetables_cb2.addItem("")
        self.vegetables_cb2.addItem("")
        self.verticalLayout_3.addWidget(self.vegetables_cb2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.porige_cb = QtWidgets.QComboBox(self.layoutWidget)
        self.porige_cb.setObjectName("porige_cb")
        self.porige_cb.addItem("")
        self.porige_cb.addItem("")
        self.porige_cb.addItem("")
        self.verticalLayout_4.addWidget(self.porige_cb)
        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.ok_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Продукты"))
        self.label.setText(_translate("Form", "Белковые продукты"))
        self.proteins_cb1.setItemText(0, _translate("Form", "Говядина"))
        self.proteins_cb1.setItemText(1, _translate("Form", "Свинина"))
        self.proteins_cb1.setItemText(2, _translate("Form", "Курица"))
        self.proteins_cb1.setItemText(3, _translate("Form", "Яйца"))
        self.proteins_cb1.setItemText(4, _translate("Form", "Печень"))
        self.proteins_cb2.setItemText(0, _translate("Form", "-"))
        self.proteins_cb2.setItemText(1, _translate("Form", "Говядина"))
        self.proteins_cb2.setItemText(2, _translate("Form", "Свинина"))
        self.proteins_cb2.setItemText(3, _translate("Form", "Курица"))
        self.proteins_cb2.setItemText(4, _translate("Form", "Яйца"))
        self.proteins_cb2.setItemText(5, _translate("Form", "Печень"))
        self.label_2.setText(_translate("Form", "Молочные продкты"))
        self.milk_cb1.setItemText(0, _translate("Form", "Молоко"))
        self.milk_cb1.setItemText(1, _translate("Form", "Творог"))
        self.milk_cb1.setItemText(2, _translate("Form", "Простокваша"))
        self.milk_cb2.setItemText(0, _translate("Form", "-"))
        self.milk_cb2.setItemText(1, _translate("Form", "Молоко"))
        self.milk_cb2.setItemText(2, _translate("Form", "Творог"))
        self.milk_cb2.setItemText(3, _translate("Form", "Простокваша"))
        self.label_3.setText(_translate("Form", "Овощи"))
        self.vegetables_cb1.setItemText(0, _translate("Form", "Морковь"))
        self.vegetables_cb1.setItemText(1, _translate("Form", "Капуста"))
        self.vegetables_cb1.setItemText(2, _translate("Form", "Салат зеленый"))
        self.vegetables_cb1.setItemText(3, _translate("Form", "Свёкла"))
        self.vegetables_cb2.setItemText(0, _translate("Form", "-"))
        self.vegetables_cb2.setItemText(1, _translate("Form", "Морковь"))
        self.vegetables_cb2.setItemText(2, _translate("Form", "Капуста"))
        self.vegetables_cb2.setItemText(3, _translate("Form", "Салат"))
        self.vegetables_cb2.setItemText(4, _translate("Form", "Свёкла"))
        self.label_4.setText(_translate("Form", "Крупы"))
        self.porige_cb.setItemText(0, _translate("Form", "Крупа овсяная"))
        self.porige_cb.setItemText(1, _translate("Form", "Крупа гречневая"))
        self.porige_cb.setItemText(2, _translate("Form", "Крупа перловая"))
        self.ok_btn.setText(_translate("Form", "OK"))
        self.cancel_btn.setText(_translate("Form", "Назад"))
