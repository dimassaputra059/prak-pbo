from abc import ABC, abstractmethod

class AkunBank(ABC):
    @abstractmethod
    def __init__(self, nama, tahun_daftar, saldo):
        pass
    
    @abstractmethod
    def transfer_saldo(self, transfer):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.usia_akun = 2023 - tahun_daftar
        self.saldo = saldo
        
    def transfer_saldo(self, transfer):
        if self.usia_akun >= 3 and transfer > 100000:
            print("biaya administrasi : gratis")
        elif self.usia_akun < 3 and transfer > 100000:
            print("biaya administrasi : Rp.2000")
        else:
            print("biaya administrasi : gratis")
            
    def lihat_suku_bunga(self):
        if self.usia_akun >= 3 and self.saldo >= 1000000000:
            print("bunga bulanan : {}".f(self.saldo * 0.01))
        elif self.usia_akun < 3 and self.saldo >= 1000000000:
            print("bunga bulanan : {}".f(self.saldo * 0.02))
        else:
            print("bunga bulanan : {}".f(self.saldo * 0.03))
            
class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.usia_akun = 2023 - tahun_daftar
        self.saldo = saldo
        
    def transfer_saldo(self, transfer):
        if self.usia_akun >= 3 and transfer > 100000:
            print("biaya administrasi : Rp.2000")
        elif self.usia_akun < 3 and transfer > 100000:
            print("biaya administrasi : Rp.5000")
        else:
            print("biaya administrasi : gratis")
            
    def lihat_suku_bunga(self):
        if self.usia_akun >= 3 and self.saldo >= 10000000:
            print("bunga bulanan : {}".f(self.saldo * 0.01))
        elif self.usia_akun < 3 and self.saldo >= 10000000:
            print("bunga bulanan : {}".f(self.saldo * 0.02))
        else:
            print("bunga bulanan : {}".f(self.saldo * 0.03))
