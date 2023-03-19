import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Exame(Gtk.Window):
    def __init__(self):

        builder = Gtk.Builder()
        builder.add_from_file("RecuperacionDI")


        Gtk.Window.__init__(self, title="Exame 15-04-2023")
        self.set_border_width(10)

        self.box1 = builder.get_object("box1")
        self.frame1 = builder.get_object("frame1")
        self.box2 = builder.get_object("box2")
        self.box3 = builder.get_object("box3")
        self.label1 = builder.get_object("label1")
        self.combobox1 = builder.get_object("combobox1")
        self.box4 = builder.get_object("box4")
        self.label2 = builder.get_object("label2")
        self.entry1 = builder.get_object("entry1")


        frmPerfis = Gtk.Frame(label="Perfís usuario")

        trvPerfis = Gtk.TreeView()

        caixaVBotons = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing = 2)

        btnNovo = Gtk.Button (label = "Novo")
        btnEditar =Gtk.Button (label = "Editar")
        btnBorrar = Gtk.Button (label = "Borrar")


        lblNomePerfil = Gtk.Label (label="Nome perfíl")
        txtNomePerfil = Gtk.Entry()
        lblDescripcionPerfil = Gtk.Label(label= "Descripción")
        txtDescripcionPerfil = Gtk.Entry()
        lblPermisos = Gtk.Label (label = "Permisos")
        cmbPermisos = Gtk.ComboBox()



        self.connect("delete-event", Gtk.main_quit)
        self.show_all()




if __name__=="__main__":

    Exame()
    Gtk.main()