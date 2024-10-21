to_do = ["Dirigirnos al hotel",
       "ir a almozar",
       "visitar el museo",
       "Volver al hotel"] 
print(to_do)
numbers =[1,2,3,4,5, "Seis"]
print(numbers)
mix = ["uno",2,3,3.14,True,[1,2,3]]
print(mix)
print(len(mix))
print("Primer elemento: ", mix[0])
print("Primer elemento: ", mix[1])
print("Primer elemento: ", mix[2])
string = "Hola mundo"
print("Primer elemento: ", string[0])
print("Primer elemento: ", string[1])
print("Primer elemento: ", string[-1])
print(mix[:6])
#Añadir a la lista 
print(mix)
mix.append(False)
print(mix[6])

#Insertar en una posicion especifica 
mix.insert(1,["a","b","c"])
print(mix)


#Condicionar el resultado 

numbers_2 =[1,2,3,4,5,6,7,165344]

print("mayor",max(numbers_2))
print("menor",min(numbers_2))

#Borrar datos de la lista 

del numbers_2 [0]
del numbers_2 [2]
del numbers_2 [-3]

print(numbers_2)


