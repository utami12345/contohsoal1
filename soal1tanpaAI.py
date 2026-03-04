n = int(input("Jumlah mahasiswa: "))

total_nilai = 0
nilai_tertinggi = 0
nama_tertinggi = ""
jumlah_lulus = 0

for i in range(n):
    print("\nMahasiswa ke-", i+1)
    nama = input("Nama: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    total_nilai += nilai_akhir

    if nilai_akhir >= 85:
        predikat = "Sangat Baik"
    elif nilai_akhir >= 75:
        predikat = "Baik"
    elif nilai_akhir >= 60:
        predikat = "Cukup"
    else:
        predikat = "Kurang"

    if nilai_akhir >= 60:
        status = "Lulus"
        jumlah_lulus += 1
    else:
        status = "Tidak Lulus"

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    print("Nilai Akhir:", nilai_akhir)
    print("Predikat:", predikat)
    print("Status:", status)

rata_rata = total_nilai / n

print("\nRata-rata kelas:", rata_rata)
print("Nilai tertinggi:", nama_tertinggi, "-", nilai_tertinggi)

print("Jumlah lulus:", jumlah_lulus)
