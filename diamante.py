class A:
    def llamada(selfs):
        print('Llamada A')


class B(A):
    def llamada(self):
        print('Llamada B')
        super().llamada()


class C(A):
    def llamada(self):
        print('Llamada C')
        super().llamada()

class D(B,C):
    def llamada(self):
        print('Llamada D')
        super().llamada()

d = D()
d.llamada()