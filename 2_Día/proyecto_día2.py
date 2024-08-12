nombre = "Jorge"
fecha = "12/08/2024"
saludo = "Buenas tardes"
bienvenida = saludo + ", " + nombre + ". " + "Como te puedo ayudar hoy: " + fecha 
dolares = 1568.15
euros_a_recibir = dolares * 0.88
billetes_10 = euros_a_recibir//10
billetes_1 = (euros_a_recibir-(billetes_10*10))//1
monedas = euros_a_recibir%1
entrega = "Se le entregaran " + str(billetes_10) + " billetes de 10, " + str(billetes_1) + " billetes de 1 y " + str(monedas) + " monedas." 
print(bienvenida)
print("Dolares a entregar:")
print(dolares)
print("Euros a recibir:")
print(euros_a_recibir)
print(entrega)
print("Muchas gracias por su dinero.")