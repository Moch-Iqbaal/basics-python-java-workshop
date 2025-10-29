# 1. Buat list berisi 5 angka
numbers = [10, 25, 7, 40, 15]
print("List awal:", numbers)

# 2. TODO: Tampilkan angka pertama dan terakhir

print("Angka pertama:", numbers[0])
print("Angka terakhir:", numbers[-1])

# 3. TODO: Tambahkan angka baru (apapun) ke akhir list

numbers.append(50)
print("List setelah ditambah:", numbers)

# 4. TODO: Urutkan list secara descending

# 5. Tampilkan hasil akhir
numbers.sort(reverse=True)
print("List urut descending:", numbers)
