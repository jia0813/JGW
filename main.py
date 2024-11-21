# Fungsi untuk membaca dictionary dari file
def read_dictionary_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = [line.strip() for line in file.readlines()]
            dictionary = {}
            for line in data:
                items = line.split('=>')
                if len(items) >= 2:
                    key = items[0].strip()
                    value = items[1].strip()
                    dictionary[key] = value
            return dictionary
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return {}

# Fungsi untuk menyimpan dictionary ke dalam file
def save_to_file(file_name, data_dict):
    with open(file_name, 'w') as file:
        for key, value in data_dict.items():
            file.write(f"{key} => {value}\n")

# Fungsi untuk menambah data ke dictionary dan file
def tambah_data(data_dict, file_name, value):
    new_key = str(len(data_dict) + 1)  # Menambahkan key baru secara otomatis
    data_dict[new_key] = value
    save_to_file(file_name, data_dict)
    return data_dict

# Fungsi untuk menghapus data berdasarkan key
def hapus_data(data_dict, file_name, key):
    if str(key) in data_dict:
        del data_dict[str(key)]
        save_to_file(file_name, data_dict)
    else:
        print(f"Key {key} tidak ditemukan!")
    return data_dict

# Fungsi untuk membuat senjata baru
def buat_senjata(data_senjata, data_jenis, data_warna):
    # Menampilkan daftar jenis senjata
    print("\nDaftar Jenis Senjata:")
    for key, value in data_jenis.items():
        print(f"{key}: {value}")
    
    # Memilih jenis senjata berdasarkan ID
    jenis_id = input("Masukkan ID jenis senjata: ")

    # Menampilkan daftar warna senjata
    print("\nDaftar Warna Senjata:")
    for key, value in data_warna.items():
        print(f"{key}: {value}")
    
    # Memilih warna senjata berdasarkan ID
    warna_id = input("Masukkan ID warna senjata: ")

    # Memasukkan nama senjata
    nama = input("Masukkan nama senjata: ")

    # Menambahkan senjata baru dengan format 'Nama Senjata;ID Jenis;ID Warna'
    new_id = str(len(data_senjata) + 1)
    data_senjata[new_id] = f"{nama};{jenis_id};{warna_id}"

    # Menyimpan data senjata ke file 'senjata.txt'
    save_to_file('senjata.txt', data_senjata)
    
    # Menampilkan konfirmasi pembuatan senjata
    print(f"\nAnda membuat senjata: {nama};{jenis_id};{warna_id}")

    return data_senjata, data_jenis, data_warna

# Membaca data dari file saat aplikasi dimulai
data_senjata = read_dictionary_from_file('senjata.txt')
data_jenis = read_dictionary_from_file('jenis.txt')
data_warna = read_dictionary_from_file('warna.txt')

# Menjalankan menu aplikasi
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
        data_senjata, data_jenis, data_warna = buat_senjata(data_senjata, data_jenis, data_warna)
    elif pilihan == '10':
        print("Keluar dari aplikasi.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
