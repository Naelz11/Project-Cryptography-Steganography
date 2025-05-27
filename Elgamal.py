# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Elgamal(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 700)
        self.elgamal_background = QtWidgets.QLabel(Dialog)
        self.elgamal_background.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.elgamal_background.setStyleSheet("background-image:url(:/newPrefix/Users/user/Downloads/Free Vector _ Gradient geometric blue technology background.jpeg);\n"
"image:url(:/newPrefix/Users/user/Downloads/Locks Silhouette Vector PNG, Black Lock Icon, Lock Icons, Black Icons, Black Lock PNG Image For Free Download.jpeg)")
        self.elgamal_background.setText("")
        self.elgamal_background.setPixmap(QtGui.QPixmap("../../../../Users/user/Downloads/Premium Vector _ Circuit board Motherboard_ Blue technology background.jpeg"))
        self.elgamal_background.setScaledContents(True)
        self.elgamal_background.setObjectName("elgamal_background")
        self.Dekripsi_button = QtWidgets.QPushButton(Dialog)
        self.Dekripsi_button.setGeometry(QtCore.QRect(410, 260, 110, 61))
        self.Dekripsi_button.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 127), stop:1 rgba(0, 0, 0)); font-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255); ")
        self.Dekripsi_button.setObjectName("Dekripsi_button")
        self.elgamal_title = QtWidgets.QLabel(Dialog)
        self.elgamal_title.setGeometry(QtCore.QRect(260, 130, 121, 31))
        self.elgamal_title.setStyleSheet("color:rgb(255, 255, 255); font: 20pt \"MS Shell Dlg 2\";")
        self.elgamal_title.setObjectName("elgamal_title")
        self.Enkripsi_button = QtWidgets.QPushButton(Dialog)
        self.Enkripsi_button.setGeometry(QtCore.QRect(120, 260, 110, 61))
        self.Enkripsi_button.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 127), stop:1 rgba(0, 0, 0)); font-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255); \n"
"")
        self.Enkripsi_button.setObjectName("Enkripsi_button")
        self.ekstrakselgamal_button = QtWidgets.QPushButton(Dialog)
        self.ekstrakselgamal_button.setGeometry(QtCore.QRect(265, 260, 111, 61))
        self.ekstrakselgamal_button.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 85, 127), stop:1 rgba(0, 0, 0)); font-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255); ")
        self.ekstrakselgamal_button.setObjectName("ekstrakselgamal_button")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(30, 630, 81, 31))
        self.backbutton.setStyleSheet("font:11pt\n")
        self.backbutton.setObjectName("backbutton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Enkripsi_button.clicked.connect(self.open_pembangkitanElGamal)
        self.Dekripsi_button.clicked.connect(self.dekripsielgamal)
        self.ekstrakselgamal_button.clicked.connect(self.ekstrakelgamal)
        self.backbutton.clicked.connect(self.open_newekstrak)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ElGamal Encryption"))
        self.elgamal_title.setText(_translate("Dialog", "EL-GAMAL"))
        self.Dekripsi_button.setText(_translate("Dialog", "DEKRIPSI"))
        self.Enkripsi_button.setText(_translate("Dialog", "ENKRIPSI"))
        self.ekstrakselgamal_button.setText(_translate("Dialog", "EKSTRAK"))
        self.backbutton.setText(_translate("Dialog", "<-back"))


    def open_pembangkitanElGamal(self):
        from Pembangkitankunci_Elgamal import Ui_pembangkitanElgamal
        self.window = QtWidgets.QDialog()
        self.ui = Ui_pembangkitanElgamal()
        self.ui.setupUi(self.window)
        self.window.show()

    def dekripsielgamal(self):
        from dekripsielgamal import Ui_dekripsielgamal
        self.window = QtWidgets.QDialog()
        self.ui = Ui_dekripsielgamal()
        self.ui.setupUi(self.window)
        self.window.show()

    def ekstrakelgamal(self):
        from Ekstrakelgamal import Ui_ekstrakselgamal
        self.window = QtWidgets.QDialog()
        self.ui = Ui_ekstrakselgamal()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def open_newekstrak(self):
        """Fungsi untuk membuka jendela start"""
        from new_ekstraksi import Ui_ekstraksi
        self.window = QtWidgets.QDialog()
        self.ui = Ui_ekstraksi()
        self.ui.setupUi(self.window)
        self.window.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Elgamal()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
