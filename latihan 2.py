data_mahasiswa = []

while True:
    print("\n=== Input Data Mahasiswa ===")
    nama = input("Nama        : ")
    tugas = float(input("Nilai Tugas : "))
    uts   = float(input("Nilai UTS   : "))
    uas   = float(input("Nilai UAS   : "))

    # Hitung nilai akhir
    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    # Tambahkan ke list utama
    data_mahasiswa.append([nama, tugas, uts, uas, akhir])

    # Tanya user mau lanjut atau tidak
    lanjut = input("Tambah data lagi? (y/t): ")
    if lanjut.lower() == "t":
        break

# Tampilkan hasil data
print("\nDaftar Nilai Mahasiswa")
print("="*65)
print("| No |     Nama     | Tugas |  UTS  |  UAS  |  Akhir |")
print("-"*65)

for i, data in enumerate(data_mahasiswa, start=1):
    print(f"| {i:>2} | {data[0]:<12} | {data[1]:>5.1f} | {data[2]:>5.1f} | {data[3]:>5.1f} | {data[4]:>6.2f} |")

print("-"*65)
