from jenissenjata import baca_jenis_senjata
from warnasenjata import baca_warna_senjata

# Fungsi untuk membaca file warna_senjata (data.txt)
def baca_warna_senjata(filename):
    warna_senjata = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            warna_senjata[int(key)] = value
    return warna_senjata

# Fungsi untuk membaca file jenis_senjata (data1.txt)
def baca_jenis_senjata(filename):
    jenis_senjata = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            jenis_senjata[int(key)] = value
    return jenis_senjata

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

# Fungsi untuk menampilkan opsi lanjut atau keluar
def lanjutkan_atau_keluar():
    while True:
        pilihan = input("Apakah ingin kembali ke menu utama atau keluar? (menu/keluar): ").lower()
        if pilihan == "menu":
            return True
        elif pilihan == "keluar":
            print("Keluar dari aplikasi.")
            return False
        else:
            print("Pilihan tidak valid, coba lagi.")

# Fungsi utama dengan loop
def main():
    warna_senjata = baca_warna_senjata('data.txt')
    jenis_senjata = baca_jenis_senjata('data1.txt')

    while True:
        print("\nPilih opsi:")
        print("1. Tampilkan warna senjata")
        print("2. Tampilkan jenis senjata")
        print("3. Tambah data warna senjata")
        print("4. Tambah data jenis senjata")
        print("5. Hapus data warna senjata")
        print("6. Hapus data jenis senjata")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan (1-7): ")

        if pilihan == '1':
            print("Warna senjata:", warna_senjata)
        elif pilihan == '2':
            print("Jenis senjata:", jenis_senjata)
        elif pilihan == '3':
            value = input("Masukkan warna senjata baru: ")
            tambah_data(warna_senjata, value)
        elif pilihan == '4':
            value = input("Masukkan jenis senjata baru: ")
            tambah_data(jenis_senjata, value)
        elif pilihan == '5':
            key = int(input("Masukkan key untuk warna senjata yang akan dihapus: "))
            hapus_data(warna_senjata, key)
            print(f"Warna senjata tersisa: {warna_senjata}")
        elif pilihan == '6':
            key = int(input("Masukkan key untuk jenis senjata yang akan dihapus: "))
            hapus_data(jenis_senjata, key)
            print(f"Jenis senjata tersisa: {jenis_senjata}")
        elif pilihan == '7':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

        # Tanyakan apakah ingin lanjut atau keluar
        if not lanjutkan_atau_keluar():
            break

if __name__ == "__main__":
    main()