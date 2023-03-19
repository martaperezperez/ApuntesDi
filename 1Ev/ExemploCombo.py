import self as self
from PyQt6.QtWidgets import QBoxLayout, QComboBox, QListWidget, QWidget

    super().__init__()

        self.setWindowTitle("Exemplo QConboBox e QListWidget")

        caixaV= QBoxLayout()

        self.combo = QComboBox()
        self.combo.addItems(["Home", "Muller", "Ambos"])
        self.combo.currentIndexChanged.connect(self.on_combo_currentIndexChanged)
        self.combo.currentTextChanged.connect(self.on_combo_currentTextChanged)
        self.combo.setEditable(True)
        self.combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        caixaV.addWidget(self.combo)

        lista= QListWidget()
        lista.addItem(["Ocupado","Parado","Pensionista"])
        lista.currentItemChanged.connect(self.on_lista_currentItemChanged)
        lista.currentTextChanged.connect(self.on_lista_currentTextChanged)
        caixaV.addWidget(lista)

        contenedor= QWidget()
        contenedor.setLayout(caixaV)

        self.setCentralWidget(contenedor)


        self.show()

    def on_combo_currentIndexChanged(self,indice):

        print(indice)
        print(self.combo.itemText(indice))

    def on_combo_currentTextChanged(self,texto):
        print(texto)

    def on_lista_currentItemChange(self , elemento):
        print(elemento.text())

    def on_lista_currentTextChanged(self,texto):
        print(texto)
