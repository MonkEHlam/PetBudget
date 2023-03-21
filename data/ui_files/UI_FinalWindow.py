# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

WINDOW_SIZE = 460, 300


class FinalWindow_UI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(WINDOW_SIZE[0], WINDOW_SIZE[1])
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 301, 281))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 240, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 10, 131, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.protein_label = QtWidgets.QLabel(self.layoutWidget)
        self.protein_label.setObjectName("protein_label")
        self.horizontalLayout.addWidget(self.protein_label)
        self.proteins_lcd = QtWidgets.QLCDNumber(self.layoutWidget)
        self.proteins_lcd.setObjectName("proteins_lcd")
        self.horizontalLayout.addWidget(self.proteins_lcd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fats_label = QtWidgets.QLabel(self.layoutWidget)
        self.fats_label.setObjectName("fats_label")
        self.horizontalLayout_2.addWidget(self.fats_label)
        self.fats_lcd = QtWidgets.QLCDNumber(self.layoutWidget)
        self.fats_lcd.setObjectName("fats_lcd")
        self.horizontalLayout_2.addWidget(self.fats_lcd)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cbhs_lcd = QtWidgets.QLCDNumber(self.layoutWidget)
        self.cbhs_lcd.setObjectName("cbhs_lcd")
        self.horizontalLayout_3.addWidget(self.cbhs_lcd)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.textBrowser, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Список покупок"))
        self.textBrowser.setHtml(
            _translate(
                "Form",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("Form", "Сохранить как txt"))
        self.label.setText(_translate("Form", "Баланс Элементов"))
        self.protein_label.setText(_translate("Form", "Белки"))
        self.fats_label.setText(_translate("Form", "Жиры"))
        self.label_4.setText(_translate("Form", "Углеводы"))
