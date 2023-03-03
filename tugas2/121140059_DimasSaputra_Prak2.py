class DataDiri:
    def __init__(self, nama, nim, kelas_PBO_siakad, jumlah_sks):
        self.nama = nama
        self.nim = nim
        self.kelas_PBO_siakad = kelas_PBO_siakad
        self.jumlah_sks = jumlah_sks

    def cetak(self):
        print("Nama :", self.nama)
        print("NIM :", self.nim)
        print("Kelas PBO siakad :", self.kelas_PBO_siakad)
        print("Jumlah sks :", self.jumlah_sks)
    
data = DataDiri("Dimas Saputra", 121140059, "RB", 22)

data.cetak()
