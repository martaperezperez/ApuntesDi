import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class GladeMarta:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("listatarefaTreeView.glade")


        wndfiestraPrincipal = builder.get_object("GtkWindow")
        self.tvwTarefas = builder.get_object("tvwTarefas")
        self.tvcTarefas = builder.get_object("tvcTarefa")
        self.tvcFeito = builder.get_object("tvcFeito")
        self.txtTarefa = builder.get_object("txtTarefa")
        self.btnEngadir = builder.get_object("btnEngadir")
        self.btnModificar = builder.get_object("btnModificar")
        self.btnBorrar = builder.get_object("bnBorrar")