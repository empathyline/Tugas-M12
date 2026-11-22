class RekeningBank:
    def __init__(self,nama_pemilik,saldo=0):
        self.nama_pemilik=nama_pemilik
        self.saldo=saldo

    def menabung(self,nominal):
        self.saldo+=nominal
        print(f"Berhasil menabung Rp{self.saldo}. Saldo sekarang: Rp{self.saldo}")

    def tarik_saldo(self,nominal):
        if self.saldo>=nominal:
            self.saldo=self.saldo-nominal
            print(f'Berhasil menarik Rp{nominal}. Saldo sekarang: Rp{self.saldo}')
        else:
            print(f'maaf, saldo tidak cukup')
        

rekening=RekeningBank("Thariq")
menabung=rekening.menabung(150000)
tarik_1=rekening.tarik_saldo(50000)
tarik_2=rekening.tarik_saldo(200000)
menabung=rekening.menabung(300000)