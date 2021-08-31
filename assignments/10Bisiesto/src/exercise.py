
def main():
    #escribe tu código abajo de esta línea
    def es_bisiesto(x):
    if x%4==0 and x%400==0:
        return "True"
    elif x%100==0:
        return "False"
    else:
        return "False"
def main():
    x=int(input("Dame el año: "))
    y=es_bisiesto(x)
    print(str(y))
main()

if __name__=='__main__':
    main()
