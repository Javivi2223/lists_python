dog = []
menu_option = ""

while menu_option != "3" :
    print("1. inscribir cachorrito")
    print("2. ver cachorritos")
    print("3. salir")
    menu_option =input()

    if menu_option == "1" :
        dog = []
        name = input("Ingrese el nombre de su cachorrito: ")
        age = int(input("Ingrese la edad de su cachorrito: "))
        breed = input("Ingrese la raza de su cachorrito: ")
        dog.append(name)
        dog.append(age)
        dog.append(breed)
        dog.append(dog)
        print("cachorrito registrado con éxito")
        print("--------------------")

    elif menu_option == "2" :
        number = 0
        while number < len(dogs):
            print(f"el nombre: {dogs[number][0]}")
            print(f"la edad: {dogs[number][1]}")
            print(f"la raza: {dogs[number][2]}")
            print("-----------------")
            number += 1
    if menu_option == "3" :
        print("¡gracias por participar!")            