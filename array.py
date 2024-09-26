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
