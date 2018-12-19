def decorador2(funcion):
    def wrap():
        print('='*12)
        funcion()
        print('='*12)
    return wrap

def decorador3(funcion):
    def wrap():
        print('decorador 3')
        funcion()
        print('*'*12)
    return wrap


@decorador3# *
@decorador2# =
def printText():
    print('Hola mundo')

printText()