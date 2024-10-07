# main.py
from lihatdata import baca_file_lihatdata
from jenis import baca_file_jenis
from warna import baca_file_warna

# Fungsi untuk membaca file data senjata
def baca_file_lihatdata(filename):
    data_senjata = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                data_senjata[int(key)] = value
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
    print(f"Data senjata yang dibaca: {data_senjata}") 
    return data_senjata

# Fungsi untuk membaca jenis senjata
def baca_file_jenis(filename):
    data_jenis = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ', 1)
                data_jenis[int(key)] = value
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
    except ValueError:
        print(f"Format data tidak valid di dalam file {filename}.")
    print(f"Data senjata yang dibaca: {data_jenis}") 
    return data_jenis

# Fungsi untuk membaca warna senjata
def baca_file_warna(filename):
    data_warna = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ', 1)
                data_warna[int(key)] = value
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
    except ValueError:
        print(f"Format data tidak valid di dalam file {filename}.")
    print(f"Data warna yang dibaca: {data_warna}") 
    return data_warna

# Fungsi untuk menambah data ke dictionary
def tambah_data(dictionary, value):
    if len(dictionary) > 0:
        key = max(dictionary.keys()) + 1  # Key baru adalah key tertinggi + 1
    else:
        key = 1  # Jika dictionary kosong, key dimulai dari 1
    dictionary[key] = value
    print(f"Data berhasil ditambahkan: {key}: {value}")

# Fungsi untuk menghapus data dari dictionary
def hapus_data(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        print(f"Data dengan key {key} berhasil dihapus.")
    else:
        print(f"Key {key} tidak ditemukan di dictionary.")

# Fungsi untuk membuat senjata
def buat_senjata():
    id_senjata = input("Masukkan ID senjata baru: ")

    # Menampilkan pilihan jenis senjata
    print("\nPilih jenis senjata:")
    for id_jenis, nama_jenis in data_jenis.items():
        print(f"{id_jenis}: {nama_jenis}")

    jenis_id = int(input("Masukkan ID jenis senjata: "))
    if jenis_id not in data_jenis:
        print("ID jenis senjata tidak valid.")
        return

    # Menampilkan pilihan warna senjata
    print("\nPilih warna senjata:")
    for id_warna, nama_warna in data_warna.items():
        print(f"{id_warna}: {nama_warna}")

    warna_id = int(input("Masukkan ID warna senjata: "))
    if warna_id not in data_warna:
        print("ID warna senjata tidak valid.")
        return

    # Simpan data senjata ke dalam dictionary
    data_senjata[int(id_senjata)] = f"{data_jenis[jenis_id]}; {data_warna[warna_id]}"
    print(f"Selamat! Anda telah membuat senjata {data_jenis[jenis_id]} berwarna {data_warna[warna_id]}.")

# Fungsi untuk melanjutkan atau keluar
def lanjutkan_atau_keluar():
    pilihan = input("Apakah Anda ingin melanjutkan? (y/n): ")
    return pilihan.lower() == 'y'

# Fungsi utama dengan loop
def main():
    global data_senjata, data_jenis, data_warna  # Menggunakan variabel global

    data_senjata = baca_file_lihatdata('lihatdata.txt')
    data_jenis = baca_file_jenis('jenis.txt')
    data_warna = baca_file_warna('warna.txt')

    while True:
        print("\nPilih opsi:")
        print("1. Lihat data senjata")
        print("2. Lihat jenis senjata")
        print("3. Lihat warna senjata") 
        print("4. Tambah data jenis senjata") 
        print("5. Tambah data warna senjata") 
        print("6. Hapus data jenis senjata") 
        print("7. Hapus data warna senjata")
        print("8. Buat senjata")
        print("9. Keluar")

        pilihan = input("Masukkan pilihan (1-9): ")

        if pilihan == '1':
            print("ID_Data Senjata:", data_senjata)
        elif pilihan == '2':
            print("ID_Jenis Senjata:", data_jenis)
        elif pilihan == '3':
            print("ID_Warna Senjata:", data_warna)
        elif pilihan == '4': 
            value = input("Masukkan jenis senjata baru: ")
            tambah_data(data_jenis, value)
        elif pilihan == '5':
            value = input("Masukkan warna senjata baru: ")
            tambah_data(data_warna, value)
        elif pilihan == '6':
            key = int(input("Masukkan key untuk jenis senjata yang akan dihapus: "))
            hapus_data(data_jenis, key)
            print(f"Jenis senjata tersisa: {data_jenis}")
        elif pilihan == '7':
            key = int(input("Masukkan key untuk warna senjata yang akan dihapus: "))
            hapus_data(data_warna, key)
            print(f"Warna senjata tersisa: {data_warna}")
        elif pilihan == '8':
            buat_senjata()
        elif pilihan == '9':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

        # Tanyakan apakah ingin lanjut atau keluar
        if not lanjutkan_atau_keluar():
            break

if __name__ == "__main__":
    main()