#Hosmax
#https://github.com/HosmaxOfficial
#-----------

import requests
import json
import random
from tkinter import *
from tkinter import filedialog
import ctypes

app = Tk()

url = ""

def searchImage():
    defaulSearch = "https://wallhaven.cc/api/v1/search"
    search = E1.get()
    global url
    url = defaulSearch + "?q=" + search
    print(url)

def setWallpaper():
    global url
    global directoryPath
    r = requests.get(url)
    response = r.json()
    lastPage = int(response["meta"]["last_page"])
    url = url + "&page=" + str(random.randint(0,lastPage))
    imageResponse = response["data"][random.randint(0,len(response["data"]))]["path"]
    imageRequest = requests.get(imageResponse)
    filePath = directoryPath + "Wallpaper.jpg"
    print(filePath)
    file = open(filePath, "wb")
    file.write(imageRequest.content)
    file.close()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filePath, 0)
    
def askPath():
    global directoryPath
    directoryPath = filedialog.askdirectory(initialdir = "/", title = "Examine")
    print(directoryPath)

E1 = Entry(app)
E1.pack( padx = 5, pady = 5 )


B1 = Button(app, text = "Search", command = searchImage)
B1.pack( padx = 5, pady = 5 )

B2 = Button(app, text = "Select folder to save", command = askPath)
B2.pack( padx = 5, pady = 5 )

B3 = Button(app, text = "Submit", command = setWallpaper)
B3.pack( padx = 5, pady = 5 )


app.mainloop()
