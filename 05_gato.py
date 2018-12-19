class Felino:
    def __init__(self, tipo):
        self.tipo = tipo
        print('se creo felino')

    def rugir(self):
        print('el felino dio un rugido')

class Mascota:
    def sientate(self):
        print('sientate')

class Gato(Felino, Mascota):

    def __init__(self,energia, hambre):
        super().__init__(tipo = 'persa')
        self.energia = energia
        self.hambre = hambre
        print('se creo un gato ' + self.tipo)

    #def __str__(self):
    #    return 'Hola soy un gato'

    def dormir(self):
        print('gato durmiendo')

cat = Gato(5,5)
cat.dormir()
cat.rugir()
cat.sientate()