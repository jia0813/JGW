def baca_file_warna(filename):
    data_warna = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ', 1)
                data_warna[int(key)] = value
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
    except ValueError:
        print(f"Format data tidak valid di dalam file {filename}.")
    print(f"Data warna yang dibaca: {data_warna}") 
    return data_warna