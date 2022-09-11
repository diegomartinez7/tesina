from tkinter import *
from tkinter import font as tkfont
from tkinter import ttk
import helpers
import splashscreen

# ----------------------------------------------------------------------------------------------------#
#                                            APLICACIÓN                                               #
# ----------------------------------------------------------------------------------------------------#

def start():
    # ----------------------------------------------------------------------------------------------------#
    #                                        DEFINICIÓN DE ROOT                                           #
    # ----------------------------------------------------------------------------------------------------#

    # Configuracion de la raíz
    # rootWidth = 800
    # rootHeight = 650
    root = Tk()
    # root.geometry(helpers.getGeometry(root,root.winfo_screenwidth(),root.winfo_screenheight()))
    root.state("zoom")
    root.title("Tie-Break")
    root.minsize(height=460, width=620)
    # root.iconbitmap(helpers.getImgPath('.ico'))
    # root['background'] = theme["color1"]
    root['background'] = '#1f1137'


    root.mainloop()

splashscreen.startSplash_Screen()
start()