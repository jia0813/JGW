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

def read_dictionary_file(file_name):
    """Membaca file dictionary dan mengonversi isinya menjadi dictionary."""
    try:
        with open(file_name, 'r') as file:
            # Membaca setiap baris dan menghapus whitespace
            data = [line.strip() for line in file.readlines() if line.strip()]

            # Membuat dictionary dengan key otomatis
            dictionary = {f"Nama{i + 1}": name for i, name in enumerate(data)}
            return dictionary
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return None

def dictionary_to_csv(dictionary, output_filename):
    """Mengonversi dictionary ke format CSV dan menyimpannya ke file."""
    try:
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=dictionary.keys())
            writer.writeheader()
            writer.writerow(dictionary)

        print(f"File dictionary berhasil diubah menjadi {output_filename}")
    except Exception as e:
        print(f"Gagal mengubah file ke CSV: {e}")

def main():
    # Membaca data dari file array
    array_file = "array.txt"  # Nama file array
    array_data = read_array_from_file(array_file)  # Baca data dari file

    if array_data is not None:
        print("Data array yang dibaca dari file:")
        print(array_data)  # Menampilkan data array yang sudah dibaca
    else:
        print("Tidak ada data yang bisa dibaca dari file array.")

    # Membaca data dari file dictionary
    dictionary_file = "dictionary.txt"  # Nama file dictionary
    dictionary_data = read_dictionary_file(dictionary_file)  # Baca data dari file

    if dictionary_data is not None:
        print("Data dictionary yang dibaca dari file:")
        print(dictionary_data)  # Menampilkan data dictionary yang sudah dibaca
        
        # Mengonversi dictionary ke CSV
        output_file = "dictionary.csv"
        dictionary_to_csv(dictionary_data, output_file)
    else:
        print("Tidak ada data yang bisa dibaca dari file dictionary.")

if _name_ == "main":
    main()
