import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from yt_dlp import YoutubeDL


def on_download(btn, entry):
    with YoutubeDL() as ytdl:
        ytdl.download(entry.get_buffer().get_text())


def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)

    mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

    entryBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    label = Gtk.Label(label="Enter link:")
    entry = Gtk.Entry()

    entryBox.set_halign(Gtk.Align.CENTER)
    entryBox.append(label)
    entryBox.append(entry)

    btn = Gtk.Button(label="Download")
    btn.set_halign(Gtk.Align.CENTER)
    btn.connect('clicked', on_download, entry)

    mainBox.set_valign(Gtk.Align.CENTER)
    mainBox.append(entryBox)
    mainBox.append(btn)

    win.set_child(mainBox)
    win.present()


app = Gtk.Application(application_id='com.github.EnderNight.yt_dlp_GUI')
app.connect('activate', on_activate)
app.run(None)
