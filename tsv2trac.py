#!/usr/bin/python
from gi.repository import Gtk
import re

class MyWindow:

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file( "main.glade" )
        self.window = builder.get_object( "window1" )
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.show()
        self.textbuffer1 = builder.get_object( "textview1" ).get_buffer()
        self.textbuffer2 = builder.get_object( "textview2" ).get_buffer()

        self.textbuffer1.connect( "changed", self.convert )
        self.textbuffer1.connect( "paste-done", self.convert )

    def convert(self, widget, *args):
        txt = self.textbuffer1
        ( st, en ) = txt.get_bounds()
        self.textbuffer2.set_text( self.to_wiki( txt.get_text( st, en, True ) ) )

    def to_wiki( self, s ):
        o = ""
        for ln in s.split("\n"):
            o += re.sub( "(^|\t|$)", r"\1|| ", ln ) + "\n"
        return o
       

win = MyWindow()
Gtk.main()
