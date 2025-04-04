#Ejercio 1
#imprimir la tabla de multiplicar del numero que un usuario ingrese por teclado, utilizado el ciclo while

#variable contadora

numero = int(input("Ingrese un numero: "))

i=10

while i>=10:
    resultado = numero* i
    print(numero, "x" , i, " = ", resultado)
    ##instruccion de incremento
    i = i - 1
    