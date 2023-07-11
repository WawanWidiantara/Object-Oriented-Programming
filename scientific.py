from calculator import Kalkulator


class Scientific(Kalkulator):
    def __init__(self, A, B):
        super().__init__(A, B)

    def pangkat(self):
        self.hasil = self.A ** self.B
        print(f'{self.A} pangkat {self.B} = {self.hasil}')

    def akar(self):
        self.hasil = self.A ** (1 / self.B)
        print(f'{self.A} akar {self.B} = {self.hasil}')


sc1 = Scientific(2, 4)
sc1.pangkat()
sc1.akar()

print('=' * 15)

sc2 = Scientific(8, 3)
sc2.pangkat()
sc2.akar()
