#las llaves nos infican que es un diccionario por lo que el int valida un significado despues de los dos pintos
numbers = {1:"uno",2:"dos",3:"tres"}

print(numbers)

print(numbers[2])

information = {"Nombre":"Camilo",
               "Apellido":"Molina",
               "Altura":1.68,
               "Edad": 25,
               }

print(information)
del information ["Altura"]
print(information)

claves = information.keys()

print(claves)
print(type(claves))

values = information.values()
print(values)

pairs = information.items()
print(pairs)

contacto = {"Camilo":{"Apellido":"Molina",
            "Altura":1.68,
            "Edad": 25,
               },
            "Katleen": {"Apellido":"De dios",
             "Altura":1.70,
            "Edad":24},
            "Carla": {"Apellido":"Florida",
             "Altura":160,
             "Edad": 29},
             "Laura": {"Apellido":"Garcia",
             "Altura":163,
             "Edad": 22}
               }


print(contacto["Camilo"])
print(contacto["Katleen"])
print(contacto["Carla"])
print(contacto["Laura"])