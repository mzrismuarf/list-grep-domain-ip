def ambil_domain(file_input, file_output):
    try:
        with open(file_input, 'r') as input_file:
            lines = input_file.readlines()

        # Jika list nya berupa domain:ip
        # Bisa disesuaikan
        domains = [line.split(':')[0].strip() for line in lines]

        with open(file_output, 'w') as output_file:
            for domain in domains:
                output_file.write(f"{domain}\n")

        print(f"Domain berhasil diambil. Hasil disimpan di {file_output}")

    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan nama file dan path yang dimasukkan benar.")


if __name__ == "__main__":
    file_input = input("Masukkan List: ")
    file_output = "result.txt"  # Nama file output, bisa diubah sesuai keinginan

    ambil_domain(file_input, file_output)
