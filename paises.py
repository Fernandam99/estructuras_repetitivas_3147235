paises = [
            {
                "nombre": "Venezuela",
                "capital": "Caracas",
                "monedad": "Bolibar",
                "superficie": 916.445,
                "poblacion": 
                 {
                    "censo": 31,  
                    "densidad": 26 
                 },
                 "ciudades":
                   [
                     "Caracas",
                     "Maracaibo",
                     "Valencia",
                     "Carabobo"
                   ],
            },
            {
                "nombre":"Brasil",
                "capital": "Brasilia",
                "moneda": "Real brasileño",
                "superficie": 8.51,
                "poblacion": 
                 {
                    "censo": 213,  
                    "densidad": 25 
                 },
                 "ciudades":
                   [
                     "São Paulo",
                     "Río de Janeiro",
                     "Brasilia"
                   ],
            },
            {
                "nombre":"Paraguay",
                "capital":"Asuncion",
                "moneda":"Guanani",
                "superficie": 406752,
                "poblacion": 
                 {
                    "censo": 7,  
                    "densidad": 18 
                 },
                 "ciudades":
                   [
                     "Asuncion",
                     "Cuidad del Este",
                     "Encarnación"
                   ],
            }
        ]

#Recoriendo todos los paises

print("recorido todos los paises")
for pais in paises:
    print("Cuidades principales: ")
    for  ciudad in pais["ciudades"]:
        print("-", ciudad)

    print("Nombre: ", pais["nombre"])
    print("Capital: ", pais["capital"])
    print("Censo: ",
          pais["poblacion"]["censo"],
          "millones")
    print("Densidad: ",
          pais["poblacion"]["densidad"],
          "por km2")
    print("Superficie: ", pais["superficie"])
  
    print("..........")