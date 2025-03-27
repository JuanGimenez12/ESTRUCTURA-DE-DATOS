#CALCULADORA
def main():                                
    historial = HistorialNavegacion()   #Creamos la Instancia de la clase, las paginas del Historial

    for i in range(3):                  #creamos un Bucle for que se va a repetir 3 veces, para ingresar 3 paginas al Historial
        url = input(f"Ingrese la URL de la página {i+1}: ")  #Pedimos que ingresen por teclado la URL, para almacenarta como una instancia de la clase Pagina
        pagina = Pagina(url)                         #Creamos una Instancia de la Pagina con la URL ingresada
        historial.agregar_pagina(pagina)   #llamamos a la funcion agregar_pagina para agregar la pagina al historial
        print(historial)                  #Imprimimos la pagina agregada como pagina actual

    while True:                          #Utilizamos un bucle while, para mostrar el Menu de opciones
        print("\nOpciones:")     
        print("1. Retroceder")
        print("2. Avanzar")
        print("3. Salir")
        opcion = input("Ingrese su opción: ")  #espera la opcion a realizar 1,2 o 3

        if opcion == "1":
            pagina = historial.retroceder()   #llama a la funcion retroceder 
            if pagina:                        #Si hay una pagina la Imprime
                print(historial)
            else:
                print("No hay páginas atrás") #Si no imprime este mensaje, ya que no hay nada para mostrar
                print(historial)              #Imprime la pagina Actual
        elif opcion == "2":
            pagina = historial.avanzar()      #llama a la funcion avanzar
            if pagina:                        #la cual verifica que exista una paginaa la cual avanzar
                print(historial)              #la imprime
            else:
                print("No hay páginas adelante") #Si no existe, imprime el mensaje
                print(historial)              #Imprime la pagina Actual
        elif opcion == "3":    #se detiene el ciclo al ingresar un 3 y cierra el menu
            break
        else:
            print("Opción inválida") #al ingresar una opcion que no existe imprime el mensaje
            print(historial)              #Imprime la pagina Actual

if __name__ == "__main__":
    main()