import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class Aplicacion(Gtk.Window):

    def __init__(self):

        super().__init__(title="Exemplo de uso de Gtk.Stack()")

        caixaV = GtK.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        stack=Gtk.Stack()

        combobox = Gtk.ComboBoxText()
        combobox.append_text("Pulsame!!")
        combobox.append_text("Etiqueta")
        combobox.connect("changed", self.on_combo_changed, stack)


        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        botonCheck = Gtk.checkButton(label="Pulsame!!")
        stack.add_titled(botonCheck, "Boton", "Pulsame!!")

        etiqueta =Gtk.Label(label="Una bonita etiqueta")
        stack.add_titled(etiqueta, "Etiqueta","Un bonita etiqueta")

        conmutador = Gtk.StackSwitcher()
        conmutador.set_stack(stack)