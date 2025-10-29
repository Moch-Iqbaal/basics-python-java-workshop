# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna

umur = int(input("masukkan usia anda"))
# 2. TODO Tentukan kategori berdasarkan usia


status = "tua"
if umur <= 12:
    status = "anak"
elif umur <= 17:
    status = "remaja"
elif umur <= 59:
    status = "dewasa"

print(status)