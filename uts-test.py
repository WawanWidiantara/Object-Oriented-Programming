import json
from m9 import PerpusItem, Katalog, Buku, Pengarang, Majalah, DVD, Pengunjung

# membuat object Buku
buku1 = Buku('Atomic Habits', 'Buku', 13149817141, 'James Clear', 234, '15 cm x 23 cm')
buku2 = Buku('test', 'Buku', 213123, 'Mail', 200, 'A4')
buku3 = Buku('api', 'Buku', 213123, 'Mail', 200, 'A4')

# membuat object majalah
majalah1 = Majalah('Bobo', 'Majalah', 300, 'Remaja')
majalah2 = Majalah('Gucci', 'Majalah', 300, 'Fasion')

# membuat object majalah
dvd1 = DVD('Iron Man', 'DVD', 'Robert Downey Jr.', 'Action')
dvd2 = DVD('Captain America', 'DVD', 'Chris Evan', 'Action')

# membuat objek pengarang
pengarang1 = Pengarang('Mail')

# membuat objek pengunjung
pengunjung1 = Pengunjung('Harto')

# info item
buku1.info()
majalah1.info()
dvd1.info()
pengarang1.info()

# cek lokasi penyimpanan
buku1.LokasiPenyimpanan()

# cek list
print(f'\nList Item Tersedia:')
print(json.dumps(PerpusItem.listItem, indent=3))
print(f'\nList Item Dipinjam:')
print(json.dumps(PerpusItem.buku_dipinjam, indent=3))
print(f'\nList Peminjam:')
print(json.dumps(Pengunjung.listPeminjam, indent=3))

# cari
print(f'\nHasil Pencarian dari Katalog:')
Katalog.cari('Iron Man')
print(f'\nHasil Pencarian dari Pengarang:')
pengarang1.cari()

# pinjam
pengunjung1.pinjam('api')
pengunjung1.pinjam('Atomic Habits')

# kembalikan
pengunjung1.kembalikan('api')
pengunjung1.kembalikan('Atomic Habits')
