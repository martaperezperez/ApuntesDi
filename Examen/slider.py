import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Ejemplo de Gtk.Scale")
        self.set_default_size(400, 300)
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1)
        scale.connect("value-changed", self.on_scale_changed)
        vbox.pack_start(scale, True, True, 0)

        self.label = Gtk.Label()
        vbox.pack_start(self.label, False, False, 0)

    def on_scale_changed(self, scale):
        value = scale.get_value()
        self.label.set_text("Posición: {}".format(value))

if __name__ == '__main__':
    window = MainWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
