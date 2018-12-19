def decorador(funcion):
    def envoltura(a):
        print('antes de la funcion')
        funcion(a)
        print('despues de la funcion')
    return envoltura

@decorador
def funcionPrueba(a):
    print('Hola funcion'+a)


funcionPrueba('asd')