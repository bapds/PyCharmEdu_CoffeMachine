class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        if (self.a**2) + (self.b**2) == (self.c**2):
            self.S = float(0.5 * (self.a * self.b))
        else:
            self.S = "Not right"


entrada = input()
lista = []
lista = entrada.split(' ')
c, a, b = lista
a = int(a)
b = int(b)
c = int(c)

new_triangulo = RightTriangle(c, a, b)
print(new_triangulo.S)
