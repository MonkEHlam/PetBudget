# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

WINDOW_SIZE = 345, 540


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.view = QtWidgets.QTableView(Form)
        self.view.setGeometry(QtCore.QRect(10, 10, 325, 520))
        self.view.setObjectName("view")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Цены"))
