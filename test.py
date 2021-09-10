import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import numexpr
import pdb

class Handler:
    def __init__(self):
        #self.queue_draw()
        pass

    pdb = lambda self, button: pdb.set_trace()

    def onDestroy(self, *args):
        Gtk.main_quit()

    def changeBar(self, *args):
        text = widthEntry.get_text()
        if text == "":
            bar.set_value(0)
            setStars(0)
        try:
            bar.set_value(float(text))
            setStars(float(text))
        except ValueError: pass

    def calculate(self, *args):
        textbuffer = builder.get_object("calc").get_buffer()
        text = textbuffer.get_text()
        print(text)

        try:
            result = str(int(numexpr.evaluate(text)))
        except:
            textbuffer.set_text("Error")
        else:
            textbuffer.set_text(result, len(result))
            widthEntry.set_text(result)
        calc.set_position(len(result))
        calc.grab_focus_without_selecting()

    '''
    def keyPressEvent(self, widget, event):
        if event.keyval == 106:
            import pdb; pdb.set_trace()
    '''

    def leave(elf, widget, event):
        setStars(float(builder.get_object("widthEntry").get_buffer().get_text()))

    def __getattr__(self, name, *args):
        if name.startswith("star"):
            number=name[4:]
            def onStarPressed(widget, event):
                if event.button == 1:
                    widthEntry.set_text(str(int(number)/2))
            return onStarPressed
        if name.startswith("enter"):
            number=name[5:]
            print(1)
            def onEnter(widget, event):
                setStars(int(number)/2)
            return onEnter
        return lambda *args: print({"name": name, "args": args})

builder = Gtk.Builder()
filename = "test.glade"
#filename = input("filename>")
builder.add_from_file(filename)
builder.connect_signals(Handler())

window = builder.get_object("window1")
button=builder.get_object("buttonid")
popover=builder.get_object("popover")
widthEntry=builder.get_object("widthEntry")
bar=builder.get_object("levelbar")
calc=builder.get_object("calc")

#builder.get_object("box").add(Gtk.Arrow())

#Uncomment to make window draggable
#window.set_titlebar(builder.get_object("headerBar"))

stars = []
for i in range(1,6):
    stars.append(builder.get_object("star" + str(i)))

def setStars(num):
    for i, star in enumerate(stars):
        if num<i+0.5:
            star.set_from_icon_name("non-starred-symbolic", Gtk.IconSize.DIALOG)
        elif num>=i+1:
            star.set_from_icon_name("starred-symbolic", Gtk.IconSize.DIALOG)
        else:
            star.set_from_icon_name("semi-starred-symbolic", Gtk.IconSize.DIALOG)
window.show_all()
calc.grab_focus_without_selecting()
#import pdb; pdb.set_trace()
Gtk.main()


#stars[0].set_from_icon_name("non-starred-symbolic", Gtk.IconSize.BUTTON)