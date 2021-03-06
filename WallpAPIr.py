#Hosmax
#https://github.com/HosmaxOfficial
#-----------

import requests
import json
import random
from tkinter import *
from tkinter import filedialog, ttk, Menu
import ctypes



app = Tk()
app.title("WallpAPIr")
app.geometry ("720x480")


langindex = 0
engwlist = ["Anime and Videogames", "Photography"]
espwlist = ["Anime y Videojuegos", "Fotografía"]
apiUrl = ["https://wallhaven.cc/api/v1/search"]
directoryPath = "/"
directorySet = FALSE

datalenwarn = "No pictures found"
qqwarn = "Page not found"
dirwarn = "Select a directory"
combowarn = "Select a category"

def english():
    global datalenwarn
    global qqwarn
    global dirwarn
    global combowarn
#    langindex = 0
    filemenu.entryconfig(1, label = "Quit")
    menubar.entryconfig(1, label = "File")
    menubar.entryconfig(2, label = "Settings")
    settingsmenu.entryconfig(1, label = "Language")
    B2.config(text = "Select folder to save")
    Combo1.set("Select a category")
    Combo1.config(values = engwlist)
    datalenwarn = "No pictures found"
    qqwarn = "Page not found"
    dirwarn = "Select a directory"
    combowarn = "Select a category"

def spanish():
    global datalenwarn
    global qqwarn
    global dirwarn
    global combowarn
#    langindex = 1
    filemenu.entryconfig(1, label = "Salir")
    menubar.entryconfig(1, label = "Archivo")
    menubar.entryconfig(2, label = "Ajustes")
    settingsmenu.entryconfig(1, label = "Idioma")
    B2.config(text = "Elige una carpeta para guardar")
    Combo1.set("Selecciona una categoría")
    Combo1.config(values = espwlist)
    datalenwarn = "No se encontraron resultados"
    qqwarn = "Página no encontrada"
    dirwarn = "Elige una carpeta"
    combowarn = "Selecciona una categoría"

    
def setWallpaper():
    global url
    global directoryPath
    global datalenwarn
    global qqwarn
    global dirwarn
    search = E1.get()
    if directorySet == TRUE:
        L1.pack_forget()
        if Combo1.current() == 0:
            L1.pack_forget()
            defaultSearch = "https://wallhaven.cc/api/v1/search"
            url = defaultSearch + "?q=" + search
            print(url)
            r = requests.get(url)
            status = r.status_code
            if status == 200:
                L1.pack_forget()
                response = r.json()
                print(status)
                lastPage = int(response["meta"]["last_page"])
                url = url + "&page=" + str(random.randint(0,lastPage))
                if len(response["data"]) != 0:
                    L1.pack_forget()
                    imageResponse = response["data"][random.randint(0,(len(response["data"])-1))]["path"]
                    imageRequest = requests.get(imageResponse)
                    filePath = directoryPath + "Wallpaper.jpg"
                    print(filePath)
                    file = open(filePath, "wb")
                    file.write(imageRequest.content)
                    file.close()
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, filePath, 0)

                else:
                    L1.configure(text = datalenwarn)
                    L1.pack()
            else:
                L1.configure(text = qqwarn)
                L1.pack()
        elif Combo1.current() == -1:
            L1.configure(text = combowarn)
            L1.pack()
    else:
        L1.configure(text = dirwarn)
        L1.pack()            

                    


# not working yet
#        elif Combo1.current() == 1:
#            defaultSearch = "https://pixabay.com/api/"
#            url = defaultSearch + "?q=" + search
#            print(url)
#            r = requests.get(url)
#            response = r.json()
#            imageResponse = response["hits"][random.randint(0,(int(response["totalHits"])-1))]["fullHDURL"]
#            imageRequest = requests.get(imageResponse)
#
        

    
def askPath():                                                                                                                  #Ask for the path to the directory where to place the wallpaper before setting it
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

Combo1 = ttk.Combobox(app, state = "readonly", values = engwlist)
Combo1.set("Select a category")
Combo1.pack( padx = 5, pady = 5 )

B2 = Button(app, text = "Select folder to save", command = askPath)
B2.pack( padx = 5, pady = 5 )

B3 = Button(app, text = "WallpAPIr!", command = setWallpaper)
B3.pack( padx = 5, pady = 5 )

L1 = Label(app, text = datalenwarn)
L1.pack( padx = 5, pady = 5 )
L1.pack_forget()

app.config(menu = menubar)
app.mainloop()
