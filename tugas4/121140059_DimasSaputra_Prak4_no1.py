class Komputer:
    def __init__(self,nama,jenis,harga,merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk
        
    def str(self):
        return (f"{self.nama} {self.jenis} produksi {self.merk}")
        
class Processor(Komputer):
    def __init__(self,nama,jenis,harga,merk,jumlah_core,kecepatan_processor):
        Komputer.__init__(self,nama,jenis,harga,merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor
        
class RAM(Komputer):
    def __init__(self,nama,jenis,harga,merk,capacity):
        Komputer.__init__(self,nama,jenis,harga,merk)
        self.capacity = capacity
        
class HDD(Komputer):
    def __init__(self,nama,jenis,harga,merk,capacity,rpm):
        Komputer.__init__(self,nama,jenis,harga,merk)
        self.capacity = capacity
        self.rpm = rpm
        
class VGA(Komputer):
    def __init__(self,nama,jenis,harga,merk,capacity):
        Komputer.__init__(self,nama,jenis,harga,merk)
        self.capacity = capacity
        
class PSU(Komputer):
    def __init__(self,nama,jenis,harga,merk,daya):
        Komputer.__init__(self,nama,jenis,harga,merk)
        self.daya = daya
        
   
p1 = Processor('Processor','Core i7 7740X',4350000,'Intel',4,'4.3GHz')
p2 = Processor('Processor','Ryzen 5 3600',250000,'AMD',4,'4.3GHz')
ram1 = RAM('RAM','DDR4 SODimm PC19200/2400MHz',328000,'V-Gen','4GB')
ram2 = RAM('RAM','DDR4 2400MHz',328000,'G.SKILL','4GB')
hdd1 = HDD('HDD','HDD 2.5 inch',295000,'Seagate','500GB',7200)
hdd2 = HDD('HDD','HDD 2.5 inch',295000,'Seagate','1000GB',7200)
vga1 = VGA('VGA','VGA GTX 1050',250000,'Asus','2GB')
vga2 = VGA('VGA','1060Ti',250000,'Asus','8GB')
psu1 = PSU('PSU','Corsair V550',250000,'Corsair','500W')
psu2 = PSU('PSU','Corsair V550',250000,'Corsair','500W')

rakit = [[p1.str(),ram1.str(),hdd1.str(),vga1.str(),psu1.str()],[p2.str(),ram2.str(),hdd2.str(),vga2.str(),psu2.str()]]

for i in range(len(rakit)):
    print(f"Komputer {i+1}")
    for j in range(len(rakit[i])):
        print(rakit[i][j])
    print("\n")
