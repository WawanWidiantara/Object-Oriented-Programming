class Gaji:
    def __init__(self, gaji_bulanan):
        self.gaji_bulanan = gaji_bulanan

    def total(self):
        return (self.gaji_bulanan * 12)


class Pegawai:
    def __init__(self, gaji_bulanan, bonus, libur):
        self.gaji_bulanan = gaji_bulanan
        self.bonus = bonus
        self.obj_gaji = Gaji(self.gaji_bulanan)
        self.potong = (libur * 200)

    def hasil_tahunan(self):
        total = self.obj_gaji.total() + self.bonus - self.potong
        return f'Total: {str(total)} rupiah'


class Manajer(Pegawai):
    def __init__(self, gaji_bulanan, bonus, libur):
        super().__init__(gaji_bulanan, bonus, libur)
        self.gaji_manajer = self.obj_gaji.total() + 1000

    def hasil_tahunan(self):
        total = self.gaji_manajer + self.bonus - self.potong
        return f'Total: {str(total)} rupiah'


obj_pegawai = Pegawai(2600, 500, 2)
obj_manajer = Manajer(2600, 500, 2)

print('Gaji Pegawai')
print(obj_pegawai.hasil_tahunan())
print('=' * 15)
print('Gaji Manajer')
print(obj_manajer.hasil_tahunan())
