class Mahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    def update_nilai(self, tugas, uts, uas):
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

    def tampilkan_data(self):
        return f"{self.nim:<9} | {self.nama:<10} | {self.tugas:<5} | {self.uts:<3} | {self.uas:<3} | {self.akhir:<5.2f}"

class ManajemenMahasiswa:
    def __init__(self):
        self.data_mahasiswa = {}

    def tambah_data(self):
        print("Tambah Data")
        nim = input("NIM        : ")
        nama = input("Nama       : ")
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))
        self.data_mahasiswa[nim] = Mahasiswa(nim, nama, tugas, uts, uas)
        print("Data berhasil ditambahkan!\n")

    def tampilkan_data(self):
        print("Daftar Nilai")
        print("=" * 60)
        print("| NO |    NIM    |    NAMA    | TUGAS | UTS | UAS | AKHIR |")
        print("=" * 60)
        if not self.data_mahasiswa:
            print("|                     TIDAK ADA DATA                     |")
        else:
            for i, mahasiswa in enumerate(self.data_mahasiswa.values(), start=1):
                print(f"| {i:<2} | {mahasiswa.tampilkan_data()}")
        print("=" * 60)

    def ubah_data(self):
        print("Ubah Data")
        nim = input("Masukkan NIM yang akan diubah: ")
        if nim in self.data_mahasiswa:
            print("Masukkan data baru:")
            nama = input("Nama       : ")
            tugas = float(input("Nilai Tugas : "))
            uts = float(input("Nilai UTS   : "))
            uas = float(input("Nilai UAS   : "))
            self.data_mahasiswa[nim].update_nilai(tugas, uts, uas)
            self.data_mahasiswa[nim].nama = nama
            print("Data berhasil diubah!\n")
        else:
            print("NIM tidak ditemukan!\n")

    def hapus_data(self):
        print("Hapus Data")
        nim = input("Masukkan NIM yang akan dihapus: ")
        if nim in self.data_mahasiswa:
            del self.data_mahasiswa[nim]
            print("Data berhasil dihapus!\n")
        else:
            print("NIM tidak ditemukan!\n")

    def cari_data(self):
        print("Cari Data")
        nim = input("Masukkan NIM yang dicari: ")
        if nim in self.data_mahasiswa:
            mahasiswa = self.data_mahasiswa[nim]
            print("Data ditemukan!")
            print(f"NIM        : {mahasiswa.nim}")
            print(f"Nama       : {mahasiswa.nama}")
            print(f"Nilai Tugas: {mahasiswa.tugas}")
            print(f"Nilai UTS  : {mahasiswa.uts}")
            print(f"Nilai UAS  : {mahasiswa.uas}")
            print(f"Nilai Akhir: {mahasiswa.akhir:.2f}\n")
        else:
            print("NIM tidak ditemukan!\n")

# Program utama
manajemen = ManajemenMahasiswa()

while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]:")
    pilihan = input("Pilihan: ").lower()
    if pilihan == 'l':
        manajemen.tampilkan_data()
    elif pilihan == 't':
        manajemen.tambah_data()
    elif pilihan == 'u':
        manajemen.ubah_data()
    elif pilihan == 'h':
        manajemen.hapus_data()
    elif pilihan == 'c':
        manajemen.cari_data()
    elif pilihan == 'k':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!\n")
