class Persona:
    def saludo(self):
        print('Hola')

    def comer(self,param1, param2):
        print('comer persona')

class Peruano(Persona):

    def saludo(self):
        print('Hablaaaa')

class Chileno(Persona):
    def saludo(self):
        print('Hola Gallo')
        super().saludo()

persona = Persona()
persona.saludo()
persona.comer(1,2)

peruano = Peruano()
peruano.saludo()

chileno = Chileno()
chileno.saludo()