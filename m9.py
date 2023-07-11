import json


class PerpusItem:

    listItem = []  # list item yang tersedia
    listBuku = [x for x in listItem if x['Subjek'] == 'Buku']
    buku_dipinjam = []  # list item yang dipinjam

    def __init__(self, judul, subjek):
        self.Judul = judul
        self.Subjek = subjek

    def LokasiPenyimpanan(self):
        if self.Subjek == 'Buku':
            print('Buku disimpan di rak buku')
        elif self.Subjek == 'Majalah':
            print('Majalah disimpan di rak majalah')
        elif self.Subjek == 'DVD':
            print('DVD disimpan di rak DVD')
        else:
            print('subjek tidak ditemukan')

    def info(self):
        pass


class Katalog:

    @classmethod  # menjadikan method ini sebagai class method
    def cari(self, judul):
        try:
            pencarian = [x for x in PerpusItem.listItem if x['Judul'] == judul]
            print(json.dumps(pencarian, indent=3))
        except:
            print('Item tidak ditemukan')


class Buku (PerpusItem):
    def __init__(self, judul, subjek, isbn, pengarang, jmlHal, ukuran):
        super().__init__(judul, subjek)
        self.ISBN = isbn
        self.Pengarang = pengarang
        self.jmlHal = jmlHal
        self.Ukuran = ukuran

        # store data ke PerpusItem.listItem
        keys = ['Judul', 'Subjek', 'ISBN', 'Pengarang', 'jmlHal', 'Ukuran']
        values = [self.Judul, self.Subjek, self.ISBN, self.Pengarang, self.jmlHal, self.Ukuran]
        buku = dict(zip(keys, values))
        PerpusItem.listItem.append(buku)
        PerpusItem.listBuku.append(buku)

    def info(self):
        print(f'Judul\t\t:{self.Judul}\nSubjek\t\t:{self.Subjek}\nISBN\t\t:{self.ISBN}\nPengarang\t:{self.Pengarang}\nHalaman\t\t:{self.jmlHal}\nUkuran\t\t:{self.Ukuran}\n')


class Pengarang:
    def __init__(self, pengarang):
        self.pengarang = pengarang

    def cari(self):
        pencarian = [x for x in PerpusItem.listBuku if x['Pengarang'] == self.pengarang]
        print(json.dumps(pencarian, indent=3))

    def info(self):
        buku = [x for x in PerpusItem.listBuku if x['Pengarang'] == self.pengarang]
        print(f'Pengarang\t: {self.pengarang}\nJumlah Buku\t: {len(buku)} buku\n')


class Majalah(PerpusItem):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue

        keys = ['Judul', 'Subjek', 'Volume', 'Issue']
        values = [self.Judul, self.Subjek, self.volume, self.issue]
        majalah = dict(zip(keys, values))
        PerpusItem.listItem.append(majalah)

    def info(self):
        print(f'Judul\t:{self.Judul}\nSubjek\t:{self.Subjek}\nVolume\t:{self.volume}\nIssue\t:{self.issue}\n')


class DVD(PerpusItem):
    def __init__(self, judul, subjek, aktor, genre):
        super().__init__(judul, subjek)
        self.Aktor = aktor
        self.Genre = genre

        # store data ke PerpusItem.listItem
        keys = ['Judul', 'Subjek', 'Aktor', 'Genre']
        values = [self.Judul, self.Subjek, self.Aktor, self.Genre]
        dvd = dict(zip(keys, values))
        PerpusItem.listItem.append(dvd)

    def info(self):
        print(f'Judul\t:{self.Judul}\nSubjek\t:{self.Subjek}\nAktor\t:{self.Aktor}\nGenre\t:{self.Genre}\n')


class Pengunjung:
    listPeminjam = []  # list peminjam buku

    def __init__(self, pengunjung):
        self.pengunjung = pengunjung

    def pinjam(self, judul):
        # cek peminjam hanya boleh meminjam 1 kali sebelum dikembalikan
        if self.pengunjung not in Pengunjung.listPeminjam:
            item = [x for x in PerpusItem.listItem if x['Judul'] == judul]
            if not item:
                print('Item tidak tersedia')
            else:
                pinjam = [x for x in PerpusItem.listItem if x['Judul'] == judul][0]

                # hapus data dari PerpusItem.listItem
                for index in range(len(PerpusItem.listItem)):
                    if PerpusItem.listItem[index]['Judul'] == judul:
                        del PerpusItem.listItem[index]
                        break

                # tambah data ke PerpusItem.buku_dipinjam
                PerpusItem.buku_dipinjam.append(pinjam)

                # tambah data ke Pengunjung.listPeminjam
                Pengunjung.listPeminjam.append(self.pengunjung)
                print('\nItem berhasil dipinjam')
        else:
            print('Pengunjung sudah meminjam')

    def kembalikan(self, judul):
        try:
            kembalikan = [x for x in PerpusItem.buku_dipinjam if x['Judul'] == judul][0]

            # cek jika buku exist in PerpusItem.buku_dipinjam
            if kembalikan in PerpusItem.buku_dipinjam:

                # tambah buku yang dikembalikan ke PerpusItem.listItem
                PerpusItem.listItem.append(kembalikan)

                # hapus item dari PerpusItem.buku_dipinjam
                for index in range(len(PerpusItem.buku_dipinjam)):
                    if PerpusItem.buku_dipinjam[index]['Judul'] == judul:
                        del PerpusItem.buku_dipinjam[index]
                        break

                # hapus item dari Pengunjung.listPeminjam
                Pengunjung.listPeminjam.remove(self.pengunjung)
                print('\nItem berhasil dikembalikan')
        except:
            print('Item belum dipinjam atau tidak ditemukan')
