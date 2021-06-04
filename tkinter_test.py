# https://youtu.be/XKHEtdqhLK8?t=22035
# https://www.youtube.com/watch?v=ji8pTynQhEo

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

window.config(background='yellow')
# window.config(background='#564c9e')
# window.config(background=rgb_to_color((255, 0, 255)))
# Color Picker    https://www.w3schools.com/colors/colors_picker.asp
# Color Mixer     https://www.w3schools.com/colors/colors_mixer.asp

# clr = askcolor(color=None)
# window.config(background=clr[1])


window2 = Tk()
window2.geometry("300x300")
window2.title("Small Window")

# icon = PhotoImage(file='dice.png')
# window2.iconphoto(False, icon)

window2.config(background='green')

window.mainloop()
