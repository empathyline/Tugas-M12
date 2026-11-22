class barang:
    def __init__(self,nama,harga):
        self.nama=nama
        self.harga=harga

baju=barang("Baju",100000)
print(baju.harga)

baju.harga=(baju.harga)-(baju.harga*0.25)
print(f"Harga Baju setelah diskon adalah sebesar {baju.harga}")