# -*- coding; utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import sys, string

def make_box(homogeneous, spacing, expand, fill, padding):
    box = gtk.HBox(homogeneous, spacing)
    button = gtk.Button("box.pack")
    box.pack_start(button, expand, fill, padding)
    button.show()
    if expand == true:
        button = gtk.Button("True,")
