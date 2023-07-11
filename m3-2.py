# class Menu:
#     def __init__(self, nomor, namaMenu, harga):
#         self.nomor = nomor
#         self.namaMenu = namaMenu
#         self.harga = harga

#     def view_menu(self):
#         print(f'{self.nomor}. {self.namaMenu}\t: {self.harga}')


# menu1 = Menu(1, 'Sate', 12000)
# menu2 = Menu(2, 'Iga', 50000)
# menu3 = Menu(3, 'Nasi', 5000)

# print('List Menu :')
# menu1.view_menu()
# menu2.view_menu()
# menu3.view_menu()


# class Buku:
#     jumlah_buku = 0

#     def __init__(self, judul, penulis):
#         self.judul = judul
#         self.penulis = penulis
#         Buku.jumlah_buku += 1

#     def view_buku(self):
#         print(f'Judul Buku\t: {self.judul}\nPenulis\t\t: {self.penulis}\n')


# buku1 = Buku("Angel & Demons", "Dan Brown")
# buku2 = Buku("How to Respect Myself", "Mark White")
# buku3 = Buku("Pierre", "Gustavo Mazali")
# buku1.view_buku()
# buku2.view_buku()
# buku3.view_buku()
# print(f'Total Buku = {Buku.jumlah_buku}')

# class Garis:
#     def __init__(self, gambar, jumlahGaris):
#         self.gambar = gambar
#         self.jumlahGaris = jumlahGaris

#     def set_jumlahGaris(self, jumlahGaris_baru):
#         self.jumlahGaris = jumlahGaris_baru

#     def view_garis(self):
#         print(f'Gambar\t\t: {self.gambar}\nJumlah Garis\t: {self.jumlahGaris}\n')


# gambar1 = Garis('segitiga', 2)
# print('awal')
# gambar1.view_garis()
# print('setelah diubah')
# gambar1.set_jumlahGaris(3)
# gambar1.view_garis()


class Pelajar:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def getName(self):
        return self.nama


pelajar1 = Pelajar("Alissa", 19)
pelajar2 = Pelajar("Melody", 18)
print(f'Nama pelajar ke-1 : {pelajar1.getName()}')
print(f'Nama pelajar ke-3 : {pelajar2.getName()}')
