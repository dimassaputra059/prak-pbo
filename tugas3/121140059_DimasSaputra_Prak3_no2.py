class AkunBank:
    list_pelanggan = []

    def __init__(self, __no_pelanggan, __nama_pelanggan, __jumlah_saldo):
        self.__no_pelanggan = __no_pelanggan
        self.__nama_pelanggan = __nama_pelanggan
        self.__jumlah_saldo = __jumlah_saldo
        self.list_pelanggan = None

    def lihat_menu(self):
        print("Selamat Datang", self.__nama_pelanggan, "di Bank Syariah Indonesia")
        print("Menu yang bisa dipilih")
        print("1. Lihat Saldo\n2. Tarik Tunai\n3. Transfer Saldo\n4. Keluar")

    def lihat_saldo(self):
        print("Jumlah saldo atas nama", self.__nama_pelanggan, ": Rp.", self.__jumlah_saldo)

    def tarik_tunai(self, nominal_tarik):
        if self.__jumlah_saldo >= nominal_tarik:
            self.__jumlah_saldo -= nominal_tarik
        else:
            print("Jumlah saldo tidak mencukupi")
        
    def transfer(self,other,nominal_transfer,no_transfer):
        if self.list_pelanggan is None and other.list_pelanggan is None and other.__no_pelanggan == no_transfer:
            other.__jumlah_saldo += nominal_transfer
            self.__jumlah_saldo -= nominal_transfer
            return True
        else:
            return False


Akun1 = AkunBank(1234, "Dimas Saputra", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

n = 0

# Akun1 simulasi
while(n != 4):
    Akun1.lihat_menu()
    n = int(input("Masukkan nomor input : "))
 
    if n == 1:
        Akun1.lihat_saldo()
    elif n == 2:
        nominal_tarik = int(input("Masukkan jumlah nominal yang ingin ditarik : Rp."))
        Akun1.tarik_tunai(nominal_tarik)
    elif n == 3:
        nominal_transfer = int(input("Masukkan nominal yang ingin ditransfer : "))
        no_transfer = int(input("Masukkan no rekening tujuan : "))
        if Akun1.transfer(Akun2, nominal_transfer, no_transfer) == False and Akun1.transfer(Akun3, nominal_transfer, no_transfer) == False:
            print("No rekening tujuan tidak dikenal! akan kembali ke menu utama")
    elif n == 4:
        print("Terima kasih telah memilih Bank Syariah Indonesia")
    print("\n")
