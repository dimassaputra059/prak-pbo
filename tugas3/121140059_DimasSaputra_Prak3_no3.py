class TokoBuku:
    jumlah_buku = 0
    def __init__(self):
        # protected atribut hanya dapat diakses dari dalam kelas dan turunan kelasnya
        # dalam contoh kasus kali ini atribut __total_harga bisa diakses pada metode harga_total()
        self.__total_harga = 0
        # private atribut memungkinkan atribut tersebut tidak bisa diakses dari luar kelas
        # dalam contoh kasus kali ini atribut _stok_buku bisa diakses pada luar kelas yaitu pada kelas TokoBuku atau StokBuku 
        self._stok_buku = 100
        # public atribut dapat diakses dari dalam atau dari luar
        # dalam contoh kasus kali ini atribut harga_buku dapat diakses dari luar kelas yaitu pada line 48
        self.harga_buku = 40000
        
    # public metode dapat diakses dari dalam atau dari luar kelas
    # dalam contoh kasus ini metode beli_buku() bisa diakses dari luar kelas yaitu pada line 51
    def beli_buku(self,jumlah):
        if jumlah <= self._stok_buku:
            self.jumlah_buku += jumlah
            self._stok_buku -= jumlah
        else:
            print("maaf stok buku tidak cukup")
        
    def cek_stok(self):
        print("stok buku tersedia :", self._stok_buku)
        
    def harga_total(self):
        self.__total_harga = self.jumlah_buku * self.harga_buku
        print("total harga buku :", self.__total_harga)
        
    # protected metode hanya bisa diakses dari dalam atau luar kelas
    # dalam contoh kasus kali ini metode __tambah_stok_buku() diakses pada kelas turunannya yaitu StokBuku()
    def _tambah_stok_buku(self,stok_tambah):
        self._stok_buku += stok_tambah

class StokBuku(TokoBuku):
    def __init__(self,jumlah_stok_buku_tambahan):
        self.jumlah_stok_buku_tambahan = jumlah_stok_buku_tambahan
    
    def _tambah_stok_buku(self):
        self._stok_buku += self.jumlah_stok_buku_tambahan

beli = TokoBuku()   
n = False
i = 0
jumlah_buku = 0
while(n == False):
    print("\nMenu:\n1. Lihat harga buku\n2. Beli buku\n3. Jumlah Buku di keranjang\n4. Harga total\n5. Cek stok buku\n6. Keluar")
    i = int(input("pilih menu : "))
    if i == 1:
        print("Harga buku:Rp.{}".format(beli.harga_buku))
    elif i == 2:
        jumlah_buku = int(input("Jumlah buku yang ingin dibeli : "))
        beli.beli_buku(jumlah_buku)
    elif i == 3:
        print("Jumlah buku di keranjang : {}".format(beli.jumlah_buku))
    elif i == 4:
        beli.harga_total()
    elif i == 5:
        beli.cek_stok()
    elif i == 6:
        n = True
