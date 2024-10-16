def baca_file_lihatdata(file_name):
    data = {}
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                data[i] = line.strip()  # Menghapus newline dan spasi ekstra
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return data

def baca_file_nama(file_name):
    data = {}
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                data[i] = line.strip()  # Menghapus newline dan spasi ekstra
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return data

def baca_file_jenis(file_name):
    data = {}
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                data[i] = line.strip()  # Menghapus newline dan spasi ekstra
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return data

def baca_file_warna(file_name):
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
    # Menambahkan data ke dalam dictionary
    key = len(data_dict) + 1
    data_dict[key] = value
    print(f"{value} telah ditambahkan.")

def hapus_data(data_dict, key):
    # Menghapus data berdasarkan key
    if key in data_dict:
        del data_dict[key]
        print(f"Data dengan key {key} telah dihapus.")
    else:
        print("Key tidak ditemukan.")

def buat_senjata():
    # Memilih nama, jenis, dan warna senjata
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

    # Output
    print(f"Anda telah memilih nama: {nama}, jenis: {jenis}, warna: {warna}")

# Membaca data dari file
data_lihatdata = baca_file_lihatdata('lihatdata.txt')
data_nama = baca_file_nama('nama.txt')
data_jenis = baca_file_jenis('jenis.txt')
data_warna = baca_file_warna('warna.txt')

while True:
    print("\nPilih opsi:")
    print("1. Lihat data senjata")
    print("2. Lihat nama senjata")
    print("3. Lihat jenis senjata")
    print("4. Lihat warna senjata") 
    print("5. Tambah data nama senjata")
    print("6. Tambah data jenis senjata") 
    print("7. Tambah data warna senjata") 
    print("8. Hapus data nama senjata")
    print("9. Hapus data jenis senjata") 
    print("10. Hapus data warna senjata")
    print("11. Buat senjata")
    print("12. Keluar")

    pilihan = input("Masukkan pilihan (1-12): ")

    if pilihan == '1':
        print("ID_Data Senjata:", data_lihatdata)
    elif pilihan == '2':
        print("ID_Nama Senjata:", data_nama)
    elif pilihan == '3':
        print("ID_Jenis Senjata:", data_jenis)
    elif pilihan == '4': 
        print("ID_Warna Senjata:", data_warna)
    elif pilihan == '5':
        value = input("Masukkan nama senjata baru: ")
        tambah_data(data_nama, value)
    elif pilihan == '6':
        value = input("Masukkan jenis senjata baru: ")
        tambah_data(data_jenis, value)
    elif pilihan == '7':
        value = input("Masukkan warna senjata baru: ")
        tambah_data(data_warna, value)
    elif pilihan == '8':
        key = int(input("Masukkan key untuk nama senjata yang akan dihapus: "))
        hapus_data(data_nama, key)
        print(f"Jenis senjata tersisa: {data_nama}")
    elif pilihan == '9':
        key = int(input("Masukkan key untuk jenis senjata yang akan dihapus: "))
        hapus_data(data_jenis, key)
        print(f"Jenis senjata tersisa: {data_jenis}")
    elif pilihan == '10':
        key = int(input("Masukkan key untuk warna senjata yang akan dihapus: "))
        hapus_data(data_warna, key)
        print(f"Warna senjata tersisa: {data_warna}")
    elif pilihan == '11':
        buat_senjata()
    elif pilihan == '12':
        print("Keluar dari aplikasi.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
