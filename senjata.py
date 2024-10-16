import tkinter as tk
from tkinter import simpledialog
import time

class WeaponApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x1024")
        self.root.configure(bg="#404B6B")

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
        self.transaction_data = []

        self.page_1()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_scrollable_frame(self):
        canvas = tk.Canvas(self.root, bg="#404B6B")
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#404B6B")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((720, 0), window=scrollable_frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return scrollable_frame

    def page_1(self):
        self.clear_widgets()
        scrollable_frame = self.create_scrollable_frame()
        tk.Label(scrollable_frame, text="Selamat datang di Dunia JGW!", font=("Arial", 70), bg="#404B6B", fg="white").pack(pady=200)
        tk.Button(scrollable_frame, text="Mulai", command=self.page_2, bg="#FEAE35", font=("Arial", 50)).pack(pady=20)

    def page_2(self):
        self.clear_widgets()
        scrollable_frame = self.create_scrollable_frame()
        tk.Label(scrollable_frame, text="Ayo bertarung! Pilih senjatamu!", font=("Arial", 70), bg="#404B6B", fg="white").pack(pady=150)
        tk.Button(scrollable_frame, text="Data Senjata", command=self.page_3, bg="#FEAE35", font=("Arial", 50)).pack(pady=20)
        tk.Button(scrollable_frame, text="Buat Senjata", command=self.page_5, bg="#FEAE35", font=("Arial", 50)).pack(pady=20)

    def page_3(self):
        self.clear_widgets()
        scrollable_frame = self.create_scrollable_frame()
        tk.Label(scrollable_frame, text="Data Senjata", font=("Arial", 50), bg="#404B6B", fg="white").pack(pady=40)

        for i, (namea, weapon, color) in enumerate(self.weapon_data, start=1):
            frame = tk.Frame(scrollable_frame, bg="#404B6B")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{i}: {namea} {weapon}; {color}", font=("Arial", 15), bg="#404B6B", fg="white").pack(side="left", padx=5)
            tk.Button(frame, text="Pilih", command=lambda n=namea, w=weapon, c=color: self.page_4(n, w, c), bg="#FEAE35", font=("Arial", 15)).pack(side="left", padx=5)
            tk.Button(frame, text="Hapus", command=lambda i=i-1: self.delete_weapon(i), bg="#FEAE35", font=("Arial", 15)).pack(side="left", padx=5)

        tk.Button(scrollable_frame, text="Kembali", command=self.page_2, bg="#FEAE35", font=("Arial", 30)).pack(pady=20)

    def page_4(self, namea, weapon, color):
        self.clear_widgets()
        self.selected_name = namea
        self.selected_color = color
        self.selected_weapon = weapon
        tk.Label(self.root, text=f"Anda telah membuat", font=("Arial", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self.root, text=f"Nama: {namea}", font=("Arial", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self.root, text=f"Jenis: {weapon}", font=("Arial", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self.root, text=f"Warna: {color}", font=("Arial", 30), bg="#404B6B", fg="white").pack(pady=10)
        tk.Button(self.root, text="Ayo Latihan Bertarung", command=self.page_training, bg="#FEAE35", font=("Arial", 30)).pack(pady=10)
        tk.Button(self.root, text="Kembali", command=self.page_2, bg="#FEAE35", font=("Arial", 30)).pack(pady=10)

    def page_5(self):
        self.clear_widgets()
        tk.Button(self.root, text="Nama Senjata", command=self.page_8, bg="#FEAE35", font=("Arial", 30)).pack(pady=30)
        tk.Button(self.root, text="Jenis Senjata", command=self.page_6, bg="#FEAE35", font=("Arial", 30)).pack(pady=30)
        tk.Button(self.root, text="Warna Senjata", command=self.page_7, bg="#FEAE35", font=("Arial", 30)).pack(pady=30)
        tk.Button(self.root, text="Kembali", command=self.page_2, bg="#FEAE35", font=("Arial", 30)).pack(pady=50)

    def page_6(self):
        self.clear_widgets()
        scrollable_frame = self.create_scrollable_frame()
        tk.Label(scrollable_frame, text="Jenis Senjata", font=("Arial", 50), bg="#404B6B", fg="white").pack(pady=20)

        for i, weapon in enumerate(self.weapon_types, start=1):
            frame = tk.Frame(scrollable_frame, bg="#404B6B")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{i}: {weapon}", font=("Arial", 15), bg="#404B6B", fg="white").pack(side="left", padx=10)
            tk.Button(frame, text="Pilih", command=lambda w=weapon: self.select_weapon(w), bg="#FEAE35", font=("Arial", 15)).pack(side="left", padx=10)
            tk.Button(frame, text="Hapus", command=lambda i=i-1: self.delete_weapon_type(i), bg="#FEAE35", font=("Arial", 15)).pack(side="left", padx=10)

        tk.Button(scrollable_frame, text="Tambah Jenis Senjata", command=self.add_weapon_type, bg="#FEAE35", font=("Arial", 15)).pack(pady=20)
        tk.Button(scrollable_frame, text="Kembali", command=self.page_8, bg="#FEAE35", font=("Arial", 15)).pack(pady=20)

    def page_7(self):
        self.clear_widgets()
        scrollable_frame = self.create_scrollable_frame()
        tk.Label(scrollable_frame, text="Warna Senjata", font=("Arial", 50), bg="#404B6B", fg="white").pack(pady=20)

        for i, color in enumerate(self.weapon_colors, start=1):
            frame = tk.Frame(scrollable_frame, bg="#404B6B")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{i}: {color}", font=("Arial", 15), bg="#404B6B", fg="white").pack(side="left", padx=10)
            tk.Button(frame, text="Pilih", command=lambda c=color: self.select_color(c), bg="#FEAE35", font=("Arial", 15)).pack(side="left", padx=10)
            tk.Button(frame, text="Hapus", command=lambda i=i-1: self.delete_color(i), bg="#FEAE35", font=("Arial", 15)).pack(side="left", padx=10)

        tk.Button(scrollable_frame, text="Tambah Warna Senjata", command=self.add_color, bg="#FEAE35", font=("Arial", 15)).pack(pady=20)
        tk.Button(scrollable_frame, text="Kembali", command=self.page_6, bg="#FEAE35", font=("Arial", 15)).pack(pady=20)

    def page_8(self):
        self.clear_widgets()
        scrollable_frame = self.create_scrollable_frame()
        tk.Label(scrollable_frame, text="Nama Senjata", font=("Arial", 50), bg="#404B6B", fg="white").pack(pady=20)

        for i, namea in enumerate(self.weapon_names, start=1):
            frame = tk.Frame(scrollable_frame, bg="#404B6B")
            frame.pack(pady=5)
            tk.Label(frame, text=f"{i}: {namea}", font=("Arial", 15), bg="#404B6B", fg="white").pack(side="left", padx=10)
            tk.Button(frame, text="Pilih", command=lambda n=namea: self.select_name(n), bg="#FEAE35", font=("Arial", 15)).pack(side="left", padx=10)
            tk.Button(frame, text="Hapus", command=lambda i=i-1: self.delete_name(i), bg="#FEAE35", font=("Arial", 15)).pack(side="left", padx=10)

        tk.Button(scrollable_frame, text="Tambah Nama Senjata", command=self.add_name, bg="#FEAE35", font=("Arial", 15)).pack(pady=20)
        tk.Button(scrollable_frame, text="Kembali", command=self.page_5, bg="#FEAE35", font=("Arial", 15)).pack(pady=20)

    def page_training(self):
        self.clear_widgets()
        self.shoot_count = 0
        tk.Label(self.root, text="Latihan Menembak Senjata", font=("Arial", 50), bg="#404B6B", fg="white").pack(pady=50)

        self.shoot_label = tk.Label(self.root, text=f"Tembakan: {self.shoot_count}", font=("Arial", 30), bg="#404B6B", fg="white")
        self.shoot_label.pack(pady=20)

        tk.Button(self.root, text="Tembak", command=self.shoot, bg="#FEAE35", font=("Arial", 30)).pack(pady=20)
        tk.Button(self.root, text="Kembali", command=self.page_2, bg="#FEAE35", font=("Arial", 30)).pack(pady=10)
        tk.Button(self.root, text="Hasil", command=self.show_results, bg="#FEAE35", font=("Arial", 30)).pack(pady=10)

    def delete_weapon(self, index):
        del self.weapon_data[index]
        self.page_3()

    def select_name(self, namea):
        self.selected_name = namea
        self.page_6()

    def select_weapon(self, weapon):
        self.selected_weapon = weapon
        self.page_7()

    def select_color(self, color):
        self.selected_color = color
        self.page_4(self.selected_name, self.selected_weapon, self.selected_color)

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
        new_name = simpledialog.askstring("Tambah Nama Senjata", "Ketik nama senjata yang anda inginkan:")
        if new_name:
            self.weapon_names.append(new_name)
        self.page_8()

    def shoot(self):
        self.shoot_count += 1
        self.shoot_label.config(text=f"Tembakan: {self.shoot_count}")

    def show_results(self):
        weapon_ids = self.read_weapon_ids()
        weapon_id = None

        for id_key, weapon_name in weapon_ids.items():
            if weapon_name.upper() == self.selected_weapon:
                weapon_id = id_key
                break

        if weapon_id is None:
            print(f"Weapon ID for {self.selected_weapon} not found in jenis.txt")
            return

        current_time = time.strftime("%H:%M:%S")
        transaction = {
            "id_transaksi": len(self.transaction_data) + 1,
            "id_jenis": weapon_id,
            "jumlah_tembakan": self.shoot_count,
            "waktu_kegiatan": current_time
        }

        self.transaction_data.append(transaction)

        with open('transactions.txt', 'a') as file:
            file.write(f"{transaction['id_transaksi']}, {transaction['id_jenis']}, {transaction['jumlah_tembakan']}, {transaction['waktu_kegiatan']}\n")

        self.clear_widgets()
        tk.Label(self.root, text="HASIL LATIHAN", font=("Arial", 50), bg="#404B6B", fg="white").pack(pady=20)

        table_frame = tk.Frame(self.root, bg="#404B6B")
        table_frame.pack(pady=20)

        tk.Label(table_frame, text="ID TRANSAKSI", font=("Arial", 20), bg="#FEAE35", fg="black", width=15).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(table_frame, text="ID JENIS", font=("Arial", 20), bg="#FEAE35", fg="black", width=15).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(table_frame, text="PELAURU YANG DIGUNAKAN", font=("Arial", 20), bg="#FEAE35", fg="black", width=25).grid(row=0, column=2, padx=5, pady=5)
        tk.Label(table_frame, text="WAKTU KEGIATAN", font=("Arial", 20), bg="#FEAE35", fg="black", width=15).grid(row=0, column=3, padx=5, pady=5)

        for i, trans in enumerate(self.transaction_data):
            tk.Label(table_frame, text=trans['id_transaksi'], font=("Arial", 20), bg="#FEAE35", fg="black", width=15).grid(row=i + 1, column=0, padx=5, pady=5)
            tk.Label(table_frame, text=trans['id_jenis'], font=("Arial", 20), bg="#FEAE35", fg="black", width=15).grid(row=i + 1, column=1, padx=5, pady=5)
            tk.Label(table_frame, text=trans['jumlah_tembakan'], font=("Arial", 20), bg="#FEAE35", fg="black", width=25).grid(row=i + 1, column=2, padx=5, pady=5)
            tk.Label(table_frame, text=trans['waktu_kegiatan'], font=("Arial", 20), bg="#FEAE35", fg="black", width=15).grid(row=i + 1, column=3, padx=5, pady=5)

        button_frame = tk.Frame(self.root, bg="#404B6B")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="KEMBALI", command=self.page_training, bg="#FEAE35", font=("Arial", 30)).pack(side="left", padx=20)
        tk.Button(button_frame, text="SELESAI", command=self.root.quit, bg="#FEAE35", font=("Arial", 30)).pack(side="left", padx=20)

    def read_weapon_ids(self):
        weapon_ids = {}
        try:
            with open("jenis.txt", 'r') as file:
                for line in file:
                    key, value = line.strip().split(': ', 1)
                    weapon_ids[key] = value
        except FileNotFoundError:
            print("File jenis.txt not found.")
        return weapon_ids

if __name__ == "__main__":
    root = tk.Tk()
    app = WeaponApp(root)
    root.mainloop()  # Ensure the Tkinter mainloop is started