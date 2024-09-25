import csv

def create_dictionary_file():
    # Buat dictionary data
    dictionary_data = {
        "Nama1": "Jia",
        "Nama2": "Gilang",
        "Nama3": "Winda"
    }
    
    # Simpan dictionary ke file
    with open("dictionary.txt", "w") as file:
        # Format key:value;key:value;...
        file.write(";".join(f"{key}:{value}" for key, value in dictionary_data.items()))
    print("File dictionary.txt berhasil dibuat.")

def dictionary_to_csv(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            data = file.read()
            # Membaca file dengan format key:value;key:value;...
            dictionary = dict(item.split(':') for item in data.split(';') if ':' in item)

        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=dictionary.keys())
            writer.writeheader()
            writer.writerow(dictionary)

        print(f"File {input_filename} berhasil diubah menjadi {output_filename}")
    except FileNotFoundError:
        print(f"File {input_filename} tidak ditemukan.")
    except Exception as e:
        print(f"Gagal mengubah file: {e}")

if __name__ == "__main__":
    create_dictionary_file()  # Buat file dictionary.txt
    dictionary_to_csv("dictionary.txt", "dictionary.csv")  # Ubah dictionary.txt menjadi dictionary.csv