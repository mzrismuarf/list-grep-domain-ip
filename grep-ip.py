def ambil_ip(file_input, file_output):
    try:
        with open(file_input, 'r') as input_file:
            lines = input_file.readlines()

        ips = [line.split(':')[1].strip() for line in lines]

        with open(file_output, 'w') as output_file:
            for ip in ips:
                output_file.write(f"{ip}\n")

        print(f"IP berhasil diambil. Hasil disimpan di {file_output}")

    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan nama file dan path yang dimasukkan benar.")

if __name__ == "__main__":
    file_input = input("Masukkan List: ")
    file_output = "result-ip.txt"  # Nama file output, bisa diubah sesuai keinginan

    ambil_ip(file_input, file_output)
