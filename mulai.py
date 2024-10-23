import tkinter as tk
from tkinter import ttk, simpledialog
import json
from datetime import datetime

class JGWApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.configure(bg="#404B6B")
        self.title("JGW Weapon Selection")
        self.font_style_large = ("ThaleahFat", 16)  # Increased font size
        self.font_style_medium = ("ThaleahFat", 14)
        self.transaction_history = []
        self.load_data()
        self.weapon_types = ["1: Pistol", "2: Sniper", "3: Pisau", "4: Basoka", "5: Senapan"]
        self.weapon_colors = ["1: Hitam", "2: Pink", "3: Putih", "4: Kuning", "5: Hijau"]

        self.selected_weapon_type = ""
        self.selected_weapon_color = ""
        self.weapon_name = ""

        # Page 1
        self.page1()

    def page1(self):
        for widget in self.winfo_children():
            widget.destroy()

        label = tk.Label(self, text="Selamat Datang di JGW", font=self.font_style_large, bg="#404B6B", fg="white")
        label.pack(pady=50)

        button = tk.Button(self, text="Mulai", command=self.page2, bg="#FEAE35", font=self.font_style_large)
        button.pack()

    def page2(self):
        for widget in self.winfo_children():
            widget.destroy()

        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True, padx=20, pady=20)

        style = ttk.Style()
        style.configure('TNotebook.Tab', font=self.font_style_medium, background="#FEAE35", foreground="black")
        style.map('TNotebook.Tab', background=[('selected', '#FEAE35')], foreground=[('selected', 'black')])

        # Data Senjata Tab
        frame1 = tk.Frame(notebook, bg="#404B6B")
        notebook.add(frame1, text="Data Senjata")

        data_senjata = [
            "1: Glok; Pistol; Hitam", "2: AWP; Sniper; Pink", 
            "3: Karambit; Pisau; Putih", "4: Rudal; Basoka; Kuning", "5: Karabin; Senapan; Hijau"
        ]
        for item in data_senjata:
            tk.Label(frame1, text=item, font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)

        # Jenis Senjata Tab
        frame2 = tk.Frame(notebook, bg="#404B6B")
        notebook.add(frame2, text="Jenis Senjata")

        for item in self.weapon_types:
            tk.Label(frame2, text=item, font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)

        # Warna Senjata Tab
        frame3 = tk.Frame(notebook, bg="#404B6B")
        notebook.add(frame3, text="Warna Senjata")

        for item in self.weapon_colors:
            tk.Label(frame3, text=item, font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)

        # Buat Senjata Tab
        frame4 = tk.Frame(notebook, bg="#404B6B")
        notebook.add(frame4, text="Buat Senjata")

        self.nama_senjata_label = tk.Label(frame4, text="Nama Senjata:", font=self.font_style_medium, bg="#404B6B", fg="white")
        self.nama_senjata_label.pack(pady=10)

        self.nama_senjata_entry = tk.Entry(frame4, font=self.font_style_medium)
        self.nama_senjata_entry.pack(pady=5)

        # Bind Enter key to save name and move forward
        self.nama_senjata_entry.bind("<Return>", self.save_weapon_name)

        tk.Button(frame4, text="Jenis Senjata", command=self.page3, bg="#FEAE35", font=self.font_style_medium).pack(pady=5)
        tk.Button(frame4, text="Warna Senjata", command=self.page4, bg="#FEAE35", font=self.font_style_medium).pack(pady=5)

    def save_weapon_name(self, event):
        # Capture weapon name and update label
        self.weapon_name = self.nama_senjata_entry.get()
        self.nama_senjata_label.config(text=f"Nama Senjata: {self.weapon_name}")

    def page3(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Pilih Jenis Senjata", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10)

        for jenis in self.weapon_types:
            frame = tk.Frame(self, bg="#404B6B")
            frame.pack(pady=5)
            tk.Button(frame, text=jenis, command=lambda j=jenis: self.select_weapon_type(j), bg="#FEAE35", font=self.font_style_medium).pack(side="left", padx=5)
            tk.Button(frame, text="Hapus", command=lambda j=jenis: self.hapus_jenis(j), bg="#FEAE35", font=self.font_style_medium).pack(side="right", padx=5)

        tk.Button(self, text="Tambah Jenis Senjata", command=self.tambah_jenis, bg="#FEAE35", font=self.font_style_medium).pack(pady=10)
        tk.Button(self, text="Kembali", command=self.page2, bg="#FEAE35", font=self.font_style_medium).pack(pady=10)

    def select_weapon_type(self, jenis):
        self.selected_weapon_type = jenis
        self.page4()

    def page4(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Pilih Warna Senjata", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10)

        for warna in self.weapon_colors:
            frame = tk.Frame(self, bg="#404B6B")
            frame.pack(pady=5)
            tk.Button(frame, text=warna, command=lambda w=warna: self.select_weapon_color(w), bg="#FEAE35", font=self.font_style_medium).pack(side="left", padx=5)
            tk.Button(frame, text="Hapus", command=lambda w=warna: self.hapus_warna(w), bg="#FEAE35", font=self.font_style_medium).pack(side="right", padx=5)

        tk.Button(self, text="Tambah Warna Senjata", command=self.tambah_warna, bg="#FEAE35", font=self.font_style_medium).pack(pady=10)
        tk.Button(self, text="Kembali", command=self.page3, bg="#FEAE35", font=self.font_style_medium).pack(pady=10)

    def select_weapon_color(self, warna):
        self.selected_weapon_color = warna
        self.page5()

    def page5(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Kamu telah membuat", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self, text=f"Nama: {self.weapon_name}", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=5)
        tk.Label(self, text=f"Jenis: {self.selected_weapon_type}", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=5)
        tk.Label(self, text=f"Warna: {self.selected_weapon_color}", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=5)

        canvas = tk.Canvas(self, bg="#404B6B")
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#404B6B")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        tk.Label(scrollable_frame, text="Sejarah Transaksi", font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)
        for transaction in self.transaction_history:
            tk.Label(scrollable_frame, text=f"ID Transaksi: {transaction['id_transaksi']}, Jenis: {transaction['id_jenis']}, "
                                        f"Peluru: {transaction['peluru']}, Waktu: {transaction['waktu']}",
                    font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)

        tk.Button(self, text="Mulai Latihan", command=self.page6, bg="#FEAE35", font=self.font_style_large).pack(pady=10)
        tk.Button(self, text="Kembali", command=self.page2, bg="#FEAE35", font=self.font_style_large).pack(pady=10)

    def page6(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.shot_count = 0

        tk.Label(self, text="Latihan Menembak Senjata", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10)

        self.shot_label = tk.Label(self, text="Peluru Ditembak: 0", font=self.font_style_medium, bg="#404B6B", fg="white")
        self.shot_label.pack(pady=5)

        tk.Button(self, text="Tembak", command=self.tembak, bg="#FEAE35", font=self.font_style_large).pack(pady=5)
        tk.Button(self, text="Hasil", command=self.page7, bg="#FEAE35", font=self.font_style_large).pack(pady=5)
        tk.Button(self, text="Kembali", command=self.page5, bg="#FEAE35", font=self.font_style_large).pack(pady=10)

        # Button for sorting (can implement sorting logic here)
        tk.Button(self, text="Sortir", command=self.sortir_transaksi, bg="#FEAE35", font=self.font_style_large).pack(pady=5)

    def tembak(self):
        self.shot_count += 1
        self.shot_label.config(text=f"Peluru Ditembak: {self.shot_count}")

    def page7(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Hasil Latihan", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10)

        # Display transaction result
        transaction_id = len(self.transaction_history) + 1
        selected_weapon = self.selected_weapon_type  # This should be set when user selects weapon
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        transaction = {
            "id_transaksi": transaction_id,
            "id_jenis": selected_weapon,
            "peluru": self.shot_count,
            "waktu": current_time
        }
        self.transaction_history.append(transaction)

        tk.Label(self, text=f"ID Transaksi: {transaction['id_transaksi']}", font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)
        tk.Label(self, text=f"Jenis Senjata: {transaction['id_jenis']}", font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)
        tk.Label(self, text=f"Peluru Ditembak: {transaction['peluru']}", font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)
        tk.Label(self, text=f"Waktu: {transaction['waktu']}", font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)

        tk.Button(self, text="Kembali", command=self.page6, bg="#FEAE35", font=self.font_style_large).pack(pady=10)
        tk.Button(self, text="Selesai", command=self.page8, bg="#FEAE35", font=self.font_style_large).pack(pady=10)

    def page8(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Latihan yang Bagus!", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10)

        tk.Button(self, text="Home", command=self.page1, bg="#FEAE35", font=self.font_style_large).pack(pady=10)
        tk.Button(self, text="Selesai", command=self.quit_app, bg="#FEAE35", font=self.font_style_large).pack(pady=10)

    def quit_app(self):
        # Save transaction history to a file or database before exiting
        self.save_data()
        self.destroy() 

    def tambah_jenis(self):
        jenis_baru = simpledialog.askstring("Tambah Jenis Senjata", "Masukkan jenis senjata:")
        if jenis_baru:
            self.weapon_types.append(jenis_baru)
            self.page3()

    def tambah_warna(self):
        warna_baru = simpledialog.askstring("Tambah Warna Senjata", "Masukkan warna senjata:")
        if warna_baru:
            self.weapon_colors.append(warna_baru)
            self.page4()

    def hapus_jenis(self, jenis):
        self.weapon_types.remove(jenis)
        self.page3()

    def hapus_warna(self, warna):
        self.weapon_colors.remove(warna)
        self.page4()

    def save_data(self):
        with open("transaction_history.json", "w") as file:
            json.dump(self.transaction_history, file)

    def load_data(self):
        try:
            with open("transaction_history.json", "r") as file:
                self.transaction_history = json.load(file)
        except FileNotFoundError:
            self.transaction_history = []


if __name__ == "__main__":
    app = JGWApp()
    app.mainloop()