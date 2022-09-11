from tkinter import *
from tkinter import ttk
import helpers

def startSplash_Screen():
    # Configuración de la Splash-Screen
    splash_root = Tk()
    splash_root.title("")
    splash_root.config(
        borderwidth=1,
        relief = "solid"
    )
    # Imagen de fondo
    logo = PhotoImage(file=helpers.getImgPath('tie_break_alt_70.png'))
    label = Label(
        splash_root,
        image=logo
    )
    label.pack(side='top', fill=BOTH, expand=1)

    def progress():
        if progressbar['value'] < 100:
            progressbar.step(1.1)
            splash_root.after(50, progress)

    progressbar = ttk.Progressbar(splash_root, mode="determinate", maximum=100, orient=HORIZONTAL)
    progressbar.pack(side='bottom', fill=X, expand=1)
    progressbar.update()  # para actualizar el height de la progressbar ya construida

    # Dimensiones y centrado
    # splash_root.geometry(helpers.getGeometry(splash_root,778,781+progressbar.winfo_height()))
    splash_root.geometry(helpers.getGeometry(splash_root,545,548+progressbar.winfo_height()))
    # Quitamos la barra superior de la ventana
    splash_root.overrideredirect(True)

    # Función para ocultar la splash screen y empezar el IDE
    def hide_splash_screen():
        splash_root.destroy()

    splash_root.after(5000, hide_splash_screen)
    progress()
    splash_root.mainloop()