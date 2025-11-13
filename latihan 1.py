# 1. Buat list dengan 5 elemen
A = [15, 30, 45, 60, 75]
print("List A:", A)

# 2. Akses list
print("Elemen ke-3:", A[2])              # 45
print("Elemen ke-2 sampai ke-4:", A[1:4]) # [30, 45, 60]
print("Elemen terakhir:", A[-1])         # 75

# 3. Ubah elemen list
A[3] = 150
print("Setelah ubah elemen ke-4:", A)

A[3:] = [225, 300]
print("Setelah ubah elemen ke-4 sampai akhir:", A)

# 4. Tambah elemen list
B = A[0:2]
print("List B:", B)

B.append("Python")
print("Setelah tambah string:", B)

B.extend([90, 105, 120])
print("Setelah tambah 3 nilai:", B)

C = B + A
print("Gabungan list B dan A:", C)
