texto = input("Ingresa un texto de al menos 10 palabras: ")
numCaracteres = len(texto)
numEspacios = texto.count(" ")
numCaracteresSinEspacios = numCaracteres - numEspacios
num_a = texto.count("a")
num_e = texto.count("e")
num_i = texto.count("i")
num_o = texto.count("o")
num_u = texto.count("u")
numVocales = num_a+num_e+num_i+num_o+num_u
numPalabras = texto.count(" ")+1
primerEspacio = texto.find(" ")
sinPrimeraPalabra = texto[primerEspacio+1:]
guiones = texto.replace(" ","-")
viceversa = texto.swapcase()
print(f"El numero de caracteres es: {numCaracteres}")
print(f"Y si no contamos los espacios tienes: {numCaracteresSinEspacios} caracteres")
print(f"De los caracteres hay {numVocales} vocales")
print(f"Las palabras en total son : {numPalabras} palabras")
print(f"Eliminando la primera palabra: {sinPrimeraPalabra}")
print(f"Si cambiamos espacios por guiones asi se ve: {guiones}")
print(f"Cambiando mayusculas por minusculas queda asi: {viceversa}")