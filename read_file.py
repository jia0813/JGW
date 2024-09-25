def read_file(nama_file):
    try:
        with open(nama_file, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return None

def main():
    while True:
        nama_file = input("Masukkan nama file txt/csv: ")
        isi_file = read_file(nama_file)
        
        if isi_file is not None:
            print("\nIsi file:")
            print(isi_file)
            
            if ',' in isi_file:  # Cek format array
                array = isi_file.split(',')
                print("\nData yang dibaca adalah Array:")
                print([item.strip() for item in array])
            elif ';' in isi_file:  # Cek format dictionary
                print("\nData yang dibaca adalah Dictionary:")
                print(isi_file)
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