#Diccionario
#coleccion de datos que los almacena en pares
#clave-valor
#un diccionario comienza y termina con llaves (curly braces)
#la calve se separa del valor con dos puntos (:)
#cda calve es un string 
#el valor puede sr de cualquier tipo
#cada elemento (propiedad) del diccionario se separa por una coma

#ejemplo: diccionario que almacene los datos de un pais

pais1 = {
            "nombre": "Argentina",
            "capital": "Buenos Aires",
            "moneda": "peso argentino",
            "ciudades": [
                            "Cordoba",
                            "Rosario",
                            "Mendoza",
                        ],
            "poblacion":{
                            "censo": 45,
                            "densidad": 17,
                        }
        }

pais2= {
            "nombre": "Peru",
            "capital": "Quito",
            "moneda": "Dolar",
            "ciudades": [
                            "Guayaquil",
                            "Machala",
                            "Santo Domingo",
                        ],
            "poblacion":{
                            "censo": 18,
                            "densidad": 64,
                        }
        }

pais3= {
            "nombre": "Paraguay",
            "capital": "Asuncion",
            "moneda": "Guarani",
            "ciudades": [
                            "Montevideo",
                            "Concepción",
                            "Villarica",
                        ],
            "poblacion":{
                            "censo": 46,
                            "densidad": 16,
                        }
        }
#Acceder a la informacion del pais
print(pais2["capital"])
print(pais1["moneda"])

#acceder a una ciudad de pais 1
print(pais1["ciudades"][2])
#interar las ciudades del pais 1
for ciudad in pais1["ciudades"]:
    print(ciudad)
#interar las ciudades del pais 2
for ciudad in pais2["ciudades"]:
    print(ciudad)
#interar las ciudades del pais 3
for ciudad in pais3["ciudades"]:
    print(ciudad)

#accceder a datos poblaccionales
print("..........")
print("Censo:" , 
      pais1["poblacion"]["censo"],
      "millones de habitantes")
print("Densidad:" , 
      pais1["poblacion"]["densidad"],
      "densidad por metro cuadrado")