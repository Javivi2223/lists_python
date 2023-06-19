grades =  [2.9, 2.7, 1.7, 4.3, 3.4]

#utilizando los metodos len() y for. calcular el promedio de las notas
sum = 0
for grade in grades:
    sum += grade

print(f"El promedio de notas es {sum/len(grades)}")    