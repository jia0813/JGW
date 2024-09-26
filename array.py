def read_array_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read().strip()  # Membersihkan whitespace
            array = data.split(",")  # Pisahkan data berdasarkan koma
            array = [item.strip() for item in array]  # Hapus spasi berlebih
            return array
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return None

def main():
    file_name = "array.txt"  # Nama file yang ingin dibaca
    array_data = read_array_from_file(file_name)  # Baca data dari file

    if array_data is not None:
        print("Data array yang dibaca dari file:")
        print(array_data)  # Menampilkan data array yang sudah dibaca
    else:
        print("Tidak ada data yang bisa dibaca dari file.")

if __name__ == "__main__":
    main()