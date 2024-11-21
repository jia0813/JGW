import os

def baca_file(file_name):
    data = {}
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                data[i] = line.strip()
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    return data

def tulis_file(file_name, data_dict):
    with open(file_name, 'w') as file:
        for key, value in data_dict.items():
            file.write(f"{value}\n")

def tambah_data(data_dict, file_name, value):
    # Cek apakah data sudah ada
    if value.lower() in [v.lower() for v in data_dict.values()]:
        print(f"{value} sudah ada di daftar.")
        return data_dict

    key = len(data_dict) + 1
    data_dict[key] = value
    tulis_file(file_name, data_dict)
    print(f"{value} telah ditambahkan.")
    return data_dict

def hapus_data(data_dict, file_name, key):
    if key in data_dict:
        del data_dict[key]
        data_dict = {i+1: value for i, value in enumerate(data_dict.values())}
        tulis_file(file_name, data_dict)
        print(f"Data dengan key {key} telah dihapus.")
    else:
        print("Key tidak ditemukan.")
    return data_dict

def buat_senjata(data_senjata, data_nama, data_jenis, data_warna):
    print("Daftar Nama Senjata:")
    for key, value in data_nama.items():
        print(f"{key}. {value}")
    
    print("\nDaftar Jenis Senjata:")
    for key, value in data_jenis.items():
        print(f"{key}. {value}")
    
    print("\nDaftar Warna Senjata:")
    for key, value in data_warna.items():
        print(f"{key}. {value}")

    # Tambah nama, jenis, warna baru jika belum ada
    nama_input = input("\nMasukkan nama senjata: ")
    if nama_input.lower() not in [v.lower() for v in data_nama.values()]:
        data_nama = tambah_data(data_nama, 'nama.txt', nama_input)

    jenis_input = input("Masukkan jenis senjata: ")
    if jenis_input.lower() not in [v.lower() for v in data_jenis.values()]:
        data_jenis = tambah_data(data_jenis, 'jenis.txt', jenis_input)

    warna_input = input("Masukkan warna senjata: ")
    if warna_input.lower() not in [v.lower() for v in data_warna.values()]:
        data_warna = tambah_data(data_warna, 'warna.txt', warna_input)

    # Cari ID untuk nama, jenis, dan warna
    nama_key = next((k for k, v in data_nama.items() if v.lower() == nama_input.lower()), None)
    jenis_key = next((k for k, v in data_jenis.items() if v.lower() == jenis_input.lower()), None)
    warna_key = next((k for k, v in data_warna.items() if v.lower() == warna_input.lower()), None)

    # Tambahkan senjata baru ke file senjata.txt
    with open('senjata.txt', 'a') as file:
        new_id = len(data_senjata) + 1
        file.write(f"{new_id}: {nama_input};{jenis_key};{warna_key}\n")

    print(f"\nAnda telah membuat senjata:")
    print(f"Nama: {nama_input}")
    print(f"Jenis: {jenis_input}")
    print(f"Warna: {warna_input}")

    return data_nama, data_jenis, data_warna

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
        print("Data Senjata:", data_senjata)
    elif pilihan == '2':
        print("Jenis Senjata:", data_jenis)
    elif pilihan == '3':
        print("Warna Senjata:", data_warna)
    elif pilihan == '4':
        value = input("Masukkan jenis senjata baru: ")
        data_jenis = tambah_data(data_jenis, 'jenis.txt', value)
    elif pilihan == '5':
        value = input("Masukkan warna senjata baru: ")
        data_warna = tambah_data(data_warna, 'warna.txt', value)
    elif pilihan == '6':
        key = int(input("Masukkan key untuk data senjata yang akan dihapus: "))
        data_senjata = hapus_data(data_senjata, 'senjata.txt', key)
    elif pilihan == '7':
        key = int(input("Masukkan key untuk jenis senjata yang akan dihapus: "))
        data_jenis = hapus_data(data_jenis, 'jenis.txt', key)
    elif pilihan == '8':
        key = int(input("Masukkan key untuk warna senjata yang akan dihapus: "))
        data_warna = hapus_data(data_warna, 'warna.txt', key)
    elif pilihan == '9':
        data_nama, data_jenis, data_warna = buat_senjata(data_senjata, data_nama, data_jenis, data_warna)
        # Update data senjata setelah buat senjata
        data_senjata = baca_file('senjata.txt')
    elif pilihan == '10':
        print("Keluar dari aplikasi.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
