import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QPushButton, QDial, QCheckBox, QComboBox, QGroupBox, QLabel, \
    QSlider, QHBoxLayout, QVBoxLayout, QWidget, QApplication


class Examen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen 7-12_2022")

        self.tedCadroTexto = QTextEdit()

        btnAbrirFich = QPushButton("Abrir fichero")
        btnReproducir = QPushButton("Reproducir ficheiro")
        btnGardar = QPushButton("Gardar")
        btnEliminar = QPushButton("Eliminar")

        dilVolume = QDial()
        chkAnimado = QCheckBox("Animado")

        btnSaltar = QPushButton("Saltar")
        btnSaltar.clicked.connect(self.on_saltarClicked)
        self.cmbSaltar = QComboBox()
        self.cmbSaltar.addItems(("0","1","2","3","4","5","6","7","8"))

        opcionsReproduccion = QGroupBox("Opcions de reproduccion")

        chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        chkEXML = QCheckBox("É XML")
        chkRepNPL = QCheckBox("Reproduccion NPL")

        lblVolumen = QLabel("Volumen:")

        lblFormato = QLabel("Formato:")
        lblSidaAudio = QLabel("SaidaAudio")

        self.sldVolume = QSlider()
        self.sldVolume.setMinimum(0)
        self.sldVolume.setMaximum(8)


        self.cmbFormato = QComboBox()
        self.cmbFormato.addItems(("mp3","wav","wma","ogg"))
        self.cmbFormato.currentTextChanged.connect(self.on_formatoChanged)
        CBSaidaAudio = QComboBox()


        caixaH1 = QHBoxLayout()
        caixaH1.addWidget((self.tedCadroTexto))

        caixaH2 = QHBoxLayout()
        caixaH2.addWidget(btnSaltar)
        caixaH2.addWidget(self.cmbSaltar)

        caixaV1 = QVBoxLayout()
        caixaV1.addWidget(dilVolume)
        caixaV1.addWidget(chkAnimado)

        caixaH3 = QHBoxLayout()
        caixaH3.addWidget(btnAbrirFich)
        caixaH3.addWidget(btnReproducir)
        caixaH3.addWidget(btnGardar)
        caixaH3.addWidget(btnEliminar)


        caixaV3 = QVBoxLayout()
        caixaV3.addWidget(chkEXML)
        caixaV3.addWidget(chkFiltrar)
        caixaV3.addWidget(chkRepNPL)

        opcionsReproduccion.setLayout(caixaV3)
        caixaH4 = QHBoxLayout()
        caixaH4.addWidget(opcionsReproduccion)

        caixaV2 = QVBoxLayout()
        caixaV2.addWidget(lblVolumen)
        caixaV2.addWidget(lblFormato)
        caixaV2.addWidget (lblSidaAudio)

        caixaV4 = QVBoxLayout()
        caixaV4.addWidget(self.sldVolume)
        caixaV4.addWidget(self.cmbFormato)
        caixaV4.addWidget(CBSaidaAudio)




        w1 = QWidget()
        w1.setLayout(caixaH2)
        caixaV1.addWidget(w1)

        w2 = QWidget()
        w2.setLayout(caixaV1)
        caixaH1.addWidget(w2)

       




        caixaH5 = QHBoxLayout()
        w3 = QWidget()
        w3.setLayout(caixaV2)
        caixaH5.addWidget(w3)

        w4 = QWidget()
        w4.setLayout(caixaV4)
        caixaH5.addWidget(w4)



        caixav5 = QVBoxLayout()
        w7 = QWidget()
        w7.setLayout(caixaH3)
        caixav5.addWidget(w7)


        w6 = QWidget()
        w6.setLayout(caixaH4)
        caixav5.addWidget(w6)


        w7 = QWidget()
        w7.setLayout(caixav5)
        caixaH5.addWidget(w7)


        caixaV8 = QVBoxLayout()
        w8 = QWidget()
        w8.setLayout(caixaH1)
        caixaV8.addWidget(w8)

        w9 = QWidget()
        w9.setLayout(caixaH5)
        caixaV8.addWidget(w9)

        widgetFinal = QWidget()
        widgetFinal.setLayout(caixaV8)
        self.setCentralWidget(widgetFinal)
        self.show()

    def on_formatoChanged(self):
        print("formato:" + self.cmbFormato.currentText())

    def on_saltarClicked(self):
        self.sldVolume.setValue(int(self.cmbSaltar.currentText()))


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = Examen()
    aplicacion.exec()