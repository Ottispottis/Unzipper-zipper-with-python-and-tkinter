# zipper/unzipper made by Otto Heldt

import tkinter as tk
import zipfile
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os

root = tk.Tk()

canvas = tk.Canvas(root, width=350, height=400)
canvas.grid(columnspan=4, rowspan=4)

instructions = tk.Label(root, text="Select a file B)", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# Placing logo to tkinter window

logo = Image.open("cool.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


def zip_file():
    file = askopenfile(parent=root, mode="rb", filetype=[("Zip file", "*.zip")])
    if file:
        unzipping = zipfile.ZipFile(file)
        unzipping.extractall("S:\pythonstuff") # Location where the files will be unzipped, change this to any directory you like
        unzipping.close()
        text = "File extracted"


        textbox = tk.Text(root, height=2, width=11, padx=15, pady=10, font="Raleway")
        textbox.insert(1.0, text)
        textbox.grid(column=1, row=4)


def unzip_file():
    file2 = askopenfile(parent=root, mode="rb")
    name = os.path.basename(file2.name)
    print(name)
    name = name + ".zip"
    if file2:
        zipping = zipfile.ZipFile(name, 'w')
        zipping.write(file2.name)
        zipping.close()
        text2 = "File zipped"
        
        textbox2 = tk.Text(root, height=2, width=11, padx=15, pady=10, font="Raleway")
        textbox2.insert(1.0, text2)
        textbox2.grid(column=1,row=4)


# creating buttons for zipping and unzipping


unzip_str = tk.StringVar()
unzip_btn = tk.Button(root, textvariable=unzip_str, command=lambda:zip_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=30)
unzip_str.set("Unzip a file B)")
unzip_btn.grid(column=1, row=2)

zip_str = tk.StringVar()
zip_btn = tk.Button(root, textvariable=zip_str, command=lambda:unzip_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=30)
zip_str.set("Zip a file B)")
zip_btn.grid(column=1, row=3)

root.mainloop()

