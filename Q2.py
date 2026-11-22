class karyawan:
    def __init__(self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
        self.energi=100
    def x (self):
        print(f'Karyawan {self.nama} memiliki gaji {self.gaji:,}')
    def lembur (self):
        self.gaji+=200000
        self.energi-=30
        print(f'karyawan {self.nama} sedang lembur!!')
        print(f"Gaji {self.nama} bertambah menjadi {self.gaji}")
        print(f"Sisa energi {self.nama} adalah {self.energi}")

kry1=karyawan("Siti",50000000)
kry1.lembur()
kry2=karyawan("Budi",45000000)
kry2.lembur()
kry3=karyawan("Andi",30000000)
kry3.lembur()
kry4=karyawan("Ziko",35000000)
kry4.lembur()
kry5=karyawan("Benny",40000000)
kry5.lembur()