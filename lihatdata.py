def baca_file_lihatdata(filename):
    data_senjata = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                data_senjata[int(key)] = value
    except FileNotFoundError:
        print(f"File {filename} tidak ditemukan.")
    print(f"Data senjata yang dibaca: {data_senjata}") 
    return data_senjata