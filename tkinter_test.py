from tkinter import *
from tkinter.colorchooser import askcolor
import os
os.system('cls')


def rgb_to_color(rgb):
    r, g, b = rgb  # translates an rgb tuple of int to a tkinter friendly color code
    return f'#{r:02x}{g:02x}{b:02x}'


window = Tk()
window.geometry("600x600")
window.title("My First Tkinter Test")

icon = PhotoImage(file='dice.png')
window.iconphoto(True, icon)
clr = askcolor(color=None)
window.config(background=clr[1])
# window.config(background=rgb_to_color((255, 0, 255)))
window.mainloop()
