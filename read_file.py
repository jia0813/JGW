from fungsiarray import read_array_from_file
from dictionary import read_dictionary_from_file

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return None

def main():
    while True:
        nama_file = input("Masukkan nama file txt/csv: ")
        isi_file = read_file(nama_file)
        
        print("\nIsi file yang dibaca:")
        print(isi_file)  # Menampilkan isi file

        if isi_file is not None:
            if ',' in isi_file:  # Cek format array
                array = read_array_from_file(nama_file)
                if array is not None:
                    print("\nData yang dibaca adalah Array:")
                    print(array)
            elif '=>' in isi_file:  # Cek format dictionary
                dictionary_data = read_dictionary_from_file(nama_file)
                if dictionary_data is not None:
                    print("\nData yang dibaca adalah Dictionary:")
                    print(dictionary_data)
            else:
                print("Format tidak dikenali.")
        else:
            print(f"File '{nama_file}' tidak ditemukan. Coba lagi.\n")
        
        pilihan = input("\nApakah Anda ingin memasukkan file lain? (y/n): ").lower()
        if pilihan != 'y':
            print("Terima kasih telah menggunakan aplikasi!")
            break

if __name__ == "__main__":
    main()
