import FindMattes as fm
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog as sd
from os import listdir


root = tk.Tk()
root.withdraw()

sourcePath = filedialog.askdirectory(parent = root, initialdir = "/", title = "Please select a diectory")
matteHeight = sd.askinteger("Set the Mattes Size:", "Output matte vertical resolution(256 for quick test)?", parent = root, initialvalue = 256)
files = listdir(sourcePath)
for file in files:
    sourceFile = sourcePath + "/" + file
    main_extension  = file.find('.')
    mattesName = file[:main_extension] + "_rotoMattes" + file[main_extension:]
    mattesPath = sourcePath + "/" + mattesName
    fm.createMatte(sourceFile, mattesPath, matteHeight)




