# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Login")
        Dialog.resize(480, 620)
        Dialog.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 50, 121, 71))
        self.label.setStyleSheet("color:rgb(225, 225, 225); font-size:28pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 111, 31))
        self.label_2.setStyleSheet("font-size:15pt; color:rgb(255, 0, 127)")
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(170, 150, 241, 51))
        self.email.setStyleSheet("font-size:14pt; color:rgb(243, 243, 243)")
        self.email.setObjectName("email")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(170, 260, 241, 51))
        self.password.setStyleSheet("font-size:14pt; color:rgb(243, 243, 243)")
        self.password.setText("")
        self.password.setObjectName("password")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 270, 111, 31))
        self.label_3.setStyleSheet("font-size:15pt; color:rgb(255, 0, 127)")
        self.label_3.setObjectName("label_3")
        self.loginbutton = QtWidgets.QPushButton(Dialog)
        self.loginbutton.setGeometry(QtCore.QRect(270, 350, 141, 41))
        self.loginbutton.setStyleSheet("background-color: rgb(167, 168, 167); font-size:14pt; color:rgb(255, 255, 255)")
        self.loginbutton.setObjectName("loginbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ahmed Corrugation Management System"))
        self.label.setText(_translate("Dialog", "Login"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.loginbutton.setText(_translate("Dialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
