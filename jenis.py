def baca_file_jenis(filename):
    data_jenis = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ', 1)
                data_jenis[int(key)] = value
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
    except ValueError:
        print(f"Format data tidak valid di dalam file {filename}.")
    print(f"Data senjata yang dibaca: {data_jenis}") 
    return data_jenis