# Fungsi untuk membaca file warna_senjata (data.txt)
def baca_warna_senjata(filename):
    warna_senjata = {}
    with open(filename, 'r') as file:
        for line in file:
            print(f"Reading line: {line}")  # Debugging line
            key, value = line.strip().split(': ')
            warna_senjata[int(key)] = value
    return warna_senjata