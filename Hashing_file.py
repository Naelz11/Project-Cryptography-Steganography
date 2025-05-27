import hashlib
import docx
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 700)
        self.ekstrak_background = QtWidgets.QLabel(Dialog)
        self.ekstrak_background.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.ekstrak_background.setStyleSheet("background-image:url(:/newPrefix/Users/user/Downloads/Free Vector _ Gradient geometric blue technology background.jpeg);\n"
"image:url(:/newPrefix/Users/user/Downloads/Locks Silhouette Vector PNG, Black Lock Icon, Lock Icons, Black Icons, Black Lock PNG Image For Free Download.jpeg)")
        self.ekstrak_background.setText("")
        self.ekstrak_background.setPixmap(QtGui.QPixmap("../../../../Users/user/Downloads/Premium Vector _ Circuit board Motherboard_ Blue technology background.jpeg"))
        self.ekstrak_background.setScaledContents(True)
        self.ekstrak_background.setObjectName("ekstrak_background")
        self.title_pembangkitankunci = QtWidgets.QLabel(Dialog)
        self.title_pembangkitankunci.setEnabled(True)
        self.title_pembangkitankunci.setGeometry(QtCore.QRect(240, 140, 141, 41))
        self.title_pembangkitankunci.setStyleSheet("color:rgb(255, 255, 255); font-size:20pt;")
        self.title_pembangkitankunci.setObjectName("title_pembangkitankunci")
        self.Inputembedded = QtWidgets.QLabel(Dialog)
        self.Inputembedded.setGeometry(QtCore.QRect(70, 270, 151, 31))
        self.Inputembedded.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.Inputembedded.setObjectName("Inputembedded")
        self.browsebutton = QtWidgets.QPushButton(Dialog)
        self.browsebutton.setGeometry(QtCore.QRect(430, 270, 81, 31))
        self.browsebutton.setStyleSheet("")
        self.browsebutton.setObjectName("browsebutton")
        self.input_embedded = QtWidgets.QLineEdit(Dialog)
        self.input_embedded.setGeometry(QtCore.QRect(230, 270, 171, 31))
        self.input_embedded.setStyleSheet("background-color:rgb(3, 41, 77); color:rgb(255, 255, 255); font-size:11pt")
        self.input_embedded.setText("")
        self.input_embedded.setObjectName("input_embedded")
        self.Hasil_hash = QtWidgets.QLineEdit(Dialog)
        self.Hasil_hash.setGeometry(QtCore.QRect(230, 430, 181, 31))
        self.Hasil_hash.setStyleSheet("background-color:rgb(3, 41, 77); color:rgb(255, 255, 255); font-size:11pt")
        self.Hasil_hash.setObjectName("Hasil_hash")
        self.start_hashing = QtWidgets.QPushButton(Dialog)
        self.start_hashing.setGeometry(QtCore.QRect(280, 330, 81, 31))
        self.start_hashing.setStyleSheet("")
        self.start_hashing.setObjectName("start_hashing")
        self.Hasilembedded = QtWidgets.QLabel(Dialog)
        self.Hasilembedded.setGeometry(QtCore.QRect(70, 430, 151, 31))
        self.Hasilembedded.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.Hasilembedded.setObjectName("Hasilembedded")
        self.savebutton = QtWidgets.QPushButton(Dialog)
        self.savebutton.setGeometry(QtCore.QRect(440, 430, 81, 31))
        self.savebutton.setStyleSheet("")
        self.savebutton.setObjectName("savebutton")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(30, 630, 81, 31))
        self.backbutton.setStyleSheet("font:11pt\n"
"")
        self.backbutton.setObjectName("backbutton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        # Connect buttons to their functions
        self.browsebutton.clicked.connect(self.browse_file)
        self.start_hashing.clicked.connect(self.hashing)
        self.savebutton.clicked.connect(self.save_hash_encrypt)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Hash Encrypt"))
        self.title_pembangkitankunci.setText(_translate("Dialog", "HASH MD5"))
        self.Inputembedded.setText(_translate("Dialog", "Pilih File Enkripsi"))
        self.browsebutton.setText(_translate("Dialog", "Browse"))
        self.start_hashing.setText(_translate("Dialog", "Mulai"))
        self.Hasilembedded.setText(_translate("Dialog", "Hasil Hashing File"))
        self.savebutton.setText(_translate("Dialog", "Simpan"))
        self.backbutton.setText(_translate("Dialog", "<-back"))

    def browse_file(self):
        options = QtWidgets.QFileDialog.Options()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Pilih File DOCX", "", "Word Documents (*.docx); All Files (*)", options=options)
        if file_name:
            self.input_embedded.setText(file_name)

    def hashing(self):
        file_path = self.input_embedded.text()
        if not file_path:
            QtWidgets.QMessageBox.warning(None, "Peringatan", "Pilih file terlebih dahulu!")
            return

        try:
            # Baca isi file sebagai byte
            with open(file_path, 'rb') as f:
                file_data = f.read()

            # Hitung hash MD5 dari file
            md5_hash = hashlib.md5(file_data).hexdigest()

            # Tampilkan hasil hash di kolom Hasil_hash
            self.Hasil_hash.setText(md5_hash)

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"Terjadi kesalahan saat menghitung hash: {e}")

    def save_hash_encrypt(self):
      file_path = self.input_embedded.text()
      if not file_path:
        QtWidgets.QMessageBox.warning(None, "Peringatan", "Pilih file terlebih dahulu!")
        return
    
      hash_value = self.Hasil_hash.text()
      if not hash_value:
        QtWidgets.QMessageBox.warning(None, "Peringatan", "Hash belum dibuat!")
        return
    
      try:
        # Buka file asli dalam mode append ('a') untuk menambahkan hasil hash tanpa menghapus isinya
        with open(file_path, 'a') as f:
            # Tambahkan hasil hash ke file
            f.write(f"\n\nHash MD5 dari file ini: {hash_value}")
        
        QtWidgets.QMessageBox.information(None, "Sukses", f"Hash berhasil disimpan ke file: {file_path}")
    
      except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Error", f"Terjadi kesalahan saat menyimpan file: {e}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
