import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QCheckBox, QTextEdit, QPushButton, QComboBox, QSlider,
                             QGroupBox, QDial, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen Recuperacion 2EV")

        self.tedCadroTexto = QTextEdit()

        btnAbrirFich = QPushButton("Abrir Ficheiro")
        btnReproducir = QPushButton("Reproducir Ficheiro")
        btnGuardar = QPushButton("Guardar")
        btnEliminar = QPushButton("Eliminar")

        btnSaltar = QPushButton("Saltar")
        btnSaltar.clicked.connect(self.on_saltarClicked)
        self.cmbSaltar = QComboBox()
        self.cmbSaltar.addItems(("0", "1", "2", "3", "4", "5", "6", "7", "8" , "9"))

        chkAnimado = QCheckBox("Animado")

        self.dilVolumne = QDial()
        self.dilVolumne.valueChanged.connect(self.on_sliderChanged)

        opcionsReproduccion = QGroupBox("Opcións de reproducción")

        self.chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        self.chkFiltrar.clicked.connect(self.on_chkFiltrar_select)
        self.chkXML = QCheckBox("É XML")
        self.chkXML.clicked.connect(self.on_chkXML_select)
        self.chkRepNPL = QCheckBox("Reproducción NPL")
        self.chkRepNPL.clicked.connect(self.on_chkRepNPL_select)

        lblVolumen = QLabel("Volumen: ")
        lblFormato = QLabel("Formato: ")
        lblSaidaAudio = QLabel("Saida Audio: ")

        self.sldVolumen = QSlider(Qt.Orientation.Horizontal)

        self.cmbFormato = QComboBox()
        self.cmbFormato.addItems(("mp3", "wav", "wma", "ogg"))
        self.cmbFormato.currentTextChanged.connect(self.on_formatoChanged)

        cmbSaidaAudio = QComboBox()




        hBoxSaltar = QHBoxLayout()
        hBoxSaltar.addWidget(btnSaltar)
        hBoxSaltar.addWidget(self.cmbSaltar)

        vBoxDial = QVBoxLayout()
        vBoxDial.addWidget(self.dilVolumne)
        vBoxDial.addWidget(chkAnimado)


        hBoxBotones = QHBoxLayout()
        hBoxBotones.addWidget(btnAbrirFich)
        hBoxBotones.addWidget(btnReproducir)
        hBoxBotones.addWidget(btnGuardar)
        hBoxBotones.addWidget(btnEliminar)

        vBoxOpciones = QVBoxLayout()
        vBoxOpciones.addWidget(self.chkFiltrar)
        vBoxOpciones.addWidget(self.chkXML)
        vBoxOpciones.addWidget(self.chkRepNPL)
        opcionsReproduccion.setLayout(vBoxOpciones)
        hBoxOpcionsReproduccion = QHBoxLayout()
        hBoxOpcionsReproduccion.addWidget(opcionsReproduccion)

        hBoxVolumen = QHBoxLayout()
        hBoxVolumen.addWidget(lblVolumen)
        hBoxVolumen.addWidget(self.sldVolumen)


        hBoxFormato = QHBoxLayout()
        hBoxFormato.addWidget(lblFormato)
        hBoxFormato.addWidget(self.cmbFormato)

        hBoxSaidaAudio = QHBoxLayout()
        hBoxSaidaAudio.addWidget(lblSaidaAudio)
        hBoxSaidaAudio.addWidget(cmbSaidaAudio)

        wSaltar = QWidget()
        wSaltar.setLayout(hBoxSaltar)

        wDial = QWidget()
        wDial.setLayout(vBoxDial)

        vBoxPrincipal2 = QVBoxLayout()
        vBoxPrincipal2.addWidget(wDial)
        vBoxPrincipal2.addWidget(wSaltar)

        wPrincipal2 = QWidget()
        wPrincipal2.setLayout(vBoxPrincipal2)


        hBoxPrincipal = QHBoxLayout()
        hBoxPrincipal.addWidget(self.tedCadroTexto)
        hBoxPrincipal.addWidget(wPrincipal2)


        wVolumen = QWidget()
        wVolumen.setLayout(hBoxVolumen)

        wFormato = QWidget()
        wFormato.setLayout(hBoxFormato)

        wSaidaAudio = QWidget()
        wSaidaAudio.setLayout(hBoxSaidaAudio)

        vBoxInferior2 = QVBoxLayout()
        vBoxInferior2.addWidget(wVolumen)
        vBoxInferior2.addWidget(wFormato)
        vBoxInferior2.addWidget(wSaidaAudio)


        wBoxFinal = QWidget()
        wBoxFinal.setLayout(hBoxPrincipal)

        wBoxBotones = QWidget()
        wBoxBotones.setLayout(hBoxBotones)



        wBoxOpcionesReproduccion = QWidget()
        wBoxOpcionesReproduccion.setLayout(hBoxOpcionsReproduccion)

        wBoxInferior2 = QWidget()
        wBoxInferior2.setLayout(vBoxInferior2)

        hBoxInferior = QHBoxLayout()
        hBoxInferior.addWidget(wBoxOpcionesReproduccion)
        hBoxInferior.addWidget(wBoxInferior2)

        wBoxInferior = QWidget()
        wBoxInferior.setLayout(hBoxInferior)


        vBoxFinal = QVBoxLayout()
        vBoxFinal.addWidget(wBoxFinal)
        vBoxFinal.addWidget(wBoxBotones)
        vBoxFinal.addWidget(wBoxInferior)

        widget = QWidget()
        widget.setLayout(vBoxFinal)
        self.setCentralWidget(widget)
        self.show()

#Metodo para imprimir por pantalla la opcion que escoges de el formato
    def on_formatoChanged(self):
        print("formato: " + self.cmbFormato.currentText())

#Metodo para imprimir en la pantalla el Volumen del dial
    def on_sliderChanged(self):
        print("Volumen del dial: " +str(self.dilVolumne.sliderPosition()))

    # Metodo para que cada vez que le demos  a una opcion nos la escriba en el cuadro de texto y si la quitamos que se quite del cuadro de texto
    def on_chkFiltrar_select(self):
        if self.chkFiltrar.isChecked():
            self.tedCadroTexto.append(self.chkFiltrar.text())
        else:
            self.tedCadroTexto.clear()
            if self.chkXML.isChecked():
                self.tedCadroTexto.append(self.chkXML.text())
            if self.chkRepNPL.isChecked():
                self.tedCadroTexto.append(self.chkRepNPL.text())

    def on_chkXML_select(self):
        if self.chkXML.isChecked():
            self.tedCadroTexto.append(self.chkXML.text())
        else:
            self.tedCadroTexto.clear()
            if self.chkFiltrar.isChecked():
                self.tedCadroTexto.append(self.chkFiltrar.text())
            if self.chkRepNPL.isChecked():
                self.tedCadroTexto.append(self.chkRepNPL.text())

    def on_chkRepNPL_select(self):
        if self.chkRepNPL.isChecked():
            self.tedCadroTexto.append(self.chkRepNPL.text())

        else:
            self.tedCadroTexto.clear()
            if self.chkFiltrar.isChecked():
                self.tedCadroTexto.append(self.chkFiltrar.text())
            if self.chkXML.isChecked():
                self.tedCadroTexto.append(self.chkXML.text())



    def on_saltarClicked(self):
        self.sldVolumen.setValue(int(self.cmbSaltar.currentText()))
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()
