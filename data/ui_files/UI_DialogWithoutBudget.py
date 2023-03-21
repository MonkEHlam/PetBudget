# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

WINDOW_SIZE = 450, 250


class DialogWithoutBudget_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(WINDOW_SIZE[0], WINDOW_SIZE[1])
        Form.setMinimumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        Form.setMaximumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 251))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem1)
        self.natural_nutritation_btn = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.natural_nutritation_btn.setFont(font)
        self.natural_nutritation_btn.setObjectName("natural_nutritation_btn")
        self.horizontalLayout.addWidget(self.natural_nutritation_btn)
        spacerItem2 = QtWidgets.QSpacerItem(
            52, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem2)
        self.ready_food_btn = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ready_food_btn.setFont(font)
        self.ready_food_btn.setObjectName("ready_food_btn")
        self.horizontalLayout.addWidget(self.ready_food_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.verticalLayout.addItem(spacerItem3)
        self.dog_mass_scroll = QtWidgets.QSpinBox(self.layoutWidget)
        self.dog_mass_scroll.setMinimum(3)
        self.dog_mass_scroll.setMaximum(50)
        self.dog_mass_scroll.setSuffix("")
        self.dog_mass_scroll.setObjectName("dog_mass_scroll")
        self.verticalLayout.addWidget(self.dog_mass_scroll)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem4)
        self.ok_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.ok_btn.setObjectName("ok_btn")
        self.dialog_btns = QtWidgets.QButtonGroup(Form)
        self.dialog_btns.setObjectName("dialog_btns")
        self.dialog_btns.addButton(self.ok_btn)
        self.horizontalLayout_2.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.dialog_btns.addButton(self.cancel_btn)
        self.horizontalLayout_2.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.radiobtns = QtWidgets.QButtonGroup()
        self.radiobtns.addButton(self.ready_food_btn)
        self.radiobtns.addButton(self.natural_nutritation_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Выберете параметры"))
        self.natural_nutritation_btn.setText(_translate("Form", "Натуральное питание"))
        self.ready_food_btn.setText(_translate("Form", "Готовые корма"))
        self.dog_mass_scroll.setPrefix(
            _translate("Form", "Масса собаки (в кг. с окргулением до целого):")
        )
        self.ok_btn.setText(_translate("Form", "OK"))
        self.cancel_btn.setText(_translate("Form", "Назад"))
