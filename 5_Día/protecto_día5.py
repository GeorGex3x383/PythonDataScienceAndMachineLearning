def generar_tablas(numero,limite):
    for num in range(1,limite+1):
        print(f"{numero} x {num} = {numero*num} ")

def inicio():
    while True:
        print("\nGenerador de tablas de multiplicar\n")
        num = int(input("Ingrese el numero que desee multiplicar: "))
        lim = int(input("Ingrese la cantidad de veces que desea multiplicarlo: "))
        generar_tablas(num,lim)
        
        op = input("\n¿Quieres calcular más tablas? (s/n) ")
        if op.lower() != "s":
            break
        
inicio()