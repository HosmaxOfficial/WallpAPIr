#Hosmax
#https://github.com/HosmaxOfficial
#-----------

#Import libraries
import requests
import json
import random
from tkinter import *
from tkinter import filedialog, ttk, Menu
import ctypes


#Start
app = Tk()
app.title("WallpAPIr")



#Variables
engvlist = ["Anime and Videogames", "Photography"]
espvlist = ["Anime y Videojuegos", "Fotografía"]
apiUrl = ["https://wallhaven.cc/api/v1/search"]
directoryPath = "/"
directorySet = FALSE

#Functions
def test():
    t = 0

def spanish():
    filemenu.entryconfig(1, label = "Salir")
    menubar.entryconfig(1, label = "Archivo")
    menubar.entryconfig(2, label = "Ajustes")
    settingsmenu.entryconfig(1, label = "Idioma")
    B2.config(text = "Elige una carpeta para guardar")
    Combo1.set("Selecciona una categoría")

def english():
    filemenu.entryconfig(1, label = "Quit")
    menubar.entryconfig(1, label = "File")
    menubar.entryconfig(2, label = "Settings")
    settingsmenu.entryconfig(1, label = "Language")
    B2.config(text = "Select folder to save")
    Combo1.set("Select a category")
    
def setWallpaper():
    if directorySet == TRUE:
        defaulSearch = "https://wallhaven.cc/api/v1/search"
        search = E1.get()
        global url
        global directoryPath
        url = defaulSearch + "?q=" + search
        print(url)
        r = requests.get(url)
        response = r.json()
        lastPage = int(response["meta"]["last_page"])
        url = url + "&page=" + str(random.randint(0,lastPage))
        imageResponse = response["data"][random.randint(0,(len(response["data"])-1))]["path"]
        imageRequest = requests.get(imageResponse)
        filePath = directoryPath + "Wallpaper.jpg"
        print(filePath)
        file = open(filePath, "wb")
        file.write(imageRequest.content)
        file.close()
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filePath, 0)
    
def askPath():                                                                                                                  #Ask the path to the directory where to place the wallpaper before setting it
    global directoryPath
    global directorySet
    directoryPath = filedialog.askdirectory(initialdir = "/", title = "Examine")
    directorySet = TRUE
    print(directoryPath)


menubar = Menu(app)                                                                                                             #Menu
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Quit", command = quit)
menubar.add_cascade(label = "File", menu = filemenu)

settingsmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Settings", menu = settingsmenu)

langmenu = Menu(settingsmenu, tearoff = 0)
langmenu.add_command(label = "Español", command = spanish)
langmenu.add_command(label = "English", command = english)
settingsmenu.add_cascade(label = "Language", menu = langmenu)


E1 = Entry(app)                                                                                                                 #Entry to search
E1.pack( padx = 5, pady = 5 )

Combo1 = ttk.Combobox(app, state = "readonly", values = vlist)
Combo1.set("Select a category")
Combo1.pack( padx = 5, pady = 5 )

B2 = Button(app, text = "Select folder to save", command = askPath)
B2.pack( padx = 5, pady = 5 )

B3 = Button(app, text = "WallpAPIr!", command = setWallpaper)
B3.pack( padx = 5, pady = 5 )


app.config(menu = menubar)
app.mainloop()
