class Kalkulator:
    def __init__(self, x, y):
        self.A = x
        self.B = y

    def tambah(self):
        self.hasil = self.A + self.B
        print(f'A + B = {self.hasil}')

    def kurang(self):
        self.hasil = self.A - self.B
        print(f'A - B = {self.hasil}')

    def kali(self):
        self.hasil = self.A * self.B
        print(f'A x B = {self.hasil}')

    def bagi(self):
        if self.B == 0:
            print('pembagian dengan nol')
        else:
            self.hasil = self.A / self.B
            print(f'A / B = {self.hasil}')


class Scientific(Kalkulator):
    def __init__(self, A, B):
        super().__init__(A, B)

    def pangkat(self):
        self.hasil = self.A ** self.B
        print(f'{self.A} pangkat {self.B} = {self.hasil}')

    def akar(self):
        self.hasil = self.A ** (1 / self.B)
        print(f'{self.A} akar {self.B} = {self.hasil}')


# object1 = Kalkulator(1, 2)
# object1.tambah()
# object1.kurang()
# object1.kali()
# object1.bagi()

# print('=' * 15)

# object2 = Kalkulator(2, 0)
# object2.bagi()

# sc1 = Scientific(2, 4)
# sc1.pangkat()
# sc1.akar()

# print('=' * 15)

# sc2 = Scientific(8, 3)
# sc2.pangkat()
# sc2.akar()
