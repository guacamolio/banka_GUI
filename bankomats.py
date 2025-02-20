import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class BankomatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bankomāts")
        self.root.attributes('-fullscreen', True)  
        
        self.balance = 1000
        self.pin = "1234"
        
        self.root.bind("<Escape>", self.exit_fullscreen) 
        self.kartes_ievietosanas_ekrans()
    
    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False) 
    
    def set_background(self):
        self.root.configure(bg="#FF6600")
    
    def kartes_ievietosanas_ekrans(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.set_background()
        
        tk.Label(self.root, text="Lūdzu, ievietojiet karti", font=("Arial", 24, "bold"), bg="#FF6600", fg="black").pack(pady=40)
        
        image = Image.open("karte.png")
        image = image.resize((600, 340))
        self.card_img = ImageTk.PhotoImage(image)
        
        self.card_button = tk.Button(self.root, image=self.card_img, bg="#FF6600", bd=0, command=self.pin_screen)
        self.card_button.pack(pady=40)
    
    def pin_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
        self.set_background()

        frame = tk.Frame(self.root, bg="#FF6600")
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(0, weight=1)  
        frame.columnconfigure(1, weight=1) 
        frame.columnconfigure(2, weight=1) 

        tk.Label(frame, text="Lūdzu, ievadiet PIN kodu", font=("Arial", 74, "bold"), bg="#FF6600", fg="black").grid(row=0, column=0, columnspan=3, padx=120, pady=60, sticky="w")

        tk.Label(frame, text="Piesedziet PIN kodu", font=("Arial", 36), bg="#FF6600", fg="black").grid(row=3, column=0, padx=280, pady=10, sticky="w")

        img = Image.open("pasleptpinclear.png")
        img = img.resize((600, 450)) 
        self.pin_image = ImageTk.PhotoImage(img)
        tk.Label(frame, image=self.pin_image, bg="#FF6600").grid(row=4, column=0, padx=200, pady=10, sticky="w")

        self.pin_entry = tk.Entry(frame, font=("Arial", 40), width=16, show="*", justify='center')
        self.pin_entry.grid(row=4, column=3, padx=20, pady=80, sticky="e", ipady=15) 

        btn_style = {"width": 12, "height": 1, "bg": "white", "fg": "black", "font": ("Arial", 40)}
        tk.Button(frame, text="Pieslēgties", **btn_style, command=self.parbaudit_pin).grid(row=5, column=3, padx=20, pady=20, sticky="w")

        tk.Button(frame, text="Atcelt", **btn_style, command=self.kartes_ievietosanas_ekrans).grid(row=10, column=0, padx=40, pady=20, sticky="w")

    def parbaudit_pin(self):
        if self.pin_entry.get() == self.pin:
            self.galvenais_screen()
        else:
            messagebox.showerror("Kļūda", "Nepareizs PIN!")
    
    def galvenais_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.set_background()

        frame = tk.Frame(self.root, bg="#FF6600")
        frame.pack(fill="both", expand=True)

        frame.columnconfigure(0, weight=1)  
        frame.columnconfigure(1, weight=2)  
        frame.columnconfigure(2, weight=1)  

        tk.Label(frame, text="Lūdzu, norādiet darījumu!", font=("Arial", 48, "bold"), bg="#FF6600", fg="black").grid(
            row=0, column=0, columnspan=3, pady=50, padx=60
        )

        btn_style = {"width": 12, "height": 1, "bg": "white", "fg": "black", "font": ("Arial", 65)}

        tk.Button(frame, text="Atdot karti", **btn_style, command=self.kartes_ievietosanas_ekrans).grid(
           row=2, column=0, padx=40, pady=20, sticky="w"
        )
        tk.Button(frame, text="Mainīt PIN kodu", **btn_style, command=self.pinkod_maina).grid(
            row=1, column=0, padx=40, pady=20, sticky="w"
        )

        tk.Button(frame, text="Naudas izmaksa", **btn_style, command=self.naudas_izmaksa).grid(
            row=1, column=2, padx=40, pady=20, sticky="e"
        )
        tk.Button(frame, text="Atlikums kontā", **btn_style, command=self.atlikums_konta).grid(
            row=2, column=2, padx=40, pady=20, sticky="e"
        )

    
    def pinkod_maina(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.set_background()
    
        frame = tk.Frame(self.root, bg="#FF6600")
        frame.pack(fill="both", expand=True)
        
        tk.Label(frame, text="Ievadiet esošo PIN kodu:", font=("Arial", 28), bg="#FF6600", fg="black").pack(pady=20)
        self.old_pin_entry = tk.Entry(frame, font=("Arial", 28), width=10, show="*", justify='center')
        self.old_pin_entry.pack(pady=10)
        
        tk.Label(frame, text="Ievadiet jauno PIN kodu:", font=("Arial", 28), bg="#FF6600", fg="black").pack(pady=20)
        self.new_pin_entry = tk.Entry(frame, font=("Arial", 28), width=10, show="*", justify='center')
        self.new_pin_entry.pack(pady=10)
        
        tk.Label(frame, text="Vēlreiz ievadiet jauno PIN kodu:", font=("Arial", 28), bg="#FF6600", fg="black").pack(pady=20)
        self.confirm_pin_entry = tk.Entry(frame, font=("Arial", 28), width=10, show="*", justify='center')
        self.confirm_pin_entry.pack(pady=10)
        
        btn_style = {"width": 12, "height": 1, "bg": "white", "fg": "black", "font": ("Arial", 28)}
        tk.Button(frame, text="Labot", **btn_style, command=self.update_pin).pack(pady=20)
        tk.Button(frame, text="Atcelt", **btn_style, command=self.galvenais_screen).pack(pady=10)
    
    def update_pin(self):
        old_pin = self.old_pin_entry.get()
        new_pin = self.new_pin_entry.get()
        confirm_pin = self.confirm_pin_entry.get()
        
        if old_pin != self.pin:
            messagebox.showerror("Kļūda", "Nepareizs esošais PIN!")
            return
        
        if new_pin != confirm_pin:
            messagebox.showerror("Kļūda", "Jaunais PIN nesakrīt!")
            return
        
        if not new_pin.isdigit() or len(new_pin) != 4:
            messagebox.showerror("Kļūda", "PIN jābūt 4 ciparu skaitlim!")
            return
        
        self.pin = new_pin
        messagebox.showinfo("PIN izmainīts", "Jūsu PIN kods veiksmīgi nomainīts!")
        self.galvenais_screen()

    
    def atlikums_konta(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.set_background()
        
        frame = tk.Frame(self.root, bg="#FF6600")
        frame.pack(fill="both", expand=True)
        
        self.balance =   self.balance
        self.reserved = 0
        self.available_balance = self.balance - self.reserved
        
        tk.Label(frame, text=f"Atlikums kontā: {self.balance:.2f} EUR", font=("Arial", 28), bg="#FF6600", fg="black").pack(pady=20)
        tk.Label(frame, text=f"Rezervēts: {self.reserved:.2f} EUR", font=("Arial", 28), bg="#FF6600", fg="black").pack(pady=10)
        tk.Label(frame, text=f"Pieejamais atlikums: {self.available_balance:.2f} EUR", font=("Arial", 28), bg="#FF6600", fg="black").pack(pady=10)
        
        btn_style = {"width": 12, "height": 1, "bg": "white", "fg": "black", "font": ("Arial", 28)}
        tk.Button(frame, text="Atpakaļ", **btn_style, command=self.galvenais_screen).pack(pady=20)
    
    
    def naudas_izmaksa(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.set_background()
        
        tk.Label(self.root, text="Lūdzu, norādiet darījumu!", font=("Arial", 24, "bold"), bg="#FF6600", fg="black").pack(pady=40)
        
        button_frame = tk.Frame(self.root, bg="#FF6600")
        button_frame.pack()
        
        btn_style = {"width": 20, "height": 2, "bg": "white", "fg": "black", "font": ("Arial", 16)}
        
        tk.Button(button_frame, text="5 EUR", **btn_style, command=lambda: self.withdraw(5)).grid(row=0, column=0, padx=20, pady=10)
        tk.Button(button_frame, text="100 EUR", **btn_style, command=lambda: self.withdraw(100)).grid(row=0, column=1, padx=20, pady=10)
        tk.Button(button_frame, text="10 EUR", **btn_style, command=lambda: self.withdraw(10)).grid(row=1, column=0, padx=20, pady=10)
        tk.Button(button_frame, text="Cita summa", **btn_style, command=self.withdraw_cita_summa).grid(row=1, column=1, padx=20, pady=10)
        tk.Button(button_frame, text="20 EUR", **btn_style, command=lambda: self.withdraw(20)).grid(row=2, column=0, padx=20, pady=10)
        tk.Button(button_frame, text="Bilance", **btn_style, command=self.parbaudit_bil).grid(row=2, column=1, padx=20, pady=10)
        
        tk.Button(self.root, text="Izņemt karti", width=25, height=2, font=("Arial", 16), bg="#E74C3C", fg="white", command=self.kartes_ievietosanas_ekrans).pack(pady=40)
    
    def parbaudit_bil(self):
        messagebox.showinfo("Konta atlikums", f"Jūsu kontā ir {self.balance} EUR")

    

    def withdraw_cita_summa(self):
        summa_logs = tk.Toplevel(self.root)
        summa_logs.title("Izņemt citu summu")
        summa_logs.geometry("500x300") 

        tk.Label(summa_logs, text="Ievadiet summu:", font=("Arial", 20)).pack(pady=20)

        self.summa_izmaksai = tk.Entry(summa_logs, font=("Arial", 20), width=10, justify="center")
        self.summa_izmaksai.pack(pady=10)

        tk.Button(
            summa_logs, text="Izņemt", font=("Arial", 18), bg="white", fg="black",
            command=self.izmaksat_naudu
        ).pack(pady=20)

    def izmaksat_naudu(self):
        try:
            summa = int(self.summa_izmaksai.get())  
            if summa > self.balance:
                messagebox.showwarning("Kļūda", "Nepietiek līdzekļu!")
            else:
                self.balance -= summa
                messagebox.showinfo("Izņemšana veiksmīga", f"Jūs izņēmāt {summa} EUR.\nJaunais atlikums: {self.balance} EUR")
        except ValueError:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu skaitli!")
            
    def withdraw(self, amount):
        if amount > self.balance:
            messagebox.showwarning("Kļūda", "Nepietiek līdzekļu!")
        else:
            self.balance -= amount
            messagebox.showinfo("Izņemšana veiksmīga", f"Jūs izņēmāt {amount} EUR.\nJaunais atlikums: {self.balance} EUR")


if __name__ == "__main__":
    root = tk.Tk()
    app = BankomatApp(root)
    root.mainloop()
