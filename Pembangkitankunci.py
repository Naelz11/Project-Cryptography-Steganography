# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import rsa
import subprocess  # Import subprocess
from PyQt5.QtWidgets import QDialog, QMessageBox
from emkripsiRSA import Ui_Enkripsi  # Import Ui_Enkripsi dari file enkripsiRSA.py

class Ui_pembangkitanRSA(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 700)
        Dialog.setStyleSheet("")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(380, 170, 171, 25))
        self.label_6.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label_6.setObjectName("label_6")
        self.Nilai_Q = QtWidgets.QLineEdit(Dialog)
        self.Nilai_Q.setGeometry(QtCore.QRect(110, 250, 131, 20))
        self.Nilai_Q.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt")
        self.Nilai_Q.setObjectName("Nilai_Q")
        self.title_pembangkitankunci = QtWidgets.QLabel(Dialog)
        self.title_pembangkitankunci.setEnabled(True)
        self.title_pembangkitankunci.setGeometry(QtCore.QRect(180, 70, 381, 41))
        self.title_pembangkitankunci.setStyleSheet("color:rgb(255, 255, 255); font-size:15pt;")
        self.title_pembangkitankunci.setObjectName("title_pembangkitankunci")
        self.move_enkripsi = QtWidgets.QPushButton(Dialog)
        self.move_enkripsi.setGeometry(QtCore.QRect(400, 490, 111, 31))
        self.move_enkripsi.setStyleSheet("color:rgb(0, 0, 0); background-color:rgb(213, 213, 213); font-size:12pt; border-radius:5px;")
        self.move_enkripsi.setObjectName("move_enkripsi")
        self.Pilih_bilangan_prima = QtWidgets.QLabel(Dialog)
        self.Pilih_bilangan_prima.setGeometry(QtCore.QRect(110, 170, 190, 28))
        self.Pilih_bilangan_prima.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt ")
        self.Pilih_bilangan_prima.setObjectName("Pilih_bilangan_prima")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(380, 320, 141, 27))
        self.label_10.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label_10.setObjectName("label_10")
        self.Nilai_e = QtWidgets.QLineEdit(Dialog)
        self.Nilai_e.setGeometry(QtCore.QRect(380, 250, 131, 20))
        self.Nilai_e.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt")
        self.Nilai_e.setObjectName("Nilai_e")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(350, 360, 16, 20))
        self.label_9.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label_9.setObjectName("label_9")
        self.Nilai_P = QtWidgets.QLineEdit(Dialog)
        self.Nilai_P.setGeometry(QtCore.QRect(110, 200, 131, 20))
        self.Nilai_P.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt;")
        self.Nilai_P.setObjectName("Nilai_P")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(350, 250, 16, 25))
        self.label_8.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(350, 200, 16, 25))
        self.label_7.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 200, 16, 25))
        self.label.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label.setObjectName("label")
        self.Bangkitkankuncibutton = QtWidgets.QPushButton(Dialog)
        self.Bangkitkankuncibutton.setGeometry(QtCore.QRect(110, 320, 141, 41))
        self.Bangkitkankuncibutton.setStyleSheet("color:rgb(0, 0, 0); background-color:rgb(213, 213, 213);font-size:12pt; border-radius: 5px;")
        self.Bangkitkankuncibutton.setObjectName("Bangkitkankuncibutton")
        self.Nilai_n = QtWidgets.QLineEdit(Dialog)
        self.Nilai_n.setGeometry(QtCore.QRect(380, 200, 131, 20))
        self.Nilai_n.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt;")
        self.Nilai_n.setObjectName("Nilai_n")
        self.Nilai_d = QtWidgets.QLineEdit(Dialog)
        self.Nilai_d.setGeometry(QtCore.QRect(380, 360, 131, 20))
        self.Nilai_d.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt")
        self.Nilai_d.setObjectName("Nilai_d")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 250, 16, 25))
        self.label_5.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_5.setObjectName("label_5")
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("background-image: url(:/newPrefix/Users/user/Downloads/Premium Vector _ Circuit board Motherboard_ Blue technology background.jpeg);")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../../../../Users/user/Downloads/Premium Vector _ Circuit board Motherboard_ Blue technology background.jpeg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 190, 251, 231))
        self.label_2.setStyleSheet("image: url(:/icon/Users/user/Downloads/Locks_Silhouette_Vector_PNG__Black_Lock_Icon__Lock_Icons__Black_Icons__Black_Lock_PNG_Image_For_Free_Download-removebg.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.background.raise_()
        self.label_6.raise_()
        self.Nilai_Q.raise_()
        self.title_pembangkitankunci.raise_()
        self.move_enkripsi.raise_()
        self.Pilih_bilangan_prima.raise_()
        self.label_10.raise_()
        self.Nilai_e.raise_()
        self.label_9.raise_()
        self.Nilai_P.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.Bangkitkankuncibutton.raise_()
        self.Nilai_n.raise_()
        self.Nilai_d.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(30, 630, 81, 31))
        self.backbutton.setStyleSheet("font:11pt\n")
        self.backbutton.setObjectName("backbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Hubungkan tombol dengan fungsi
        self.Bangkitkankuncibutton.clicked.connect(self.generate_keys)
        self.move_enkripsi.clicked.connect(self.open_enkripsi)  
        self.backbutton.clicked.connect(self.open_RSA)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Kunci Publik Anda"))
        self.title_pembangkitankunci.setText(_translate("Dialog", "PEMBANGKITAN KUNCI RSA"))
        self.move_enkripsi.setText(_translate("Dialog", "Enkripsi"))
        self.Pilih_bilangan_prima.setText(_translate("Dialog", "Pilih Bilangan Prima"))
        self.label_10.setText(_translate("Dialog", "Kunci Privat Anda"))
        self.label_9.setText(_translate("Dialog", "d "))
        self.label_8.setText(_translate("Dialog", "e "))
        self.label_7.setText(_translate("Dialog", "n "))
        self.label.setText(_translate("Dialog", "P "))
        self.Bangkitkankuncibutton.setText(_translate("Dialog", "Bangkitkan Kunci"))
        self.label_5.setText(_translate("Dialog", "Q "))
        self.backbutton.setText(_translate("Dialog", "<-back"))

    def is_prime(self, n):
        """Fungsi untuk memeriksa apakah n adalah bilangan prima."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_keys(self):
        print("Tombol Bangkitkan Kunci diklik")

        try:
            # Mendapatkan input P dan Q
            p = int(self.Nilai_P.text())
            q = int(self.Nilai_Q.text())
            print(f"Nilai P: {p}, Nilai Q: {q}")  # Debugging statement

            # Validasi apakah P dan Q adalah bilangan prima
            if not self.is_prime(p) or not self.is_prime(q):
                QtWidgets.QMessageBox.warning(None, "Error", "P dan Q harus merupakan bilangan prima!")
                return

            print("P dan Q valid sebagai bilangan prima")  # Debugging statement

            # Generate key pair
            (pubkey, privkey) = rsa.newkeys(p * q)

            # Menampilkan kunci publik dan privat pada UI
            self.Nilai_n.setText(str(pubkey.n))
            self.Nilai_e.setText(str(pubkey.e))
            self.Nilai_d.setText(str(privkey.d))

            print("Kunci berhasil dibangkitkan")  # Debugging statement

            self.public_key_n = pubkey.n
            self.public_key_e = pubkey.e

            with open("private_key.pem", "wb") as f:
                f.write(privkey.save_pkcs1())

        except ValueError as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Input tidak valid. Masukkan bilangan bulat.\n{e}")
            print(f"Error: {e}")  # Debugging statement
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Terjadi kesalahan: {e}")
            print(f"Terjadi kesalahan: {e}")  # Debugging statement

    def open_enkripsi(self):
        """Fungsi untuk membuka jendela enkripsi"""
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Enkripsi()
        self.ui.setupUi(self.window, self.public_key_n, self.public_key_e)
        self.window.show()
    
    def open_RSA(self):
        """Fungsi untuk membuka jendela start"""
        from RSA import Ui_RSA
        self.window = QtWidgets.QDialog()
        self.ui = Ui_RSA()
        self.ui.setupUi(self.window)
        self.window.show()

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_pembangkitanRSA()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
