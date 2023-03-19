import sys
from PyQt6.QtCore import  Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QCheckBox, QTextEdit, QPushButton, QComboBox, QSlider,
                             QGroupBox, QDial, QHBoxLayout, QWidget, QVBoxLayout)

class Examen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 7-12_2022")

        self.tedCadroTexto = QTextEdit()


        btnAbrirFich = QPushButton("Abrir ficheiro")
        btnReproducir = QPushButton("Reproducir ficheiro")
        btnGardar = QPushButton("Gardar")
        btnEliminar = QPushButton("Eliminar")

        dilVolume = QDial()
        chkAnimado = QCheckBox("Animado")


        btnSaltar = QPushButton("Saltar")
        cmbSaltar = QComboBox()


        opcionsReproduccion = QGroupBox("Opcións de reproducción")

        chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        chkEXML = QCheckBox("É XML")
        chkRepNPL = QCheckBox("Reproducción NPL")


        lblVolume = QLabel("volume:")
        lblFormato = QLabel("Formato:")
        lblSaidaAudio = QLabel("SaidaAudio")


        sldVolume = QSlider(Qt.Orientation.Horizontal)
        cmbFormato = QComboBox()
        cmbSaidaAudio = QComboBox()

        Hbox1 = QHBoxLayout()
        Hbox1.addWidget(self.tedCadroTexto)

        caixaH = QHBoxLayout()
        caixaH.addWidget(btnAbrirFich)
        caixaH.addWidget(btnReproducir)
        caixaH.addWidget(btnGardar)
        caixaH.addWidget(btnEliminar)

        caixaV11 = QVBoxLayout()
        caixaV11.addWidget(dilVolume)
        caixaV11.addWidget(chkAnimado)

        caixaH11 = QHBoxLayout()
        caixaH11.addWidget(btnSaltar)
        caixaH11.addWidget(cmbSaltar)

        caixaH5 = QHBoxLayout()
        caixaH5.addWidget(opcionsReproduccion)

        caixaV = QVBoxLayout()
        caixaV.addWidget(chkFiltrar)
        caixaV.addWidget(chkEXML)
        caixaV.addWidget(chkRepNPL)

        caixaV3 = QVBoxLayout()
        caixaV3.addWidget(lblVolume)
        caixaV3.addWidget(lblFormato)
        caixaV3.addWidget(lblSaidaAudio)

        caixaV3 = QVBoxLayout()
        caixaV3.addWidget(sldVolume)
        caixaV3.addWidget(cmbFormato)
        caixaV3.addWidget(cmbSaidaAudio)



        widget0 = QWidget()
        widget0.setLayout(caixaH11)
        caixaV11.addWidget(widget0)

        widget1 = QWidget()
        widget1.setLayout(caixaV11)
        Hbox1.addWidget(widget1)

        widget2 = QWidget()
        widget2.setLayout(caixaV3)
        caixaH5.addWidget(widget2)

        vBoxPrincipal = QVBoxLayout()
        w1 = QWidget()
        w1.setLayout(Hbox1)
        w2 = QWidget()
        w2.setLayout(caixaH5)
        vBoxPrincipal.addWidget(w1)
        vBoxPrincipal.addWidget(w2)


        widget = QWidget
        widget.setLayout(vBoxPrincipal)
        self.setCentralWidget(widget)
        self.show()





if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = Examen()
    aplicacion.exec()