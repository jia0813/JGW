import tkinter as tk
from tkinter import simpledialog

class WeaponApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#404B6B")

        # Page data
        self.weapon_data = [
            ("GLOK", "PISTOL", "HITAM"),
            ("AWP", "SNIPER", "PINK"),
            ("KARAMBIT", "PISAU", "PUTIH"),
            ("RUDAL", "BASOKA", "KUNING"),
            ("KARABIN", "SENAPAN", "HIJAU")
        ]
        self.weapon_types = ["PISTOL", "SNIPER", "PISAU", "BASOKA", "SENAPAN"]
        self.weapon_colors = ["HITAM", "PINK", "PUTIH", "KUNING", "HIJAU"]
        self.weapon_names = ["GLOK", "AWP", "KARAMBIT", "RUDAL", "KARABIN"]

        self.selected_weapon = None
        self.selected_color = None
        self.selected_name = None 

        # Start with page 1
        self.page_1()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def page_1(self):
        self.clear_widgets()
        tk.Label(self.root, text="Selamat datang di Dunia JGW!", font=("ThaleahFat", 70), bg="#404B6B", fg="white").pack(pady=200)
        tk.Button(self.root, text="Mulai", command=self.page_2, bg="#FEAE35", font=("ThaleahFat", 50)).pack(pady=20)

    def page_2(self):
        self.clear_widgets()
        tk.Label(self.root, text="Ayo bertarung! Pilih senjatamu!", font=("ThaleahFat", 70), bg="#404B6B", fg="white").pack(pady=150)
        tk.Button(self.root, text="Data Senjata", command=self.page_3, bg="#FEAE35", font=("ThaleahFat", 50)).pack(pady=20)
        tk.Button(self.root, text="Buat Senjata", command=self.page_5, bg="#FEAE35", font=("ThaleahFat", 50)).pack(pady=20)

    def page_3(self):
        self.clear_widgets()
        tk.Label(self.root, text="Data Senjata", font=("ThaleahFat", 50), bg="#404B6B", fg="white").pack(pady=40)

        for i, (namea, weapon, color) in enumerate(self.weapon_data, start=1):
            frame = tk.Frame(self.root, bg="#404B6B")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{i}: {namea} {weapon}; {color}", font=("ThaleahFat", 15), bg="#404B6B", fg="white").pack(side="left", padx=10)
            tk.Button(frame, text="Pilih", command=lambda n=namea, w=weapon, c=color: self.page_4(n, w, c), bg="#FEAE35", font=("ThaleahFat", 15)).pack(side="left", padx=10)
            tk.Button(frame, text="Hapus", command=lambda i=i-1: self.delete_weapon(i), bg="#FEAE35", font=("ThaleahFat", 15)).pack(side="left", padx=10)

        tk.Button(self.root, text="Kembali", command=self.page_2, bg="#FEAE35", font=("ThaleahFat", 30)).pack(pady=20)

    def page_4(self, namea, weapon, color):
        self.clear_widgets()
        tk.Label(self.root, text=f"Anda telah membuat", font=("ThaleahFat", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self.root, text=f"Nama: {namea}", font=("ThaleahFat", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self.root, text=f"Jenis: {weapon}", font=("ThaleahFat", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self.root, text=f"Warna: {color}", font=("ThaleahFat", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self.root, text=f"Selamat bertarung!", font=("ThaleahFat", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Button(self.root, text="Buat Senjata Lagi", command=self.page_2, bg="#FEAE35", font=("ThaleahFat", 30)).pack(pady=10)
        tk.Button(self.root, text="Simpan dan Tutup", command=self.root.quit, bg="#FEAE35", font=("ThaleahFat", 30)).pack(pady=10)
        tk.Button(self.root, text="Tutup Saja", command=self.root.quit, bg="#FEAE35", font=("ThaleahFat", 30)).pack(pady=10)

    def page_5(self):
        self.clear_widgets()
        tk.Button(self.root, text="Nama Senjata", command=self.page_8, bg="#FEAE35", font=("ThaleahFat", 30)).pack(pady=30)
        tk.Button(self.root, text="Jenis Senjata", command=self.page_6, bg="#FEAE35", font=("ThaleahFat", 30)).pack(pady=30)
        tk.Button(self.root, text="Warna Senjata", command=self.page_7, bg="#FEAE35", font=("ThaleahFat", 30)).pack(pady=30)
        tk.Button(self.root, text="Kembali", command=self.page_2, bg="#FEAE35", font=("ThaleahFat", 30)).pack(pady=50)

    def page_6(self):
        self.clear_widgets()
        tk.Label(self.root, text="Jenis Senjata", font=("ThaleahFat", 50), bg="#404B6B", fg="white").pack(pady=20)

        for i, weapon in enumerate(self.weapon_types, start=1):
            frame = tk.Frame(self.root, bg="#404B6B")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{i}: {weapon}", font=("ThaleahFat", 15), bg="#404B6B", fg="white").pack(side="left", padx=10)
            tk.Button(frame, text="Pilih", command=lambda w=weapon: self.select_weapon(w), bg="#FEAE35", font=("ThaleahFat", 15)).pack(side="left", padx=10)
            tk.Button(frame, text="Hapus", command=lambda i=i-1: self.delete_weapon_type(i), bg="#FEAE35", font=("ThaleahFat", 15)).pack(side="left", padx=10)

        tk.Button(self.root, text="Tambah Jenis Senjata", command=self.add_weapon_type, bg="#FEAE35", font=("ThaleahFat", 15)).pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_8, bg="#FEAE35", font=("ThaleahFat", 15)).pack(pady=20)

    def page_7(self):
        self.clear_widgets()
        tk.Label(self.root, text="Warna Senjata", font=("ThaleahFat", 50), bg="#404B6B", fg="white").pack(pady=20)

        for i, color in enumerate(self.weapon_colors, start=1):
            frame = tk.Frame(self.root, bg="#404B6B")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{i}: {color}", font=("ThaleahFat", 15), bg="#404B6B", fg="white").pack(side="left", padx=10)
            tk.Button(frame, text="Pilih", command=lambda c=color: self.select_color(c), bg="#FEAE35", font=("ThaleahFat", 15)).pack(side="left", padx=10)
            tk.Button(frame, text="Hapus", command=lambda i=i-1: self.delete_color(i), bg="#FEAE35", font=("ThaleahFat", 15)).pack(side="left", padx=10)

        tk.Button(self.root, text="Tambah Warna Senjata", command=self.add_color, bg="#FEAE35", font=("ThaleahFat", 15)).pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_6, bg="#FEAE35", font=("ThaleahFat", 15)).pack(pady=20)

    def page_8(self):
        self.clear_widgets()
        tk.Label(self.root, text="Nama Senjata", font=("ThaleahFat", 50), bg="#404B6B", fg="white").pack(pady=20)

        for i, namea in enumerate(self.weapon_names, start=1):
            frame = tk.Frame(self.root, bg="#404B6B")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{i}: {namea}", font=("ThaleahFat", 15), bg="#404B6B", fg="white").pack(side="left", padx=10)
            tk.Button(frame, text="Pilih", command=lambda n=namea: self.select_name(n), bg="#FEAE35", font=("ThaleahFat", 15)).pack(side="left", padx=10)
            tk.Button(frame, text="Hapus", command=lambda i=i-1: self.delete_name(i), bg="#FEAE35", font=("ThaleahFat", 15)).pack(side="left", padx=10)

        tk.Button(self.root, text="Tambah Nama Senjata", command=self.add_name, bg="#FEAE35", font=("ThaleahFat", 15)).pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_5, bg="#FEAE35", font=("ThaleahFat", 15)).pack(pady=20)

    def delete_weapon(self, index):
        del self.weapon_data[index]
        self.page_3()

    def select_name(self, namea):
        self.selected_name = namea
        self.page_8()

    def select_weapon(self, weapon):
        self.selected_weapon = weapon
        self.page_7()

    def select_color(self, color):
        self.selected_color = color
        self.page_4(self.selected_name, self.selected_weapon, self.selected_color)

    def select_name(self, namea):
        self.selected_name = namea
        self.page_6()

    def delete_weapon_type(self, index):
        del self.weapon_types[index]
        self.page_6()

    def delete_color(self, index):
        del self.weapon_colors[index]
        self.page_7()

    def delete_name(self, index):
        del self.weapon_names[index] 
        self.page_8()

    def add_weapon_type(self):
        new_weapon = simpledialog.askstring("Tambah Jenis Senjata", "Ketik jenis senjata yang anda inginkan:")
        if new_weapon:
            self.weapon_types.append(new_weapon)
        self.page_6()

    def add_color(self):
        new_color = simpledialog.askstring("Tambah Warna Senjata", "Ketik warna senjata yang anda inginkan:")
        if new_color:
            self.weapon_colors.append(new_color)
        self.page_7()
    
    def add_name(self):
        new_name = simpledialog.askstring("Tambah Nama Senjata", "Ketik warna senjata yang anda inginkan:")
        if new_name:
            self.weapon_names.append(new_name)
        self.page_8()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeaponApp(root)
    root.mainloop()