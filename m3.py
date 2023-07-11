class Mahasiswa:
    '''Dasar untuk kelas untuk semua mahasiswa'''
    jml_mahasiswa = 0

    def __init__(self, nama, npm, kelas):
        self.nama = nama
        self.npm = npm
        self.kelas = kelas
        Mahasiswa.jml_mahasiswa += 1

    def view_jumlah(self):
        print(f'Total Mahasiswa : {Mahasiswa.jml_mahasiswa}')

    def view_profil(self):
        print(f"Nama Mahasiswa : {self.nama}")
        print(f"NPM Mahasiswa : {self.npm}")
        print(f"Kelas Mahasiswa : {self.kelas}")


# membuat objeck dari class Mahasiswa
mhs1 = Mahasiswa("Widi", 111, "A")
mhs2 = Mahasiswa("Antara", 112, "A")

# view
mhs1.view_profil()
print("=" * 25)
mhs2.view_profil()
print("=" * 25)
print(f'Jumlah Mahasiswa : {Mahasiswa.jml_mahasiswa}')
print(" ")
mhs1.nama = 'Nia'
mhs1.view_profil()
