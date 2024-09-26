import csv

def read_array_from_file(file_name):
    """Membaca file array dan mengonversi isinya menjadi list."""
    try:
        with open(file_name, 'r') as file:
            data = file.read().strip()  # Membersihkan whitespace
            array = data.split(",")  # Pisahkan data berdasarkan koma
            array = [item.strip() for item in array]  # Hapus spasi berlebih
            return array
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return None

def array_to_csv(array, output_filename):
    """Mengonversi array ke format CSV dan menyimpannya ke file."""
    try:
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(array)  # Menulis data array ke file CSV
        print(f"Data array berhasil disimpan ke {output_filename}")
    except Exception as e:
        print(f"Gagal menyimpan data ke CSV: {e}")

def main():
    file_name = "array.txt"  # Nama file yang ingin dibaca
    array_data = read_array_from_file(file_name)  # Baca data dari file

    if array_data is not None:
        print("Data array yang dibaca dari file:")
        print(array_data)  # Menampilkan data array yang sudah dibaca

        # Menyimpan data array ke file CSV
        output_file = "array.csv"
        array_to_csv(array_data, output_file)
    else:
        print("Tidak ada data yang bisa dibaca dari file.")

if __name__ == "__main__":
    main()
