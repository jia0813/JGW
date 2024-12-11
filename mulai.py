import tkinter as tk
from tkinter import ttk, simpledialog
import json
from datetime import datetime
from tkinter import ttk, simpledialog, messagebox
from tkcalendar import DateEntry
import datetime
import ast

class JGWApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.configure(bg="#404B6B")
        self.title("JGW Weapon Selection")
        self.font_style_large = ("ThaleahFat", 10)  # Increased font size
        self.font_style_medium = ("ThaleahFat", 8)
        self.transaction_history = []
        self.jenis_map = {}   # Mapping for jenis senjata
        self.warna_map = {}   # Mapping for warna senjata
        self.weapon_types = []
        self.weapon_colors = []
        self.load_data()
        
        self.weapon_types = []
        self.weapon_colors = []
        self.load_weapon_data()

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
        self.load_weapon_data()
        # Create "Keluar" button at the top-right corner of the main window
        keluar_button = tk.Button(self, text="KELUAR", command=self.quit_app, bg="#FEAE35", font=self.font_style_medium)
        keluar_button.place(x=1170, y=10)  # Adjust the x and y position as needed based on window size

        # Notebook for tabs
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True, padx=20, pady=50)  # Adjust the padding to leave space for "Keluar" button

        style = ttk.Style()
        style.configure('TNotebook.Tab', font=self.font_style_medium, background="#FEAE35", foreground="black")
        style.map('TNotebook.Tab', background=[('selected', '#FEAE35')], foreground=[('selected', 'black')])

        # Data Senjata Tab
        frame1 = tk.Frame(notebook, bg="#404B6B")
        frame2 = tk.Frame(notebook, bg="#404B6B")
        frame3 = tk.Frame(notebook, bg="#404B6B")
        frame4 = tk.Frame(notebook, bg="#404B6B")
        notebook.add(frame1, text="Data Senjata")
        notebook.add(frame2, text="Jenis Senjata")
        notebook.add(frame3, text="Warna Senjata")
        notebook.add(frame4, text="Hasil Latihan")
        
        # Display weapon data from self.weapon_data_list in Data Senjata tab
        for item in self.weapon_data_list:
            item_frame = tk.Frame(frame1, bg="#404B6B")
            item_frame.pack(fill='x', padx=10, pady=5)

            # "Lihat" button
            tk.Button(item_frame, text="LIHAT", command=lambda i=item: print(i) or self.view_weapon(i), bg="#FEAE35", font=self.font_style_medium).pack(side="left", padx=5)

            # Display weapon details
            tk.Label(item_frame, text=";".join(ast.literal_eval(item.split(": ")[1])), font=self.font_style_medium, bg="#404B6B", fg="white").pack(side="left", padx=10)
            tk.Button(item_frame, text="PILIH", command=lambda i=item: print(i) or self.select_weapon(i), bg="#FEAE35", font=self.font_style_medium).pack(side="right", padx=5)
            # "Pilih" and "Hapus" buttons
            tk.Button(item_frame, text="HAPUS", command=lambda i=item: self.delete_weapon(i), bg="#FEAE35", font=self.font_style_medium).pack(side="right", padx=5)

        # "Tambah Data Senjata" button
        tk.Button(frame1, text="TAMBAH DATA SENJATA", command=self.tambah_data_senjata, bg="#FEAE35", font=self.font_style_medium).pack(pady=20)
        control_frame = tk.Frame(frame1, bg="#404B6B")
        control_frame.pack(pady=20)

        # Add data from jenis.txt to the Jenis Senjata tab
        self.load_jenis_data()
        for index, jenis in enumerate(self.weapon_types, start=1):
            jenis_frame = tk.Frame(frame2, bg="#404B6B")
            jenis_frame.pack(fill='x', padx=10, pady=5)

            tk.Button(jenis_frame, text="LIHAT", command=lambda j=jenis: self.view_weapons_by_type(j), bg="#FEAE35", font=self.font_style_medium).pack(side="left", padx=5)
            # Display the index and jenis
            tk.Label(jenis_frame, text=f"{jenis}", font=self.font_style_medium, bg="#404B6B", fg="white").pack(side="left", padx=10)

            # "Lihat" button for viewing weapons of this type
            

            # "Pilih" and "Hapus" buttons for each jenis
            tk.Button(jenis_frame, text="HAPUS", command=lambda j=jenis: self.hapus_jenis(j), bg="#FEAE35", font=self.font_style_medium).pack(side="right", padx=5)

        # "Tambah Jenis Senjata" button
        tk.Button(frame2, text="TAMBAH JENIS SENJATA", command=self.tambah_jenis, bg="#FEAE35", font=self.font_style_medium).pack(pady=20)

        # Add data from warna.txt to the Warna Senjata tab
        self.load_warna_data()

        for index, warna in enumerate(self.weapon_colors, start=1):
            warna_frame = tk.Frame(frame3, bg="#404B6B")
            warna_frame.pack(fill='x', padx=10, pady=5)
            tk.Button(warna_frame, text="LIHAT", command=lambda w=warna: self.view_weapons_by_color(w), bg="#FEAE35", font=self.font_style_medium).pack(side="left", padx=5)
            # Display the index and warna
            tk.Label(warna_frame, text=f"{warna}", font=self.font_style_medium, bg="#404B6B", fg="white").pack(side="left", padx=10)
            
            # "Pilih" and "Hapus" buttons for each warna
            tk.Button(warna_frame, text="HAPUS", command=lambda w=warna: self.hapus_warna(w), bg="#FEAE35", font=self.font_style_medium).pack(side="right", padx=5)

        # "Tambah Warna Senjata" button
        tk.Button(frame3, text="TAMBAH WARNA SENJATA", command=self.tambah_warna, bg="#FEAE35", font=self.font_style_medium).pack(pady=20)

        # Title for the "Hasil Latihan" section, centered
        tk.Label(frame4, text="HASIL LATIHAN", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10, anchor="center")

        # Centered headers
        headers_frame = tk.Frame(frame4, bg="#404B6B")
        headers_frame.pack(pady=5, anchor="center")
        tk.Label(headers_frame, text="DATA SENJATA", font=self.font_style_medium, bg="#404B6B", fg="white", width=15).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(headers_frame, text="PELURU", font=self.font_style_medium, bg="#404B6B", fg="white", width=10).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(headers_frame, text="WAKTU", font=self.font_style_medium, bg="#404B6B", fg="white", width=20).grid(row=0, column=2, padx=5, pady=5)
        tk.Label(headers_frame, text="", font=self.font_style_medium, bg="#404B6B", fg="white", width=10).grid(row=0, column=3, padx=5, pady=5)  # Empty for Hapus button

        # Display each transaction in a centered row
        for index, transaction in enumerate(self.transaction_history):
            transaction_frame = tk.Frame(frame4, bg="#404B6B")
            transaction_frame.pack(anchor="center", pady=2)  # Center each row
            
            # Extract data for display
            weapon_id = transaction["id_senjata"]
            peluru = transaction["peluru"]
            waktu = transaction["waktu"]
            
            # Display data for each transaction, centered
            tk.Label(transaction_frame, text=weapon_id, font=self.font_style_medium, bg="#FEAE35", fg="black", width=15).grid(row=0, column=0, padx=5, pady=5)
            tk.Label(transaction_frame, text=str(peluru), font=self.font_style_medium, bg="#FEAE35", fg="black", width=10).grid(row=0, column=1, padx=5, pady=5)
            tk.Label(transaction_frame, text=waktu, font=self.font_style_medium, bg="#FEAE35", fg="black", width=20).grid(row=0, column=2, padx=5, pady=5)
            
            # "Hapus" button to delete the transaction
            tk.Button(transaction_frame, text="HAPUS", command=lambda t=transaction: self.delete_transaction(t), bg="#FEAE35", font=self.font_style_medium, width=10).grid(row=0, column=3, padx=5, pady=5)

        # Centered Sort button at the bottom
        tk.Button(frame4, text="SORTIR", command=self.sort_transactions, bg="#FEAE35", font=self.font_style_medium).pack(pady=10, anchor="center")

    def view_weapons_by_color(self, warna):
        # Filter weapons by color (warna)
        filtered_weapons = []
        color_to_search = warna.split(": ")[1].strip().lower()

        # Iterate through weapon data list and filter by color
        for weapon in self.weapon_data_list:
            weapon_data = ast.literal_eval(weapon.split(": ")[1])  # Convert string representation to list
            if len(weapon_data) > 2 and weapon_data[2].strip().lower() == color_to_search:
                filtered_weapons.append(weapon)

        # Create a popup window to display weapon details
        popup = tk.Toplevel(self)
        popup.geometry("600x500")
        popup.configure(bg="#404B6B")
        popup.title(f"Details for Weapon Color: {warna}")

        frame = tk.Frame(popup, bg="#404B6B")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Column headers for the data table with yellow background
        headers = ["Data Senjata", "Digunakan", "Peluru", "Waktu"]
        for i, header in enumerate(headers):
            tk.Label(frame, text=header, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=1, column=i, padx=10, pady=5)

        row_counter = 2  # Start adding data from row 2 (row 1 is for headers)
        total_usage_all_weapons = 0
        total_ammo_all_weapons = 0
        found_any_data = False  # Flag to check if any data was found for any weapon

        for weapon in filtered_weapons:
            weapon_data = ast.literal_eval(weapon.split(": ")[1])  # Convert string representation to list
            weapon_name = weapon_data[0]  # Assuming weapon name is the first part

            # Filter transactions related to the current weapon
            related_transactions = [t for t in self.transaction_history if t["id_senjata"] == weapon_name]

            if related_transactions:
                found_any_data = True  # Set flag to True if data exists
                for index, transaction in enumerate(related_transactions, start=row_counter):
                    ammo = transaction["peluru"]
                    time = transaction["waktu"]

                    # Display the counter in the "Digunakan" column
                    counter = index - row_counter + 1  # Start from 1 for each weapon

                    # Add labels for each piece of data with yellow background and consistent size
                    tk.Label(frame, text=weapon_name, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=0, padx=10, pady=5)
                    tk.Label(frame, text=str(counter), font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=1, padx=10, pady=5)
                    tk.Label(frame, text=ammo, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=2, padx=10, pady=5)
                    tk.Label(frame, text=time, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=3, padx=10, pady=5)

                # Move the row counter down after each weapon
                row_counter += len(related_transactions)
            else:
                if found_any_data:  # If data has already been found for a previous weapon
                    tk.Label(frame, text="...", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=0, padx=10, pady=5)
                    tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=1, padx=10, pady=5)
                    tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=2, padx=10, pady=5)
                    tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=3, padx=10, pady=5)
                    row_counter += 1
                else:
                    # Skip the else block if there is data earlier, this part prevents the "no data" message
                    tk.Label(frame, text="...", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=0, padx=10, pady=5)
                    tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=1, padx=10, pady=5)
                    tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=2, padx=10, pady=5)
                    tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=3, padx=10, pady=5)
                    row_counter += 1

                # Add the summary for each weapon after all transactions
                total_usage_all_weapons += len(related_transactions)
                total_ammo_all_weapons += sum(int(t["peluru"]) for t in related_transactions) if related_transactions else 0

            # Add the summary row for all weapons at the end of the table
            summary_row = row_counter
            tk.Label(frame, text="Jumlah", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=0, padx=10, pady=5)
            tk.Label(frame, text=f"{total_usage_all_weapons}x digunakan", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=1, padx=10, pady=5)
            tk.Label(frame, text=f"{total_ammo_all_weapons}x digunakan", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=2, padx=10, pady=5)

            # Move the row counter down after the summary
            row_counter += 1
    def view_weapons_by_type(self, jenis):
        # Filter weapons by type (jenis)
        filtered_weapons = []
        filtered_weapons = [weapon for weapon in self.weapon_data_list if jenis.split(": ")[1].strip().lower() in weapon]
        #ambil data dari weapon list, terus difilter
        js = jenis.split(": ")[1]
        for wp in self.weapon_data_list:
            js_dalam = wp.split(": ")[1].split(",")[1][2:-1]
            if js_dalam == js:
                filtered_weapons.append(wp)
        #print(jenis.split(": ")[1].strip().lower())
        #print(self.weapon_data_list)
        print(js_dalam)
 
        if filtered_weapons:
            # Create a popup window to display weapon details
            popup = tk.Toplevel(self)
            popup.geometry("600x500")
            popup.configure(bg="#404B6B")
            popup.title(f"Details for Weapon Type: {jenis}")

            frame = tk.Frame(popup, bg="#404B6B")
            frame.pack(fill="both", expand=True, padx=20, pady=20)

            # Column headers for the data table with yellow background
            headers = ["Data Senjata", "Digunakan", "Peluru", "Waktu"]
            for i, header in enumerate(headers):
                tk.Label(frame, text=header, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=1, column=i, padx=10, pady=5)

            row_counter = 2  # Start adding data from row 2 (row 1 is for headers)
            total_usage_all_weapons = 0
            total_ammo_all_weapons = 0
            found_any_data = False  # Flag to check if any data was found for any weapon

            for weapon in filtered_weapons:
                #print(ast.literal_eval(weapon.split(": ")[1])[0])
                weapon_id = ast.literal_eval(weapon.split(": ")[1])[1]  # Assuming weapon ID is stored in 'id_senjata'
                weapon_name = ast.literal_eval(weapon.split(": ")[1])[0]  # Assuming weapon name is stored in 'name'

                # Filter transactions related to the current weapon
                related_transactions = [t for t in self.transaction_history if t["id_senjata"] == weapon_name]
                #print("related",related_transactions)
                
                if related_transactions:  # If there are transactions
                    found_any_data = True  # Set flag to True if data exists
                    for index, transaction in enumerate(related_transactions, start=row_counter):
                        ammo = transaction["peluru"]
                        time = transaction["waktu"]

                        # Display the counter in the "Digunakan" column
                        counter = index - row_counter + 1  # Start from 1 for each weapon

                        # Add labels for each piece of data with yellow background and consistent size
                        tk.Label(frame, text=weapon_name, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=0, padx=10, pady=5)
                        tk.Label(frame, text=str(counter), font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=1, padx=10, pady=5)
                        tk.Label(frame, text=ammo, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=2, padx=10, pady=5)
                        tk.Label(frame, text=time, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=3, padx=10, pady=5)
                    
                    # Move the row counter down after each weapon
                    row_counter += len(related_transactions)
                else:  # If no transactions are found
                    if found_any_data:  # If data has already been found for a previous weapon
                        tk.Label(frame, text="...", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=0, padx=10, pady=5)
                        tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=1, padx=10, pady=5)
                        tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=2, padx=10, pady=5)
                        tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=3, padx=10, pady=5)
                        row_counter += 1
                    else:
                        # Skip the else block if there is data earlier, this part prevents the "no data" message
                        tk.Label(frame, text="...", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=0, padx=10, pady=5)
                        tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=1, padx=10, pady=5)
                        tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=2, padx=10, pady=5)
                        tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=row_counter, column=3, padx=10, pady=5)
                        row_counter += 1

                # Add the summary for each weapon after all transactions
                total_usage_all_weapons += len(related_transactions)
                total_ammo_all_weapons += sum(int(t["peluru"]) for t in related_transactions) if related_transactions else 0

            # Add the summary row for all weapons at the end of the table
            summary_row = row_counter
            tk.Label(frame, text="Jumlah", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=0, padx=10, pady=5)
            tk.Label(frame, text=f"{total_usage_all_weapons}x digunakan", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=1, padx=10, pady=5)
            tk.Label(frame, text=f"{total_ammo_all_weapons}x digunakan", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=2, padx=10, pady=5)

            # Move the row counter down after the summary
            row_counter += 1

        else:
            # If no weapons of the selected type are found, show a message
            tk.messagebox.showinfo("No weapons", f"No weapons found for type: {jenis}")






    def delete_transaction(self, transaction):
        # Tampilkan dialog konfirmasi untuk penghapusan
        result = tk.messagebox.askyesno("Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus transaksi ini?")
        if result:
            # Hapus transaksi dari transaction_history
            self.transaction_history = [t for t in self.transaction_history if t != transaction]
            
            # Simpan data yang telah diperbarui ke data.json
            self.save_data()

            # Refresh halaman untuk menampilkan daftar yang telah diperbarui
            self.page2()

    def delete_weapon(self, weapon):
        # Confirm deletion
        result = tk.messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {weapon}?")
        if not result:
            return  # Exit if user cancels

        # Remove from the weapon_data_list
        self.weapon_data_list = [item for item in self.weapon_data_list if item != weapon]
        weapon_id = weapon.split(":")[0].strip()

        # Update weapon_id_map and remove from senjata.txt
        self.weapon_id_map.pop(weapon_id, None)
        try:
            # Write updated list back to senjata.txt
            with open("senjata.txt", "w") as file:
                for index,item in enumerate(self.weapon_data_list, start=1):
                    item_list = item.split(': ')
                    item_list = ast.literal_eval(item_list[1])
                    file.write(f"{index} => {item_list[0]};{item_list[1]};{item_list[2]}\n")
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File senjata.txt not found.")

        # Refresh the page to show updated list
        self.page2()
    def display_selected_weapon(self, weapon_name, weapon_type_id, weapon_color_id):
        # Look up the names for the type and color based on their IDs
        weapon_type_name = self.jenis_map.get(weapon_type_id, "Unknown Type")
        weapon_color_name = self.warna_map.get(weapon_color_id, "Unknown Color")

        # Clear the current widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Display the weapon information
        tk.Label(self, text="KAMU TELAH MEMBUAT", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10)
        tk.Label(self, text=f"NAMA: {weapon_name}", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=5)
        tk.Label(self, text=f"JENIS: {weapon_type_name}", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=5)
        tk.Label(self, text=f"WARNA: {weapon_color_name}", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=5)

        # Buttons for next actions
        tk.Button(self, text="MULAI LATIHAN", command=self.page6, bg="#FEAE35", font=self.font_style_large).pack(pady=10)
        tk.Button(self, text="KEMBALI", command=self.page2, bg="#FEAE35", font=self.font_style_large).pack(pady=5)

    def view_weapon(self, weapon):
        # Extract the weapon ID from the weapon string (e.g., "1: Glok; Pistol; Hitam")
        weapon_id = weapon.split(": ")[0].strip()
        weapon_info = self.weapon_id_map.get(weapon_id, "Unknown Weapon")
        weapon_name = weapon_info[0]  # Get only the weapon name
        
        # Filter transactions related to this weapon to get ammo and time details
        related_transactions = [t for t in self.transaction_history if t["id_senjata"] == weapon_name]
        
        # Calculate totals for the summary
        if related_transactions:
            total_usage = len(related_transactions)  # Total number of times the weapon was used
            total_ammo = sum(int(transaction["peluru"]) for transaction in related_transactions)  # Total ammo used
        else:
            total_usage = 0
            total_ammo = 0
        
        # Popup window for displaying the weapon info
        popup = tk.Toplevel(self)
        popup.geometry("600x500")  # Adjust size to fit all data and summary
        popup.configure(bg="#404B6B")  # Set background to match design
        popup.title("Weapon Usage Details")

        # Add a frame to contain the label and button, and center-align it
        frame = tk.Frame(popup, bg="#404B6B")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Column headers for the data table with yellow background
        headers = ["Data Senjata", "Digunakan", "Peluru", "Waktu"]
        for i, header in enumerate(headers):
            tk.Label(frame, text=header, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=1, column=i, padx=10, pady=5)

        # Add data rows for each transaction related to the weapon
        if related_transactions:
            for index, transaction in enumerate(related_transactions, start=2):  # Starting from row 2
                weapon_data = transaction["id_senjata"]
                ammo = transaction["peluru"]
                time = transaction["waktu"]

                # Display the counter in the "Digunakan" column
                counter = index - 1  # This will start from 1, 2, 3, etc.
                
                # Add labels for each piece of data with yellow background and consistent size
                tk.Label(frame, text=weapon_data, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=0, padx=10, pady=5)
                tk.Label(frame, text=str(counter), font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=1, padx=10, pady=5)  # Display the counter here
                tk.Label(frame, text=ammo, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=2, padx=10, pady=5)
                tk.Label(frame, text=time, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=index, column=3, padx=10, pady=5)
                # Rekapitulasi Data (Summary) Section
                summary_row = len(related_transactions) + 2  # Position of the summary row

                # Add labels for the summary section
                tk.Label(frame, text="Jumlah", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=0, padx=10, pady=5)
                tk.Label(frame, text=f"{total_usage}x digunakan", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=1, padx=10, pady=5)
                tk.Label(frame, text=f"{total_ammo}x digunakan", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=2, padx=10, pady=5)
        else:
            # If no data found, display the weapon name with 0s
            tk.Label(frame, text=weapon_name, font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=2, column=0, padx=10, pady=5)
            tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=2, column=1, padx=10, pady=5)
            tk.Label(frame, text="0", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=2, column=2, padx=10, pady=5)
            tk.Label(frame, text="-", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=2, column=3, padx=10, pady=5)
            summary_row = 3  # Position of the summary row

            # Add labels for the summary section
            tk.Label(frame, text="Jumlah", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=0, padx=10, pady=5)
            tk.Label(frame, text=f"{total_usage}x digunakan", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=1, padx=10, pady=5)
            tk.Label(frame, text=f"{total_ammo}x digunakan", font=("ThaleahFat", 12), bg="#FEAE35", fg="black", width=20, height=1, anchor='center').grid(row=summary_row, column=2, padx=10, pady=5)

        

        # OK button to close the popup with yellow background
        tk.Button(frame, text="OK", command=popup.destroy, bg="#FEAE35", font=self.font_style_medium, width=15).grid(row=summary_row + 1, column=0, columnspan=4, pady=20)




    def create_weapon_tab(self, frame):
        tk.Label(frame, text="Nama Senjata:", font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=10)
        self.nama_senjata_entry = tk.Entry(frame, font=self.font_style_medium)
        self.nama_senjata_entry.pack(pady=5)
        self.nama_senjata_entry.bind("<Return>", self.save_weapon_name)

        tk.Button(frame, text="Jenis Senjata", command=self.page3, bg="#FEAE35", font=self.font_style_medium).pack(pady=5)
        tk.Button(frame, text="Warna Senjata", command=self.page4, bg="#FEAE35", font=self.font_style_medium).pack(pady=5)
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

    def select_weapon_type(self, jenis, notebook):
        # Store the selected weapon type and switch to the Warna Senjata tab
        self.selected_weapon_type = jenis.split(": ", 1)[-1]  # Extract the type name
        self.select_tab(notebook, "Warna Senjata")

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
        # Store the selected weapon color and save the weapon data
        self.selected_weapon_color = warna.split(": ", 1)[-1]  # Extract the color name
        self.save_new_weapon_data()
    def save_new_weapon_data(self):
        # Dapatkan nomor urut terbaru
        new_id = len(self.weapon_data_list) + 1

        # Dapatkan ID jenis dan warna dari weapon_type dan weapon_color
        id_jenis = self.weapon_types.index(self.selected_weapon_type) + 1
        id_warna = self.weapon_colors.index(self.selected_weapon_color) + 1

        # Format data senjata dengan format yang diinginkan
        weapon_entry = f"{new_id}: ['{self.weapon_name}', '{id_jenis}', '{id_warna}']"

        # Tambahkan entry ke daftar dan simpan ke file
        self.weapon_data_list.append(weapon_entry)
        self.save_weapon_data()
        messagebox.showinfo("Success", f"Senjata '{self.weapon_name}' berhasil disimpan.")
        self.page2()
    
    def select_tab(self, notebook, tab_name):
        # Switch to the specified tab
        for i in range(notebook.index("end")):
            if notebook.tab(i, "text") == tab_name:
                notebook.select(i)
                break
        
        # If we found the Notebook, proceed to select the tab
        if notebook:
            self.load_weapon_data()
            for index in range(notebook.index("end")):
                self.load_weapon_data()
                if notebook.tab(index, "text") == tab_name:
                    self.load_weapon_data()
                    notebook.select(index)
                    break
        else:
            tk.messagebox.showerror("Error", "Notebook widget not found.")

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
            tk.Label(scrollable_frame, text=f"ID Transaksi: {transaction['id_transaksi']}, Senjata: {transaction['id_senjata']}, "
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
        tk.Button(self, text="Simpan", command=self.page7, bg="#FEAE35", font=self.font_style_large).pack(pady=5)
        tk.Button(self, text="Kembali", command=self.page2, bg="#FEAE35", font=self.font_style_large).pack(pady=10)

    def tembak(self):
        self.shot_count += 1
        self.shot_label.config(text=f"Peluru Ditembak: {self.shot_count}")

    def page7(self):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Hasil Latihan", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10)

        # Generate transaction result
        transaction_id = len(self.transaction_history) + 1
        id_senjata = self.selected_weapon_type.split(":")[0].strip()  # Extract only the ID part from selected_weapon_type
        current_time = datetime.datetime.now().strftime("%Y-%m-%d")

        # Append transaction data to history
        transaction = {
            "id_transaksi": transaction_id,
            "id_senjata": id_senjata,
            "peluru": self.shot_count,
            "waktu": current_time
        }
        self.transaction_history.append(transaction)
        self.save_data()  # Save to data.json

        # Display transaction details
        tk.Label(self, text=f"ID Transaksi: {transaction['id_transaksi']}", font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)
        tk.Label(self, text=f"ID Senjata: {transaction['id_senjata']}", font=self.font_style_medium, bg="#404B6B", fg="white").pack(pady=5)
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
            self.save_jenis_data()  # Save to jenis.txt
            self.page2()  # Refresh page to show the new entry

    def save_jenis_data(self):
    # Save the updated list to jenis.txt
        try:
            with open("jenis.txt", "w") as file:
                for index, jenis in enumerate(self.weapon_types, start=1):  # Mulai penomoran dari 1
                    # Pastikan jenis hanya mengambil nama senjata tanpa angka atau tanda tambahan
                    if ": " in jenis:
                        jenis = jenis.split(": ", 1)[-1].strip()  # Hapus angka dan ': '
                    file.write(f"{index} => {jenis}\n")  # Tambahkan angka dengan format konsisten
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File jenis.txt not found.")


    

    def hapus_jenis(self, jenis):
        if jenis in self.weapon_types:
            self.weapon_types.remove(jenis)
            self.save_jenis_data()  # Save changes to jenis.txt
            self.page2()  # Refresh page to update the display

    def tambah_warna(self):
        warna_baru = simpledialog.askstring("Tambah Warna Senjata", "Masukkan warna senjata:")
        if warna_baru:
            self.weapon_colors.append(warna_baru)
            self.save_warna_data()  # Save to warna.txt
            self.page2()  # Refresh page to show the new entry

    def hapus_warna(self, warna):
        if warna in self.weapon_colors:
            self.weapon_colors.remove(warna)
            self.save_warna_data()  # Save changes to warna.txt
            self.page2()  # Refresh page to update the display

    def load_warna_data(self):
        # Load weapon colors from warna.txt into a dictionary
        try:
            self.weapon_colors = []
            with open("warna.txt", "r") as file:
                for line in file:
                    id, name = line.strip().split(" => ")
                    self.warna_map[id] = name
                    self.weapon_colors.append(f'{id}: {name}')
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File warna.txt not found.")

    def save_warna_data(self):
        try:
            with open("warna.txt", "w") as file:
                for index, warna in enumerate(self.weapon_colors, start=1):  # Mulai penomoran dari 1
                    if ": " in warna:
                        warna = warna.split(": ", 1)[-1].strip()  # Hapus angka dan ': '
                    file.write(f"{index} => {warna}\n")  # Tambahkan angka dengan format konsisten
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File warna.txt not found.")
    

    def save_data(self):
        data = {
            "transaction_history": self.transaction_history,
            "weapon_types": self.weapon_names,
            "weapon_colors": self.weapon_colors
        }
        with open("data.json", "w") as file:
            json.dump(data, file)
            
    def load_weapon_data(self):
        self.weapon_id_map = {}
        self.weapon_data_list = []
        try:
            with open("senjata.txt", "r") as file:
                for line in file:
                    # Pisahkan id senjata dari informasi lainnya
                    weapon_id, rest = line.strip().split(" => ")
                    # Pisahkan informasi senjata menjadi bagian-bagian
                    weapon_info = rest.split(";")
                    self.weapon_id_map[weapon_id] = weapon_info  # Store ID and info mapping
                    self.weapon_data_list.append(f"{weapon_id}: {weapon_info}")  # Store full info for display
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File senjata.txt not found.")
    def load_data(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                self.transaction_history = data.get("transaction_history", [])
                self.weapon_types = data.get("weapon_types", [])
                self.weapon_names = data.get("weapon_names", [])
                self.weapon_colors = data.get("weapon_colors", [])
        except FileNotFoundError:
            self.transaction_history = []
            self.weapon_types = []
            self.weapon_colors = []
        except json.JSONDecodeError:
            print("Error decoding file JSON.")
            self.transaction_history = []
            self.weapon_types = []
            self.weapon_colors = []
    def load_jenis_data(self):
        # Load weapon types from jenis.txt into a dictionary
        try:
            self.weapon_types = []
            with open("jenis.txt", "r") as file:
                for line in file:
                    id, name = line.strip().split(" => ")
                    self.jenis_map[id] = name
                    self.weapon_types.append(f'{id}: {name}')
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File jenis.txt not found.")
    def tambah_data_senjata(self):
        # Popup for weapon creation
        popup = tk.Toplevel(self)
        popup.geometry("300x200")
        popup.configure(bg="#FEAE35")
        popup.title("Buat Senjata Baru")

        tk.Label(popup, text="BUAT SENJATA BARU", font=self.font_style_medium, bg="#FEAE35", fg="black").pack(pady=5)

        # Weapon Name Entry
        tk.Label(popup, text="Masukkan Nama Senjata", bg="#FEAE35").pack()
        name_entry = tk.Entry(popup)
        name_entry.pack()

        # Weapon Type Dropdown
        tk.Label(popup, text="Pilih Jenis Senjata", bg="#FEAE35").pack()
        weapon_type_var = tk.StringVar(popup)
        weapon_type_dropdown = ttk.Combobox(popup, textvariable=weapon_type_var, values=self.weapon_types, state="readonly")
        weapon_type_dropdown.pack()

        # Weapon Color Dropdown
        tk.Label(popup, text="Pilih Warna Senjata", bg="#FEAE35").pack()
        weapon_color_var = tk.StringVar(popup)
        weapon_color_dropdown = ttk.Combobox(popup, textvariable=weapon_color_var, values=self.weapon_colors, state="readonly")
        weapon_color_dropdown.pack()

        # OK and Cancel Buttons
        button_frame = tk.Frame(popup, bg="#FEAE35")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="OK", command=lambda: self.create_weapon(name_entry.get(), weapon_type_var.get(), weapon_color_var.get(), popup), bg="white").pack(side="left", padx=5)
        tk.Button(button_frame, text="CANCEL", command=popup.destroy, bg="white").pack(side="left", padx=5)
    def create_weapon(self, name, weapon_type, weapon_color, popup):
        if not name or not weapon_type or not weapon_color:
            messagebox.showwarning("Warning", "Lengkapi semua data senjata.")
            return
        popup.destroy()
        self.weapon_name = name
        self.selected_weapon_type = weapon_type
        self.selected_weapon_color = weapon_color
        self.save_new_weapon_data()
    def edit_weapon_name(self):
        # Step 2: Show popup to edit the weapon name
        new_name = simpledialog.askstring("Edit Nama Senjata", "Ubah nama senjata:", initialvalue=self.weapon_name)
        if new_name:
            self.weapon_name = new_name
            self.data_senjata_label.config(text=f"NAMA SENJATA: {self.weapon_name}")
    def save_weapon_data(self):
        # Save weapon data to senjata.txt
        try:
            with open("senjata.txt", "w") as file:
                for index,item in enumerate(self.weapon_data_list, start=1):
                    item_list = item.split(': ')
                    item_list = ast.literal_eval(item_list[1])
                    file.write(f"{index} => {item_list[0]};{item_list[1]};{item_list[2]}\n")
        except FileNotFoundError:
            tk.messagebox.showerror("Error", "File senjata.txt not found.")

    def select_weapon(self, weapon):
        # Extract the weapon details
        weapon_parts = weapon.split(": ")
        weapon_list = ast.literal_eval(weapon_parts[1])  # Remove ID and take name
        # print('wp=',weapon_list)
        weapon_name = weapon_list[0]
        weapon_type = weapon_list[1]
        weapon_color = weapon_list[2]
        self.selected_weapon_color = weapon_color
        self.selected_weapon_type = weapon_name
        

        # Show the selected weapon details on a new page
        self.display_selected_weapon(weapon_name, weapon_type, weapon_color)
        # Tambahkan fungsi popup untuk tombol "SORTIR"

    def sort_transactions(self):
        # Create a top-level window for sort options
        self.sort_popup = tk.Toplevel(self)
        self.sort_popup.geometry("400x400")
        self.sort_popup.title("Opsi Sortir")
        self.sort_popup.configure(bg="#F3E8C4")

        # Frame to display sorted results (headers will be added only after sorting)
        self.sorted_history_frame = tk.Frame(self.sort_popup, bg="#F3E8C4")
        self.sorted_history_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Function to display headers right above the data
        def display_headers(option):
            # Clear existing headers
            for widget in self.sorted_history_frame.winfo_children():
                widget.destroy()

            # Add headers based on the sorting option selected
            headers_frame = tk.Frame(self.sorted_history_frame, bg="#F3E8C4")
            headers_frame.pack(pady=5)
            
            tk.Label(headers_frame, text="DATA SENJATA", font=self.font_style_medium, bg="#F3E8C4", width=15).pack(side="left", padx=5)
            tk.Label(headers_frame, text="PELURU", font=self.font_style_medium, bg="#F3E8C4", width=10).pack(side="left", padx=5)
            
            # Conditionally add "WAKTU" header if it’s part of the data being displayed
            if option == "all_history" or option == "last_three":
                tk.Label(headers_frame, text="WAKTU", font=self.font_style_medium, bg="#F3E8C4", width=20).pack(side="left", padx=5)

        # Function to display sorted history below headers
        def display_sorted_history(sorted_history, option):
            display_headers(option)  # Display headers right before showing sorted data

            # Display sorted results based on the selected option
            for transaction in sorted_history:
                result_frame = tk.Frame(self.sorted_history_frame, bg="#F3E8C4")
                result_frame.pack(pady=2)

                weapon_id = transaction["id_senjata"]
                peluru = transaction["peluru"]
                waktu = transaction["waktu"]

                tk.Label(result_frame, text=weapon_id, font=self.font_style_medium, bg="#FEAE35", width=15).pack(side="left", padx=5)
                tk.Label(result_frame, text=str(peluru), font=self.font_style_medium, bg="#FEAE35", width=10).pack(side="left", padx=5)
                if option == "all_history" or option == "last_three":
                    tk.Label(result_frame, text=waktu, font=self.font_style_medium, bg="#FEAE35", width=20).pack(side="left", padx=5)

        # Function to apply sorting based on selected option
        def apply_sorting(option):
            if option == "last_three":
                sorted_history = self.transaction_history[-3:]
            elif option == "most_used":
                weapon_usage = {}
                for transaction in self.transaction_history:
                    weapon_name = transaction["id_senjata"]
                    weapon_usage[weapon_name] = weapon_usage.get(weapon_name, 0) + transaction["peluru"]
                most_used_weapon = max(weapon_usage, key=weapon_usage.get)
                sorted_history = [{"id_senjata": most_used_weapon, "peluru": weapon_usage[most_used_weapon], "waktu": "N/A"}]
            elif option == "least_used":
                weapon_usage = {}
                for transaction in self.transaction_history:
                    weapon_name = transaction["id_senjata"]
                    weapon_usage[weapon_name] = weapon_usage.get(weapon_name, 0) + transaction["peluru"]
                least_used_weapon = min((k for k in weapon_usage if weapon_usage[k] > 0), key=weapon_usage.get, default=None)
                sorted_history = [{"id_senjata": least_used_weapon, "peluru": weapon_usage[least_used_weapon], "waktu": "N/A"}] if least_used_weapon else []
            elif option == "never_used":
                used_weapons = {transaction["id_senjata"] for transaction in self.transaction_history}
                all_weapons = {weapon.split(":")[1].strip().split(";")[0] for weapon in self.weapon_data_list}
                never_used_weapons = list(all_weapons - used_weapons)
                sorted_history = [{"id_senjata": weapon_name, "peluru": 0, "waktu": "N/A"} for weapon_name in never_used_weapons]
            else:  # option == "all_history"
                sorted_history = self.transaction_history

            # Pass sorted history and the sorting option to display_sorted_history
            display_sorted_history(sorted_history, option)

        # Function to sort by date range
        def sort_by_date():
            # Create a new popup for date range selection
            date_popup = tk.Toplevel(self.sort_popup)
            date_popup.geometry("300x200")
            date_popup.title("Pilih Rentang Tanggal")
            date_popup.configure(bg="#F3E8C4")

            tk.Label(date_popup, text="Pilih Tanggal Mulai:", bg="#F3E8C4").pack(pady=5)
            start_date_entry = DateEntry(date_popup, width=12, background='darkblue', foreground='white', borderwidth=2)
            start_date_entry.pack(pady=5)

            tk.Label(date_popup, text="Pilih Tanggal Akhir:", bg="#F3E8C4").pack(pady=5)
            end_date_entry = DateEntry(date_popup, width=12, background='darkblue', foreground='white', borderwidth=2)
            end_date_entry.pack(pady=5)

            def filter_by_date():
                start_date = datetime.datetime.strptime(start_date_entry.get(), "%m/%d/%y")
                end_date = datetime.datetime.strptime(end_date_entry.get(), "%m/%d/%y")

                filtered_history = [
                    transaction for transaction in self.transaction_history
                    if start_date <= datetime.datetime.strptime(transaction["waktu"], "%Y-%m-%d %H:%M:%S") <= end_date
                ]
                display_sorted_history(filtered_history, "date_range")
                date_popup.destroy()

            tk.Button(date_popup, text="Terapkan", command=filter_by_date, bg="#FEAE35").pack(pady=10)
            tk.Button(date_popup, text="Batal", command=date_popup.destroy, bg="#FEAE35").pack(pady=5)

        # Sort option buttons
        tk.Button(self.sort_popup, text="3 LATIHAN TERAKHIR", command=lambda: apply_sorting("last_three"), bg="#FEAE35", font=self.font_style_medium).pack(pady=5)
        tk.Button(self.sort_popup, text="SENJATA YANG PALING BANYAK DIGUNAKAN", command=lambda: apply_sorting("most_used"), bg="#FEAE35", font=self.font_style_medium).pack(pady=5)
        tk.Button(self.sort_popup, text="SENJATA YANG PALING SEDIKIT DIGUNAKAN", command=lambda: apply_sorting("least_used"), bg="#FEAE35", font=self.font_style_medium).pack(pady=5)
        tk.Button(self.sort_popup, text="SENJATA YANG TIDAK PERNAH DIGUNAKAN", command=lambda: apply_sorting("never_used"), bg="#FEAE35", font=self.font_style_medium).pack(pady=5)
        tk.Button(self.sort_popup, text="TAMPILKAN SEMUA SEJARAH", command=lambda: apply_sorting("all_history"), bg="#FEAE35", font=self.font_style_medium).pack(pady=5)
        tk.Button(self.sort_popup, text="BERDASARKAN TANGGAL", command=sort_by_date, bg="#FEAE35", font=self.font_style_medium).pack(pady=5)

        # Frame for displaying the sorted results under the options in the top-level window
        self.sorted_history_frame = tk.Frame(self.sort_popup, bg="#F3E8C4")
        self.sorted_history_frame.pack(fill="both", expand=True, padx=10, pady=10)




    # Fungsi untuk memperbarui tampilan tab "Hasil Latihan" dengan data yang diurutkan
    def display_sorted_history(self, sorted_history):
        # Bersihkan isi frame4 sebelum menambahkan data yang baru
        for widget in self.frame4.winfo_children():
            widget.destroy()
        
        # Menampilkan ulang title dan headers
        tk.Label(self.frame4, text="HASIL LATIHAN", font=self.font_style_large, bg="#404B6B", fg="white").pack(pady=10, anchor="center")
        headers_frame = tk.Frame(self.frame4, bg="#404B6B")
        headers_frame.pack(pady=5, anchor="center")
        tk.Label(headers_frame, text="DATA SENJATA", font=self.font_style_medium, bg="#404B6B", fg="white", width=15).grid(row=0, column=0, padx=5, pady=5)
        tk.Label(headers_frame, text="PELURU", font=self.font_style_medium, bg="#404B6B", fg="white", width=10).grid(row=0, column=1, padx=5, pady=5)
        tk.Label(headers_frame, text="WAKTU", font=self.font_style_medium, bg="#404B6B", fg="white", width=20).grid(row=0, column=2, padx=5, pady=5)
        tk.Label(headers_frame, text="", font=self.font_style_medium, bg="#404B6B", fg="white", width=10).grid(row=0, column=3, padx=5, pady=5)

        # Menampilkan data yang telah disortir
        for index, transaction in enumerate(sorted_history):
            transaction_frame = tk.Frame(self.frame4, bg="#404B6B")
            transaction_frame.pack(anchor="center", pady=2)
            
            weapon_id = transaction["id_senjata"]
            peluru = transaction["peluru"]
            waktu = transaction["waktu"]
            
            tk.Label(transaction_frame, text=weapon_id, font=self.font_style_medium, bg="#FEAE35", fg="black", width=15).grid(row=0, column=0, padx=5, pady=5)
            tk.Label(transaction_frame, text=str(peluru), font=self.font_style_medium, bg="#FEAE35", fg="black", width=10).grid(row=0, column=1, padx=5, pady=5)
            tk.Label(transaction_frame, text=waktu, font=self.font_style_medium, bg="#FEAE35", fg="black", width=20).grid(row=0, column=2, padx=5, pady=5)
            tk.Button(transaction_frame, text="HAPUS", command=lambda t=transaction: self.delete_transaction(t), bg="#FEAE35", font=self.font_style_medium, width=10).grid(row=0, column=3, padx=5, pady=5)

if __name__ == "__main__":
    app = JGWApp()
    app.mainloop()
