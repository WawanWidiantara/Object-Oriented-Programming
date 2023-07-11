class Karyawan(object):  # parent class
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.umr = 2000000

    def infoKaryawan(self):
        print(f'Nama\t\t: {self.nama}')
        print(f'Jabatan\t\t: {self.jabatan}')
        print(f'Gaji\t\t: Rp. {self.umr}')


class Manager(Karyawan):  # child class
    def __init__(self, nama, jabatan):
        super().__init__(nama, jabatan)
        self.gaji = self.umr * 3

    def infoKaryawan(self):
        print(f'Nama\t\t: {self.nama}')
        print(f'Jabatan\t\t: {self.jabatan}')
        print(f'Gaji\t\t: Rp. {self.gaji}')  # overriding


class Satpam(Karyawan):  # child class
    def __init__(self, nama, jabatan):
        super().__init__(nama, jabatan)

    # overloading
    def bonusGaji(self, lembur=None, libur=None):
        bonus = 0
        if lembur != None and libur != None:
            bonus = (lembur * self.umr * 0.2) - (libur * self.umr * 0.1)
        else:
            bonus = lembur * self.umr * 0.1

        if bonus >= 0:
            print(f'Bonus\t\t: Rp. {int(bonus)}')
        else:
            print(f'Potong Gaji\t: Rp. {int(bonus * -1)}')


# object
mnj1 = Manager('Gede', 'Manager')
pgw1 = Satpam('Widiantara', 'Pegawai')
pgw2 = Satpam('Wawan', 'Pegawai')

print('-- [DAFTAR PEGAWAI] --\n')
mnj1.infoKaryawan()
print('=' * 35)
pgw1.infoKaryawan()
pgw1.bonusGaji(2, 8)
print('=' * 35)
pgw2.infoKaryawan()
pgw2.bonusGaji(2)
