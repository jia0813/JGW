def baca_file(file_name):
    data = {}
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                data[i] = line.strip()  # Menghapus newline dan spasi ekstra
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return data

def tambah_data(data_dict, value):
    key = len(data_dict) + 1
    data_dict[key] = value
    print(f"{value} telah ditambahkan.")

def hapus_data(data_dict, key):
    if key in data_dict:
        del data_dict[key]
        print(f"Data dengan key {key} telah dihapus.")
    else:
        print("Key tidak ditemukan.")

def buat_senjata():
    print("Pilih nama senjata:")
    for key, value in data_nama.items():
        print(f"{key}. {value}")
    nama_key = int(input("Masukkan nomor nama senjata yang dipilih: "))
    nama = data_nama.get(nama_key, "Senjata tidak valid")

    print("Pilih jenis senjata:")
    for key, value in data_jenis.items():
        print(f"{key}. {value}")
    jenis_key = int(input("Masukkan nomor jenis senjata yang dipilih: "))
    jenis = data_jenis.get(jenis_key, "Jenis tidak valid")

    print("Pilih warna senjata:")
    for key, value in data_warna.items():
        print(f"{key}. {value}")
    warna_key = int(input("Masukkan nomor warna senjata yang dipilih: "))
    warna = data_warna.get(warna_key, "Warna tidak valid")

    print(f"Anda telah memilih nama: {nama}, jenis: {jenis}, warna: {warna}")

# Membaca data dari file
data_senjata = baca_file('senjata.txt')
data_nama = baca_file('nama.txt')
data_jenis = baca_file('jenis.txt')
data_warna = baca_file('warna.txt')

while True:
    print("\nPilih opsi:")
    print("1. Lihat data senjata")
    print("2. Lihat jenis senjata")
    print("3. Lihat warna senjata")
    print("4. Tambah jenis senjata")
    print("5. Tambah warna senjata")
    print("6. Hapus data senjata")
    print("7. Hapus jenis senjata")
    print("8. Hapus warna senjata")
    print("9. Buat senjata")
    print("10. Keluar")

    pilihan = input("Masukkan pilihan (1-10): ")

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
        key = int(input("Masukkan key untuk data senjata yang akan dihapus: "))
        hapus_data(data_senjata, key)
        print(f"Data senjata tersisa: {data_senjata}")
    elif pilihan == '7':
        key = int(input("Masukkan key untuk jenis senjata yang akan dihapus: "))
        hapus_data(data_jenis, key)
        print(f"Jenis senjata tersisa: {data_jenis}")
    elif pilihan == '8':
        key = int(input("Masukkan key untuk warna senjata yang akan dihapus: "))
        hapus_data(data_warna, key)
        print(f"Warna senjata tersisa: {data_warna}")
    elif pilihan == '9':
        buat_senjata()
    elif pilihan == '10':
        print("Keluar dari aplikasi.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
