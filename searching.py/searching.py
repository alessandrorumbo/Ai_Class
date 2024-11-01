import random

def buat_list_angka():
    # Membuat list dengan 20 angka acak antara 1 hingga 10
    return [random.randint(1, 10) for _ in range(20)]

def cek_angka(input_angka):
    angka_list = buat_list_angka()
    print(f"List angka: {angka_list}")
    
    if input_angka % 2 == 0:  # Cek apakah angka genap
        indeks = [index for index, value in enumerate(angka_list) if value == input_angka]
        if indeks:
            print(f"Angka {input_angka} ditemukan di indeks: {indeks}")
        else:
            print(f"Angka {input_angka} tidak ditemukan dalam list.")
    else:
        print("Input angka adalah ganjil. Tidak ada output.")

# Contoh penggunaan
angka_input = int(input("Masukkan angka (1-10): "))
cek_angka(angka_input)
