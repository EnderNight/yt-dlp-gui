from yt_dlp import YoutubeDL
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


def on_download(btn, entry, video, audio):

    ydl_ops = {
        'format': 'best'
    }
    if video.get_active() and audio.get_active():
        ydl_ops['format'] = 'bestvideo+bestaudio/best'
        print("downloading best audio and best video")
    else:
        if video.get_active():
            ydl_ops['format'] = 'bestvideo'
            print("downloading best video only")
        if audio.get_active():
            ydl_ops['format'] = 'bestaudio'
            print("downloading best audio only")

    with YoutubeDL(ydl_ops) as ytdl:
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

    optionsBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    video = Gtk.CheckButton(label="Video")
    audio = Gtk.CheckButton(label="Audio")

    optionsBox.set_halign(Gtk.Align.CENTER)
    optionsBox.append(video)
    optionsBox.append(audio)

    btn = Gtk.Button(label="Download")
    btn.set_halign(Gtk.Align.CENTER)
    btn.connect('clicked', on_download, entry, video, audio)

    mainBox.set_valign(Gtk.Align.CENTER)
    mainBox.append(entryBox)
    mainBox.append(optionsBox)
    mainBox.append(btn)

    win.set_child(mainBox)
    win.present()


def runApp():
    app = Gtk.Application(application_id='com.github.EnderNight.yt_dlp_GUI')
    app.connect('activate', on_activate)
    app.run(None)
