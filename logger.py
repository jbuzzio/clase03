def logger(debug):
    def log(func):
        def wraper(x, y):
            if debug:
                print('valor a: ',x)
                print('valor b: ',y)
                return func(x,y)
        return wraper
    return log

@logger(debug = True)
def suma(a,b):
    return a + b


print(suma(1,2))