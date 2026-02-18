import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# 1. සුපර්ස්ටාර් දත්ත (Dictionary)
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

# 2. පින්තූරය ක්ලික් කරාම ඕපන් වෙන අලුත් පේජ් එක (Detail Window)
def show_details(name):
    # අලුත් Window එකක් සාදා ගැනීම
    detail_window = tk.Toplevel(root)
    detail_window.title(f"{name} - Superstar Details")
    detail_window.geometry("500x650")
    detail_window.configure(bg="#1a1a1a") # Dark Theme background

    # ලොකු පින්තූරය පෙන්වීම
    try:
        img_path = f"{name.lower().replace(' ', '_')}.jpg"
        full_img = Image.open(img_path)
        # පින්තූරය ලොකුවට resize කිරීම (300x300)
        full_img = full_img.resize((350, 350), Image.LANCZOS) 
        photo = ImageTk.PhotoImage(full_img)
        
        img_label = tk.Label(detail_window, image=photo, bg="#1a1a1a")
        img_label.image = photo 
        img_label.pack(pady=30)
    except:
        tk.Label(detail_window, text="Image Not Found", fg="red", bg="#1a1a1a", font=("Arial", 14)).pack(pady=30)

    # සුපර්ස්ටාර්ගේ නම
    tk.Label(detail_window, text=name, font=("Impact", 28), fg="#e74c3c", bg="#1a1a1a").pack(pady=10)

    # විස්තර පෙන්වීම
    tk.Label(detail_window, text=superstars[name], font=("Arial", 14), fg="white", bg="#1a1a1a", justify="center").pack(pady=20, padx=20)

    # ආපහු යාමට Button එකක්
    tk.Button(detail_window, text="Back to Gallery", command=detail_window.destroy, bg="#34495e", fg="white", font=("Arial", 10, "bold"), width=20).pack(pady=20)

# 3. ප්‍රධාන Window එක සැකසීම
root = tk.Tk()
root.title("WWE Superstars Gallery")
root.geometry("900x700")
root.configure(bg="#2c3e50")

# Title එකක් දාමු
main_title = tk.Label(root, text="WWE SUPERSTARS ROSTER", font=("Impact", 30), fg="white", bg="#2c3e50", pady=20)
main_title.grid(row=0, column=0, columnspan=5)

# 4. Grid එක සඳහා Cards සෑදීම
row, col = 1, 0

for name in superstars:
    # Card එකක් විදිහට Frame එකක් සෑදීම
    card = tk.Frame(root, bd=2, relief="flat", padx=10, pady=10, bg="#34495e")
    card.grid(row=row, column=col, padx=15, pady=15)
    
    try:
        # Gallery එකේ පෙන්වන කුඩා පින්තූරය (120x120)
        img_name = f"{name.lower().replace(' ', '_')}.jpg"
        img = Image.open(img_name)
        img = img.resize((120, 120), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        # පින්තූරය Button එකක් ලෙස
        btn = tk.Button(card, image=photo, command=lambda n=name: show_details(n), borderwidth=0, cursor="hand2")
        btn.image = photo 
        btn.pack()
    except:
        tk.Button(card, text="No Image", width=15, height=7, command=lambda n=name: show_details(n)).pack()

    # නම ලේබල් එකක් ලෙස
    tk.Label(card, text=name, font=("Arial", 11, "bold"), fg="white", bg="#34495e").pack(pady=5)
    
    col += 1
    if col > 4: # පේළියකට 5 බැගින්
        col = 0
        row += 1

root.mainloop()