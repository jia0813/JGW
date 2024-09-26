mport csv

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
    # Nama file yang ingin dibaca
    input_file = "dictionary.txt"
    
    # Membaca file dictionary
    dictionary_data = read_dictionary_file(input_file)

    if dictionary_data is not None:
        # Mengonversi dictionary ke CSV
        output_file = "dictionary.csv"
        dictionary_to_csv(dictionary_data, output_file)

if _name_ == "_main_":
    main()
