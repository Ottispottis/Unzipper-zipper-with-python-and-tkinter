import tkinter as tk
import zipfile
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import os

root = tk.Tk()

canvas = tk.Canvas(root, width=350, height=400)
canvas.grid(columnspan=4, rowspan=4)

# Instructions

instructions = tk.Label(root, text="Select a file B)", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

logo = Image.open("cool.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

def zip_file():
    file = askopenfile(parent=root, mode="rb", filetype=[("Zip file", "*.zip")])
    if file:
        unzipping = zipfile.ZipFile(file)
        unzipping.extractall("S:\pythonstuff")
        unzipping.close()
        text = "File extracted"

        # Textbox
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

# Browse

browse_str = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_str, command=lambda:zip_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=30)
browse_str.set("Unzip a file B)")
browse_btn.grid(column=1, row=2)

zip_str = tk.StringVar()
zip_btn = tk.Button(root, textvariable=zip_str, command=lambda:unzip_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=30)
zip_str.set("Zip a file B)")
zip_btn.grid(column=1, row=3)

root.mainloop()
