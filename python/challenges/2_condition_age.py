# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna

usia = int(input("Masikkan uisa Anda: "))

# 2. TODO Tentukan kategori berdasarkan usia

ket = ""
if usia <= 18:
    ket = "Remaja"
elif usia <= 40:
    ket = "Dewasa"
else:
    ket = "Tua"

print(ket)

umur = int(input("masukkan usia anda"))

keterangan = ""
if umur <= 20:
    ket = "remaja"
elif umur <= 30:
    ket = "dewasa"
else:
    ket = "tua"
    