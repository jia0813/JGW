# Fungsi untuk membaca file jenis_senjata (data1.txt)
def baca_jenis_senjata(filename):
    jenis_senjata = {}
    with open(filename, 'r') as file:
        for line in file:
            print(f"Reading line: {line}")  # Debugging line
            key, value = line.strip().split(': ')
            jenis_senjata[int(key)] = value
    return jenis_senjata