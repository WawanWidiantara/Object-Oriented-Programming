class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Vector {self.a, self.b}'

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


p1 = Vector(5, 10)
p2 = Vector(4, -2)
print(p1 + p2)
