class karyawan:
    def __init__(self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
    def x (self):
        print(f'Karyawan {self.nama} memiliki gaji {self.gaji:,}')

kry1=karyawan("Siti",50000000)
kry1.x()
kry2=karyawan("Budi",45000000)
kry2.x()
kry3=karyawan("Andi",30000000)
kry3.x()
kry4=karyawan("Ziko",35000000)
kry4.x()
kry5=karyawan("Benny",40000000)
kry5.x()