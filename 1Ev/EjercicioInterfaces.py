import sys


from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class EjercicioInterfaces(QMainWindow):
    def __int__(self):
        super().__init__()

        boton1 = QPushButton("Ocultar >>")
        boton1.clicked.connect(self.on_button_clicked)
        self.setCentralWidget(boton1)
        self.show()
       

    def on_button_clicked(self):
        print("O boton foi pulsado")


applicacion = QApplication(sys.argv)
fiestra = EjercicioInterfaces()
applicacion.exec()