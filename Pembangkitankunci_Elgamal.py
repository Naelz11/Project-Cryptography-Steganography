# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets 
from sympy import isprime, primitive_root
import random
from emkripsielgamal import Ui_enkripsielgamal
from cryptography.fernet import Fernet

class Ui_pembangkitanElgamal(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 700)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 130, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.background = QtWidgets.QLabel(Dialog)
        self.background.setGeometry(QtCore.QRect(-20, -20, 631, 741))
        self.background.setAutoFillBackground(False)
        self.background.setStyleSheet("background-image: url(:/newPrefix/Users/user/Downloads/Premium Vector _ Circuit board Motherboard_ Blue technology background.jpeg);")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("../../../../Users/user/Downloads/Premium Vector _ Circuit board Motherboard_ Blue technology background.jpeg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.logo_kunci = QtWidgets.QLabel(Dialog)
        self.logo_kunci.setGeometry(QtCore.QRect(135, 190, 341, 241))
        self.logo_kunci.setStyleSheet("image:url(:/newPrefix/Users/user/Downloads/Locks_Silhouette_Vector_PNG__Black_Lock_Icon__Lock_Icons__Black_Icons__Black_Lock_PNG_Image_For_Free_Download-removebg.png)")
        self.logo_kunci.setText("")
        self.logo_kunci.setObjectName("logo_kunci")
        self.Nilai_p = QtWidgets.QLineEdit(Dialog)
        self.Nilai_p.setGeometry(QtCore.QRect(390, 250, 131, 20))
        self.Nilai_p.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74);font-size:11pt;")
        self.Nilai_p.setObjectName("Nilai_p")
        self.Nilai_P = QtWidgets.QLineEdit(Dialog)
        self.Nilai_P.setGeometry(QtCore.QRect(120, 270, 131, 20))
        self.Nilai_P.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74);font-size:11pt;")
        self.Nilai_P.setObjectName("Nilai_P")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(370, 300, 16, 25))
        self.label_8.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label_8.setObjectName("label_8")
        self.title_pembangkitankunci = QtWidgets.QLabel(Dialog)
        self.title_pembangkitankunci.setEnabled(True)
        self.title_pembangkitankunci.setGeometry(QtCore.QRect(170, 100, 301, 41))
        self.title_pembangkitankunci.setStyleSheet("color:rgb(255, 255, 255); font-size:15pt;")
        self.title_pembangkitankunci.setObjectName("title_pembangkitankunci")
        self.move_enkripsibutton = QtWidgets.QPushButton(Dialog)
        self.move_enkripsibutton.setGeometry(QtCore.QRect(410, 550, 111, 31))
        self.move_enkripsibutton.setStyleSheet("color:rgb(0, 0, 0); background-color:rgb(213, 213, 213); font-size:11pt; border-radius:5px;")
        self.move_enkripsibutton.setObjectName("move_enkripsi")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(100, 270, 16, 21))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_3.setObjectName("label_3")
        self.Pilih_bilangan_prima = QtWidgets.QLabel(Dialog)
        self.Pilih_bilangan_prima.setGeometry(QtCore.QRect(120, 210, 141, 25))
        self.Pilih_bilangan_prima.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.Pilih_bilangan_prima.setObjectName("Pilih_bilangan_prima")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(370, 250, 16, 25))
        self.label_7.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_7.setObjectName("label_7")
        self.Bangkitkankuncibutton = QtWidgets.QPushButton(Dialog)
        self.Bangkitkankuncibutton.setGeometry(QtCore.QRect(130, 390, 121, 31))
        self.Bangkitkankuncibutton.setStyleSheet("color:rgb(0, 0, 0); background-color:rgb(213, 213, 213); font-size:11pt; border-radius: 5px;\n"
"")
        self.Bangkitkankuncibutton.setObjectName("Bangkitkankuncibutton")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(390, 410, 126, 21))
        self.label_10.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(390, 210, 129, 23))
        self.label_6.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_6.setObjectName("label_6")
        self.Nilai_g = QtWidgets.QLineEdit(Dialog)
        self.Nilai_g.setGeometry(QtCore.QRect(390, 300, 131, 20))
        self.Nilai_g.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt;")
        self.Nilai_g.setObjectName("Nilai_g")
        self.Nilai_h = QtWidgets.QLineEdit(Dialog)
        self.Nilai_h.setGeometry(QtCore.QRect(390, 350, 131, 20))
        self.Nilai_h.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt")
        self.Nilai_h.setObjectName("Nilai_h")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(370, 350, 16, 25))
        self.label_12.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(370, 450, 16, 25))
        self.label_13.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt")
        self.label_13.setObjectName("label_13")
        self.Nilai_privatx = QtWidgets.QLineEdit(Dialog)
        self.Nilai_privatx.setGeometry(QtCore.QRect(390, 450, 131, 20))
        self.Nilai_privatx.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt;")
        self.Nilai_privatx.setObjectName("Nilai_privatx")
        self.Nilai_privatP = QtWidgets.QLineEdit(Dialog)
        self.Nilai_privatP.setGeometry(QtCore.QRect(390, 490, 131, 20))
        self.Nilai_privatP.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(4, 40, 74); font-size:11pt;")
        self.Nilai_privatP.setObjectName("Nilai_privatP")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(370, 490, 16, 25))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_4.setObjectName("label_4")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(30, 630, 81, 31))
        self.backbutton.setStyleSheet("font:11pt\n")
        self.backbutton.setObjectName("backbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect the button to the function
        self.Bangkitkankuncibutton.clicked.connect(self.generate_keys)
        self.move_enkripsibutton.clicked.connect(self.go_to_enkripsi)
        self.backbutton.clicked.connect(self.open_Elgamal)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Pembangkit Kunci ElGamal"))
        self.label_8.setText(_translate("Dialog", "g"))
        self.title_pembangkitankunci.setText(_translate("Dialog", "PEMBANGKITAN KUNCI EL-GAMAL"))
        self.move_enkripsibutton.setText(_translate("Dialog", "Enkripsi"))
        self.label_3.setText(_translate("Dialog", "P"))
        self.Pilih_bilangan_prima.setText(_translate("Dialog", "Pilih Bilangan Prima"))
        self.label_7.setText(_translate("Dialog", "P"))
        self.Bangkitkankuncibutton.setText(_translate("Dialog", "Bangkitkan Kunci"))
        self.label_10.setText(_translate("Dialog", "Kunci Privat Anda"))
        self.label_6.setText(_translate("Dialog", "Kunci Publik Anda"))
        self.label_12.setText(_translate("Dialog", "h"))
        self.label_13.setText(_translate("Dialog", "x"))
        self.label_4.setText(_translate("Dialog", "P"))
        self.backbutton.setText(_translate("Dialog", "<-back"))

     # Import untuk memeriksa bilangan prima

    def generate_keys(self):
     try:
        # Mengambil nilai p dari input pengguna
        p = int(self.Nilai_P.text())
        
        # Validasi p harus bilangan prima
        if not isprime(p):
            raise ValueError("Nilai P harus bilangan prima yang valid.")
        
        # Pemilihan g yang lebih aman
        g = random.randint(2, p-1)
        # Secara opsional, lakukan pengecekan apakah g adalah akar primitif dari p
        
        # Menghitung kunci privat x dan kunci publik h
        x = random.randint(1, p-2)  # Menghasilkan kunci privat dengan aman
        h = pow(g, x, p)  # Menghitung kunci publik

        # Menampilkan kunci yang dihasilkan
        self.Nilai_p.setText(str(p))
        self.Nilai_g.setText(str(g))
        self.Nilai_h.setText(str(h))
        self.Nilai_privatx.setText(str(x))
        self.Nilai_privatP.setText(str(p))
        
        # Simpan kunci yang dibangkitkan ke dalam variabel
        self.generated_keys = {
            'p': p,
            'g': g,
            'x': x,
            'h': h
        }
     except ValueError as e:
          QtWidgets.QMessageBox.critical(None, "Input Error", str(e))
     except Exception as e:
          QtWidgets.QMessageBox.critical(None, "Error", f"Terjadi kesalahan: {str(e)}")


    def go_to_enkripsi(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_enkripsielgamal()

        # Kirimkan kunci publik ke halaman enkripsi
        self.ui.setupUi(self.window, self.generated_keys)
        self.window.show()
    
    def open_Elgamal(self):
        """Fungsi untuk membuka jendela start"""
        from Elgamal import Ui_Elgamal
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Elgamal()
        self.ui.setupUi(self.window)
        self.window.show()
        
import keylogo_rc

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_pembangkitanElgamal()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
