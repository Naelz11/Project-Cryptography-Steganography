import os
import numpy as np
from scipy.io import wavfile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from scipy.fftpack import fft, ifft
import hashlib
from docx import Document
import wave
import struct
import math

from startwindow import Ui_startwindow

class Ui_Embedd(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 700)
        self.embedd_background = QtWidgets.QLabel(Dialog)
        self.embedd_background.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.embedd_background.setStyleSheet("background-image:url(:/newPrefix/Users/user/Downloads/Free Vector _ Gradient geometric blue technology background.jpeg);\n"
"image:url(:/newPrefix/Users/user/Downloads/Locks Silhouette Vector PNG, Black Lock Icon, Lock Icons, Black Icons, Black Lock PNG Image For Free Download.jpeg)")
        self.embedd_background.setText("")
        self.embedd_background.setPixmap(QtGui.QPixmap("../../../../Users/user/Downloads/Premium Vector _ Circuit board Motherboard_ Blue technology background.jpeg"))
        self.embedd_background.setScaledContents(True)
        self.embedd_background.setObjectName("embedd_background")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 110, 261, 71))
        self.label.setStyleSheet("color:rgb(255, 255, 255); font-size:20pt;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 151, 31))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_2.setObjectName("label_2")
        self.input_pesanrahasia = QtWidgets.QLineEdit(Dialog)
        self.input_pesanrahasia.setGeometry(QtCore.QRect(240, 230, 171, 31))
        self.input_pesanrahasia.setStyleSheet("background-color:rgb(3, 41, 77); color:rgb(255, 255, 255); font-size:11pt")
        self.input_pesanrahasia.setObjectName("input_pesanrahasia")
        self.browsefile = QtWidgets.QPushButton(Dialog)
        self.browsefile.setGeometry(QtCore.QRect(440, 230, 81, 31))
        self.browsefile.setStyleSheet("")
        self.browsefile.setObjectName("browsefile")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 290, 151, 31))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 430, 121, 31))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.label_4.setObjectName("label_4")
        self.input_stegofile = QtWidgets.QLineEdit(Dialog)
        self.input_stegofile.setGeometry(QtCore.QRect(240, 290, 171, 31))
        self.input_stegofile.setStyleSheet("background-color:rgb(3, 41, 77); color:rgb(255, 255, 255); font-size:11pt")
        self.input_stegofile.setObjectName("input_stegofile")
        self.hasil_embed = QtWidgets.QLineEdit(Dialog)
        self.hasil_embed.setGeometry(QtCore.QRect(210, 480, 191, 31))
        self.hasil_embed.setStyleSheet("background-color:rgb(3, 41, 77); color:rgb(255, 255, 255); font-size:11pt")
        self.hasil_embed.setObjectName("hasil_embed")
        self.browse_audio = QtWidgets.QPushButton(Dialog)
        self.browse_audio.setGeometry(QtCore.QRect(440, 290, 81, 31))
        self.browse_audio.setStyleSheet("")
        self.browse_audio.setObjectName("browse_audio")
        self.save_file = QtWidgets.QPushButton(Dialog)
        self.save_file.setGeometry(QtCore.QRect(420, 480, 81, 31))
        self.save_file.setStyleSheet("")
        self.save_file.setObjectName("save_file")
        self.backbutton = QtWidgets.QPushButton(Dialog)
        self.backbutton.setGeometry(QtCore.QRect(30, 630, 81, 31))
        self.backbutton.setStyleSheet("font:11pt\n"
"")
        self.backbutton.setObjectName("backbutton")
        self.embedbutton = QtWidgets.QPushButton(Dialog)
        self.embedbutton.setGeometry(QtCore.QRect(440, 350, 81, 31))
        self.embedbutton.setStyleSheet("")
        self.embedbutton.setObjectName("embed_file")
        self.input_key = QtWidgets.QLabel(Dialog)
        self.input_key.setGeometry(QtCore.QRect(70, 350, 151, 31))
        self.input_key.setStyleSheet("color:rgb(255, 255, 255); font-size:12pt;")
        self.input_key.setObjectName("label_5")
        self.input_stegokey = QtWidgets.QLineEdit(Dialog)
        self.input_stegokey.setGeometry(QtCore.QRect(240, 350, 91, 31))
        self.input_stegokey.setStyleSheet("background-color:rgb(3, 41, 77); color:rgb(255, 255, 255); font-size:11pt")
        self.input_stegokey.setObjectName("input_stegokey")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.browsefile.clicked.connect(self.browse_file)
        self.browse_audio.clicked.connect(self.browse_audio_file)
        self.embedbutton.clicked.connect(self.embed_file_method)
        self.save_file.clicked.connect(self.save_file_method)
        self.backbutton.clicked.connect(self.open_startwindow)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "EMBED MESSAGE"))
        self.label_2.setText(_translate("Dialog", "Input Pesan Rahasia "))
        self.browsefile.setText(_translate("Dialog", "Browse"))
        self.label_3.setText(_translate("Dialog", "Input Stego Audio"))
        self.label_4.setText(_translate("Dialog", "Hasil Embedded"))
        self.browse_audio.setText(_translate("Dialog", "Browse audio"))
        self.save_file.setText(_translate("Dialog", "Simpan"))
        self.backbutton.setText(_translate("Dialog", "<-back"))
        self.embedbutton.setText(_translate("Dialog", "Embed"))
        self.input_key.setText(_translate("Dialog", "Input Stego Key"))

    def browse_audio_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(None, "Pilih File Audio", "", "WAV Files (*.wav)", options=options)
        if file:
            self.input_stegofile_path = file
            self.input_stegofile.setText(f"File Audio Terpilih: {file}")
            self.input_stegofile.setText(file)

    def browse_file(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(None, "Pilih File DOCX", "", "DOCX Files (*.docx)", options=options)
        if file:
            self.input_pesanrahasia_path = file
            self.input_pesanrahasia.setText(f"File Dokumen Terpilih: {file}")
            self.input_pesanrahasia.setText(file)
            

    def embed_file_method(self):
        input_audio = self.input_stegofile.text()
        input_docx = self.input_pesanrahasia.text()
        stego_key = self.input_stegokey.text()

        if not input_audio or not input_docx or not stego_key:
            QMessageBox.warning(None, "Input Error", "Semua input harus diisi!")
            return

        try:
        # Membaca file DOCX sebagai byte
            with open(input_docx, 'rb') as docx_file:
                docx_data = docx_file.read()

        # Hash kunci sebagai validasi tambahan
            key_hash = hashlib.md5(stego_key.encode()).digest()
            print("[DEBUG] Embed key hash:", key_hash)

        # Membuka file WAV
            with wave.open(input_audio, 'rb') as wav_file:
                params = wav_file.getparams()
                frames = bytearray(wav_file.readframes(wav_file.getnframes()))

        # Menyiapkan data untuk disisipkan (hash + panjang data + data DOCX)
            data_to_embed = key_hash + struct.pack('<I', len(docx_data)) + docx_data
            bits_to_embed = ''.join(f'{byte:08b}' for byte in data_to_embed)  # Konversi ke bit-string

            if len(bits_to_embed) > len(frames) * 8:
                QMessageBox.critical(None, "Error", "Ukuran data terlalu besar untuk file audio.")
                return

        # Sisipkan bit ke dalam LSB dari setiap byte dalam frames
            frame_index = 0
            for bit in bits_to_embed:
                frames[frame_index] = (frames[frame_index] & 0xFE) | int(bit)  # Ganti LSB
                frame_index += 1
            # Membaca file audio asli untuk perhitungan PSNR dan SNR
            try:
                with wave.open(input_audio, 'rb') as original_audio:
                    original_frames = bytearray(original_audio.readframes(original_audio.getnframes()))
            except Exception as e:
                QMessageBox.critical(None, "Error", f"Gagal membaca file audio asli untuk PSNR/SNR: {str(e)}")
                return

       
        # Validasi panjang data
            if len(frames) != len(original_frames):
                QMessageBox.critical(None, "Error", "File audio hasil embedding memiliki panjang yang berbeda dengan file asli.")
                return
        # Hitung noise power dan sinyal asli
            noise = [frames[i] - original_frames[i] for i in range(len(frames))]
            signal_power = sum(x**2 for x in original_frames) / len(original_frames)
            noise_power = sum(x**2 for x in noise) / len(noise)

        # Hitung PSNR dan SNR
            if noise_power > 0:
                psnr = 10 * math.log10((255**2) / noise_power)
                snr = 10 * math.log10(signal_power / noise_power)
            else:
                psnr = float('inf')  # Tidak ada noise
                snr = float('inf')  # Tidak ada noise

        # Menyimpan hasil embedding dalam buffer
            self.embed_result = {
                "params": params,
                "frames": bytes(frames),
            }

        # Menampilkan hasil embedding dan PSNR/SNR
            QMessageBox.information(None, "Success",
            f"Proses embedding berhasil. Silakan simpan file.\nPSNR: {psnr:.2f} dB\nSNR: {snr:.2f} dB")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Terjadi kesalahan: {str(e)}")


    def save_file_method(self):
        if not hasattr(self, 'embed_result'):
            QMessageBox.warning(None, "Tidak Ada Data", "Lakukan embedding terlebih dahulu sebelum menyimpan.")
            return

        options = QFileDialog.Options()
        output_audio, _ = QFileDialog.getSaveFileName(
            None, "Simpan File Audio", "", "WAV Files (*.wav)", options=options
        )

        if output_audio:
            try:
            # Ambil hasil embedding dari buffer
                embed_result = self.embed_result
                params = embed_result["params"]
                frames = embed_result["frames"]

            # Buat file WAV baru dengan data embed
                with wave.open(output_audio, 'wb') as wav_output:
                    wav_output.setparams(params)
                    wav_output.writeframes(frames)

                QMessageBox.information(None, "Simpan Berhasil", f"File berhasil disimpan di: {output_audio}")
            except Exception as e:
                QMessageBox.critical(None, "Simpan Gagal", f"Gagal menyimpan file: {str(e)}")
        else:
            QMessageBox.warning(None, "Save Error", "Proses penyimpanan dibatalkan.")
            
    def open_startwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_startwindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Embedd()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

