class Burung:
    def intro(self):
        print('Ada Beberapa Burung')

    def terbang(self):
        print('Kebanyakan Burung bisa terbang, tapi ada burung yang tidak bisa terbang')


class Emprit(Burung):
    def terbang(self):
        print('Burung Emprit bisa terbang')


class Ostrich(Burung):
    def terbang(self):
        print('Burung Ostrich tidak bisa terbang')


# obj
obj_burung = Burung()
obj_emprit = Emprit()
obj_ostrich = Ostrich()

obj_burung.intro()
obj_burung.terbang()
obj_emprit.terbang()
obj_ostrich.terbang()
