## Ciclo for 
##Es especial para recorrer estructuras de datos
##Todo lo que esta entre braques[] se denomina lista

#funcion range(python)
#crea una lista de numeros en el rango definido por el usuario

numero = int(input("Ingrese un numero: "))
for i in range(1,11):
    resultado = numero *i
    print(numero, "x",i,"=",resultado)