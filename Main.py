# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ahmed Corrugation Machines")
        MainWindow.resize(1479, 962)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.existing_client = QtWidgets.QPushButton(self.centralwidget)
        self.existing_client.setGeometry(QtCore.QRect(520, 880, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(12)
        self.existing_client.setFont(font)
        self.existing_client.setObjectName("existing_client")
        self.createLedger = QtWidgets.QPushButton(self.centralwidget)
        self.createLedger.setGeometry(QtCore.QRect(1190, 880, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(12)
        self.createLedger.setFont(font)
        self.createLedger.setObjectName("createLedger")
        self.createLedger_2 = QtWidgets.QPushButton(self.centralwidget)
        self.createLedger_2.setGeometry(QtCore.QRect(880, 880, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(12)
        self.createLedger_2.setFont(font)
        self.createLedger_2.setObjectName("createLedger_2")
        self.ClientTable = QtWidgets.QTableView(self.centralwidget)
        self.ClientTable.setGeometry(QtCore.QRect(380, 30, 1091, 821))
        self.ClientTable.setObjectName("ClientTable")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ahmed Corrugation Machines"))
        self.existing_client.setText(_translate("MainWindow", "Open Client Ledger"))
        self.createLedger.setText(_translate("MainWindow", "Add New Client "))
        self.createLedger_2.setText(_translate("MainWindow", "Cash Sale"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())
