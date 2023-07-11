class UTY(object):
    def __init__(self, status, nama, prodi):
        self.status = status
        self.nama = nama
        self.prodi = prodi

    def Semangat(self):
        print('Indonesia Maju Indonesia Tumbuh UTY Hebat')

    def Info(self):
        print('-- INFORMASI --')
        print(f'Nama\t\t: {self.nama}')
        print(f'Status\t\t: {self.status}')
        print(f'Program Studi\t: {self.prodi}')


class Dosen(UTY):
    def __init__(self, status, nama, prodi, nip):
        super().__init__(status, nama, prodi)
        self.nip = nip

    def SemangatDosen(self):
        self.Semangat()
        print('Dosen bermartabat')

    def InfoDosen(self):
        print(f'NIP\t\t: {str(self.nip)}')


class Mahasiswa(UTY):
    """docstring for Mahasiswa"""

    def __init__(self, status, nama, prodi, npm):
        super().__init__(status, nama, prodi)
        self.npm = npm

    def SalamMhs(self):
        self.Semangat()
        print('Salam Mahasiswa')

    def InfoMhs(self):
        print(f'NPM\t\t: {str(self.npm)}')


# Object Dosen
dosen1 = Dosen('dosen', 'Thomas', 'Informatika', 1235678)
dosen1.Info()
dosen1.InfoDosen()
dosen1.SemangatDosen()

print('-' * 43)

# Object Mahasiswa
mhs1 = Mahasiswa('mahasiswa', 'Effendy', 'Informatika', 5215678)
mhs1.Info()
mhs1.InfoMhs()
mhs1.SalamMhs()
