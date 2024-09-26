import csv

def read_array_from_file(file_name):
    """Membaca data dari file array.txt dan mengembalikannya sebagai list."""
    try:
        with open(file_name, 'r') as file:
            data = file.read().strip()  # Membersihkan whitespace
            array = data.split(",")  # Pisahkan data berdasarkan koma
            return [item.strip() for item in array]  # Hapus spasi berlebih
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return None

def read_dictionary_from_file(file_name):
    """Membaca data dari file dictionary.txt dan mengembalikannya sebagai dictionary."""
    try:
        with open(file_name, 'r') as file:
            data = file.read().strip()  # Membersihkan whitespace
            # Membuat dictionary dari data yang dipisahkan oleh ;
            dictionary = dict(item.split(':') for item in data.split(';') if ':' in item)
            return dictionary
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return None

def read_python_file(file_name):
    """Membaca isi file Python dan mengembalikannya sebagai string."""
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
        return None

def main():
    while True:
        choice = input("Pilih file yang ingin dibaca (1: array.txt, 2: dictionary.txt, 3: array.py, 4: dictionary.py, 0: keluar): ")

        if choice == '1':
            # Membaca file array.txt
            array_file = "array.txt"
            array_data = read_array_from_file(array_file)

            if array_data is not None:
                print("Data dari array.txt:")
                print(array_data)

        elif choice == '2':
            # Membaca file dictionary.txt
            dictionary_file = "dictionary.txt"
            dict_data = read_dictionary_from_file(dictionary_file)

            if dict_data is not None:
                print("\nData dari dictionary.txt:")
                print(dict_data)

        elif choice == '3':
            # Membaca file array.py
            array_py_file = "array.py"
            array_py_data = read_python_file(array_py_file)

            if array_py_data is not None:
                print("\nIsi dari array.py:")
                print(array_py_data)

        elif choice == '4':
            # Membaca file dictionary.py
            dictionary_py_file = "dictionary.py"
            dict_py_data = read_python_file(dictionary_py_file)

            if dict_py_data is not None:
                print("\nIsi dari dictionary.py:")
                print(dict_py_data)

        elif choice == '0':
            print("Terima kasih telah menggunakan aplikasi!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if _name_ == "_main_":
    main()
