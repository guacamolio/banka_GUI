import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class BankomatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bankomāts")
        self.root.attributes('-fullscreen', True)  # Pilnekrāna režīms
        
        self.balance = 1000
        self.pin = "1234"
        
        self.root.bind("<Escape>", self.exit_fullscreen)  # Nospiest Escape, lai izietu no pilnekrāna
        self.set_background()
        self.create_insert_card_screen()
    
    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)  # Atspējot pilnekrāna režīmu
    
    def set_background(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        bg_image = Image.open("bankomats.jpg")
        bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def create_insert_card_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.set_background()
        
        tk.Label(self.root, text="Lūdzu, ievietojiet karti", font=("Arial", 24, "bold"), bg="#FF6600", fg="white").pack(pady=40)
        
        image = Image.open("karte.png")
        image = image.resize((300, 180), Image.LANCZOS)
        self.card_img = ImageTk.PhotoImage(image)
        
        self.card_button = tk.Button(self.root, image=self.card_img, bg="#FF6600", bd=0, command=self.create_pin_screen)
        self.card_button.pack(pady=40)
    
    def create_pin_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.set_background()
        
        tk.Label(self.root, text="Lūdzu, ievadiet PIN", font=("Arial", 24, "bold"), bg="#FF6600", fg="white").pack(pady=40)
        
        self.pin_entry = tk.Entry(self.root, font=("Arial", 20), show="*", justify='center')
        self.pin_entry.pack(pady=20)
        
        tk.Button(self.root, text="Pieslēgties", width=20, height=2, bg="#FFFFFF", fg="black", command=self.check_pin).pack(pady=20)
    
    def check_pin(self):
        if self.pin_entry.get() == self.pin:
            self.create_main_screen()
        else:
            messagebox.showerror("Kļūda", "Nepareizs PIN!")
    
    def create_main_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.set_background()
        
        tk.Label(self.root, text="Lūdzu, norādiet darījumu!", font=("Arial", 24, "bold"), bg="#FF6600", fg="white").pack(pady=40)
        
        button_frame = tk.Frame(self.root, bg="#FF6600")
        button_frame.pack()
        
        btn_style = {"width": 20, "height": 2, "bg": "#FFFFFF", "fg": "black", "font": ("Arial", 16)}
        
        tk.Button(button_frame, text="5 EUR", **btn_style, command=lambda: self.withdraw_fixed(5)).grid(row=0, column=0, padx=20, pady=10)
        tk.Button(button_frame, text="100 EUR", **btn_style, command=lambda: self.withdraw_fixed(100)).grid(row=0, column=1, padx=20, pady=10)
        tk.Button(button_frame, text="10 EUR", **btn_style, command=lambda: self.withdraw_fixed(10)).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(button_frame, text="Cita summa", **btn_style, command=self.withdraw_money).grid(row=1, column=1, padx=20, pady=10)
        tk.Button(button_frame, text="20 EUR", **btn_style, command=lambda: self.withdraw_fixed(20)).grid(row=2, column=0, padx=20, pady=10)
        tk.Button(button_frame, text="Bilance", **btn_style, command=self.check_balance).grid(row=2, column=1, padx=20, pady=10)
        tk.Button(button_frame, text="50 EUR", **btn_style, command=lambda: self.withdraw_fixed(50)).grid(row=3, column=0, padx=20, pady=10)
        tk.Button(button_frame, text="Iemaksāt", **btn_style, command=self.deposit_money).grid(row=3, column=1, padx=20, pady=10)
        
        tk.Button(self.root, text="Izņemt karti", width=25, height=2, font=("Arial", 16), bg="#E74C3C", fg="white", command=self.create_insert_card_screen).pack(pady=40)
    
    def check_balance(self):
        messagebox.showinfo("Konta atlikums", f"Jūsu kontā ir {self.balance} EUR")
    
    def withdraw_money(self):
        messagebox.showinfo("Izņemšana", "Funkcija vēl nav ieviesta.")

    def deposit_money(self):
        messagebox.showinfo("Iemaksa", "Funkcija vēl nav ieviesta.")

    def withdraw_fixed(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            messagebox.showinfo("Izņemšana veiksmīga", f"Jūs izņēmāt {amount} EUR. Jaunais atlikums: {self.balance} EUR")
        else:
            messagebox.showwarning("Kļūda", "Nepietiek līdzekļu!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankomatApp(root)
    root.mainloop()
