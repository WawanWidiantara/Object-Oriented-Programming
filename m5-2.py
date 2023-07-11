# class Menu:
#     def __init__(self, item, harga, diskon):
#         self._item = item
#         self.harga = harga
#         self.__diskon = diskon

#     def getDiskon(self):
#         return f'{self.__diskon * 100}%'

#     def setDiskon(self, diskon_baru):
#         self.__diskon = diskon_baru

#     def lihatMenu(self):
#         diskon = self.harga * self.__diskon
#         print(f'{self._item}\t: {self.harga - diskon}')


# # object
# menu1 = Menu('Udang Keju', 20000, 0.1)
# menu2 = Menu('Banana Cake', 35000, 0.05)

# # coba methods
# menu1.lihatMenu()
# menu2.lihatMenu()
# print('=' * 30)

# print(f'diskon {menu1._item}\t: {menu1.getDiskon()}')
# print(f'diskon {menu2._item}\t: {menu2.getDiskon()}')
# print('=' * 30)

# menu1.setDiskon(0.5)
# menu2.setDiskon(0.2)
# menu1.lihatMenu()
# menu2.lihatMenu()


# class Buku:

#     list_peminjam = []

#     def __init__(self, judul, penulis):
#         self.__judul = judul
#         self.penulis = penulis

#     def pinjamBuku(self, nama):
#         if nama not in Buku.list_peminjam:
#             Buku.list_peminjam.append(nama)
#             print(f'{nama} meminjam buku "{self.__judul}"')
#         else:
#             print(f'{nama} sudah pernah meminjam buku')

#     def kembalikanBuku(self, nama):
#         if nama in Buku.list_peminjam:
#             Buku.list_peminjam.remove(nama)
#             print(f'{nama} mengembalikan buku dengan judul "{self.__judul}"')
#         else:
#             print(f'Peminjam not found')


# # object
# buku1 = Buku("Angel & Demons", "Dan Brown")
# buku2 = Buku("How to Respect Myself", "Mark White")
# buku3 = Buku("Pierre", "Gustavo Mazali")

# # method
# buku1.pinjamBuku('Anto')
# buku2.pinjamBuku('Rudi')
# buku3.pinjamBuku('Suherman')
# print('=' * 30)
# print(f'List peminjam Buku: {Buku.list_peminjam}')
# print('=' * 30)

# buku1.kembalikanBuku('Anto')
# buku2.pinjamBuku('Rudi')
# buku3.kembalikanBuku('Widi')
# print('=' * 30)
# print(f'List peminjam Buku: {Buku.list_peminjam}')
# print('=' * 30)


class Pelajar:
    def __init__(self, nama, npm, tahun_lahir):
        self.nama = nama
        self.__npm = npm
        self.__tahun_lahir = tahun_lahir

    def getUmur(self):
        print(f'Umur {self.nama}\t: {2022 - self.__tahun_lahir} tahun')

    def setUmur(self, umur):
        self.__tahun_lahir = umur

    def getNPM(self):
        print(f'NPM {self.nama}\t: {self.__npm}')


pelajar1 = Pelajar('Widi', 135, 2002)
pelajar2 = Pelajar('Gede', 521, 2003)

print('=' * 30)
pelajar1.getUmur()
pelajar2.getUmur()
print('=' * 30)

print('Set umur Gede: ')
pelajar2.setUmur(2002)
pelajar2.getUmur()
print('=' * 30)

pelajar1.getNPM()
pelajar2.getNPM()
