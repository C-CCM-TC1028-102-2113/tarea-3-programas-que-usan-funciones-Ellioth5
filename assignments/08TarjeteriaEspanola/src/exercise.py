
def main():
    #escribe tu código abajo de esta línea
    def func (x,y):
    a=x*12
    b=y*35
    if a>b:
        return b
    if b>a:
        return a
def main():
    x=int(input("Dame la cantidad de pliegos de papel albanene: "))
    y=int(input("Dame la cantidad de plumones: "))
    pal=func(x,y)
    print("El número máximo de tarjetas que se pueden hacer es: "+str(pal))
main()

if __name__=='__main__':
    main()
