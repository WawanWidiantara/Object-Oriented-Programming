class Induk:
    def my_method(self):
        print(f'Memanggil Method Induk')


class Anak(Induk):
    def my_method(self):
        print(f'Memanggil Method Anak')


a = Anak()
a.my_method()
