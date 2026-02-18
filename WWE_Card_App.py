import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

superstars = {
    "John Cena": "17-times World Champion\nFinisher : AA(Attitude Adjustment)",
    "Randy Orton": "The Viper\nFinisher : RKO",
    "Drew McIntyre": "The Scottish Warrior\nFinisher : Claymore",
    "Brock Lesnar": "The Beast\nFinisher : F5",
    "Roman Reigns": "Tribal Chief(OTC)\nFinisher : Spear",
    "Seth Rollins": "The Visionary\nFinisher : Stomp",
    "Jon Moxley": "The Lunatic Fringe\nFinisher : Crab Stomp",
    "Rey Mysterio": "The Lucha King\nFinisher : 619",
    "AJ Styles": "The Phenominal 1\nFinisher : Fourarm",
    "CM Punk": "Best In The World\nFinisher : GTS"
}

def show_details(name):
    messagebox.showinfo(name, superstars[name])

root = tk.Tk()
root.title("WWE Superstars Gallery")
root.geometry("800x600")

row, col = 0, 0

for name in superstars:
    
    card = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
    card.grid(row=row, column=col, padx=10, pady=10)
    
    try:
        img_path = f"{name.lower().replace(' ', '_')}.jpg"
        img = Image.open(img_path)
        img = img.resize((100, 100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        img_btn = tk.Button(card, image=photo, command=lambda n=name: show_details(n))
        img_btn.image = photo 
        img_btn.pack()
    except:
        tk.Button(card, text="No Image", width=12, height=6, command=lambda n=name: show_details(n)).pack()

    tk.Label(card, text=name, font=("Arial", 10, "bold")).pack()
    
    col += 1
    if col > 4:
        col = 0
        row += 1

root.mainloop()