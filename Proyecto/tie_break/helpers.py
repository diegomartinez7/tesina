from pathlib import Path
from tkinter import *

def getImgPath(fileName):
    base_path = Path(__file__).parent
    file_path = (base_path / "../tie_break/resources/img" / fileName).resolve()
    return file_path

def getAudioPath(fileName):
    base_path = Path(__file__).parent
    file_path = (base_path / "../tie_break/resources/audio" / fileName).resolve()
    return file_path

def getFilePath(fileName):
    base_path = Path(__file__).parent
    file_path = (base_path / "../tie_break/resources/config" / fileName).resolve()
    return file_path

# Función para centrar un widget en pantalla
def getGeometry(widget, width, height):
    screenWidth = widget.winfo_screenwidth()
    screenHeight = widget.winfo_screenheight()
    x = (screenWidth / 2) - (width / 2)
    y = (screenHeight / 2) - (height / 2)
    geometry = '%dx%d+%d+%d' % (width, height, x, y)
    return geometry