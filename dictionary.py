def read_dictionary_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = [line.strip() for line in file.readlines()]  # Membaca setiap baris dan membersihkan whitespace
            
            # Membuat dictionary berdasarkan format 'key => value'
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
        return None
