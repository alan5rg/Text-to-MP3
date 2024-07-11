import sys
import os
from gtts import gTTS
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QMessageBox, QMenuBar, QLineEdit, QTextEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox, QSlider, QDial, QAction, QColorDialog
import qdarkstyle
from qdarkstyle import load_stylesheet, LightPalette, DarkPalette


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Texto a MP3")
        self.setFixedSize(540, 480)
        self.left = 0
        self.top = 0
        self.move(self.left,self.top)

        layout_principal = QVBoxLayout()
        self.texto_box = QTextEdit("escribe aquí el texto que quiere pasar a voz")
        self.nombre_mp3box = QLineEdit("archivo.mp3")
        boton_crear = QPushButton("Crear audio MP3")
        boton_escuchar = QPushButton("Escuchar audio MP3 creado")
        boton_textohabla = QPushButton("Texto a Voz")
        boton_crear.clicked.connect(self.textoMP3)
        boton_escuchar.clicked.connect(self.escucharMP3)
        boton_textohabla.clicked.connect(self.textoHabla)
        
        layout_principal.addWidget(self.texto_box)
        layout_principal.addWidget(self.nombre_mp3box)
        layout_principal.addWidget(boton_crear)
        layout_principal.addWidget(boton_escuchar)
        layout_principal.addWidget(boton_textohabla)

        contenedor_central = QWidget()
        contenedor_central.setLayout(layout_principal)
        self.setCentralWidget(contenedor_central)

    def textoMP3(self):
        tts = gTTS(self.texto_box.toPlainText(), lang='es', slow=False)
        tts.save(self.nombre_mp3box.text())

    def escucharMP3(self):
        os.system(f'parole -p {self.nombre_mp3box.text()}')

    def textoHabla(self):
         self.textoMP3()
         self.escucharMP3()
         
if __name__ == '__main__':
        app = QApplication(sys.argv)
        app.setStyleSheet(qdarkstyle.load_stylesheet(DarkPalette))
        #app.setStyleSheet(qdarkstyle.load_stylesheet(LightPalette))
      
        window = MainWindow()
        window.show()
        sys.exit(app.exec())