shopping_list = []
menu_option = ""

while menu_option != "4":

    print("Lista de compras")    
    print("1. agregar")
    print("2. quitar")
    print("3. ver")
    print("4. salir")

    menu_option = input()
    if menu_option == "1":
      # Agregamos elementos a la lista
      producto = input("agrega lo que necesites comprar: ")
      shopping_list.append(producto)
      print("producto agregado con éxito.")
      print("-----------------------------")  

    elif menu_option == "2":
      producto = input("¿qué producto desea eliminar?: ")  
      shopping_list.remove(producto)


    elif menu_option == "3":
       # Mostrar todo el contenido de shopping_list
       for producto in shopping_list:
        print(producto)
       

    elif menu_option == "4":
       print("Chao chao")

    else:
        print("Selecciona una opción válida")    
