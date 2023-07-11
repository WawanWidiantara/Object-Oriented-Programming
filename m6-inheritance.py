class Induk:
    parent_attr = 100

    def __init__(self):
        print(f'Memanggil Konstruktor Induk')

    def parent_method(self):
        print(f'Memanggil Method Induk')

    def __setattr__(self, attr):
        Induk.parent_attr = attr

    def getattr(self):
        print(f'Atribut Induk: {Induk.parent_attr}')


class Anak(Induk):
    def __init__(self):
        print(f'Memanggil Konstruktor Anak')

    def child_method(self):
        print(f'Memanggil Method Anak')


a1 = Anak()
a1.child_method()
a1.parent_method()
a1.__setattr__(200)
a1.getattr()
