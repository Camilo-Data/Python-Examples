squares = [x**2 for x in range (1,11)]
Cube = [x**3 for x in range (1,11)]
print("Los cuadrados son: ",squares)
print("Los Cubos son: ",Cube)

celsius = [x for x in range(0,1000)]
farenheit = [(temp * 9/5)*32 for temp in celsius ]
#print("Temperatura en farenheit es: ",farenheit)

#Numeros pares 

evens = [x for x in range(1,100) if x%2 == 0 ]
#print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix]for i in range(len(matrix[0]))]
print(matrix)
print(transposed)

#Codigo sin simplificacion - Comprehension list 

transposed = [] # lista vacia 
for i in range(len(matrix[0])): # iteraccion 
    transposed_row =[]
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)
print(transposed)