
def main():
    #escribe tu código abajo de esta línea
print("Qué quiere sacar? 1.Area 2.Volumen 3.Ambas")
jh=int(input())
if jh==1 or jh==2 or jh==3:
    print("Dame los datos")
    bas=float(input("Base "))
    alt=float(input("Altura "))
    prof=float(input("Profundidad "))
    def Area(bas,alt):
        area=(bas*alt)
        return area
    def Volumen(bas,alt,prof):
        vol=(bas*prof)*alt
        return vol
    def main():
        if jh==1:
            x=Area(bas,alt)
            print(float(x))
        elif jh==2:
            y=Volumen(bas,alt,prof)
            print(float(y))
        elif jh==3:
            x=Area(bas,alt)
            y=Volumen(bas,alt,prof)
            print("El area es "+ (str(x)))
            print("El volumen es "+ (str(y)))
else:
    print("Error")
main()

if __name__=='__main__':
    main()
