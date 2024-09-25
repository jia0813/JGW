import csv

def create_array_file():
    array_data = ["Jia", "Gilang", "Winda"]
    with open("array.txt", "w") as file:
        file.write("\n".join(array_data) + "\n")
    print("File array.txt berhasil dibuat.")

def array_to_csv(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            array_data = [line.strip() for line in file.readlines()]

        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(array_data)
        print(f"File {input_filename} berhasil diubah menjadi {output_filename}")
    except FileNotFoundError:
        print(f"File {input_filename} tidak ditemukan.")
    except Exception as e:
        print(f"Gagal mengubah file: {e}")

if __name__ == "__main__":
    create_array_file()  # Buat file array.txt
    array_to_csv("array.txt", "array.csv")  # Ubah array.txt menjadi array.csv