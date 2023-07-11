class Mobil:
    def __init__(self, merk, warna, CC):
        self.__merk = merk
        self.warna = warna
        self.CC = CC

    def tampilkan_merk(self):
        print(f'Merk\t: {self.__merk}')


jip = Mobil('Jeep', 'hitam', 3000)
jip.tampilkan_merk()

print(f'Warna\t: {jip.warna}')
print(f'CC\t: {jip.CC}')
