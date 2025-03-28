class Pagina:                  #
    def __init__(self, url):   #Constructor
        self.url = url         #Guarda como atributo las URL

    def __str__(self):        #Devuelve las URL como cadenas de texto para que sea mas legible
        return f"{self.url}"

class HistorialNavegacion:          #Creamos la clase HistorialNavegacion CON 3 PILAS
    def __init__(self):
        self.pagina_actual = None   #Pila en la que se almacenara la pagina Actual que estamos viendo
        self.pila_adelante = []     #Inicializamos una Lista vacia donde se Guardaran las paginas que se pueden volver a visitar
        self.pila_atras = []        #Inicializamos una Lista vacia donde se guardan las en las que se puede retroceder
        
    def agregar_pagina(self, pagina):    #Metodo para agregar una nueva Pagina al Historial y actualizar el estado de las pilas
        if self.pagina_actual:           #Si existe una pagina Actual, la desplaza a la Pila ATRAS
            self.pila_atras.append(self.pagina_actual)  #Para ingresar la nueva pagina al historial,hacemos el cambio
        self.pagina_actual = pagina         #Actualizamos la Pgina Actual con los Datos ingresados como Pagina

    def retroceder(self):
        if not self.pila_atras:           #Verifica que halla una pagina hacia atras a la cual retroceder 
            return None                   #sino no retorna nada
        self.pila_adelante.append(self.pagina_actual)  #La pagina Actual, la mueve hacia Adelante 
        self.pagina_actual = self.pila_atras.pop()     #extrae la Pagina que esta Atras y la mueve a la Pila Actual
        return self.pagina_actual                      #Retorna la nueva pagina Actual

    def avanzar(self):
        if not self.pila_adelante:        #Verifica que Exista un Pagina Hacia Adelante a la cual ir
            return None                   #sino no retorna nada
        self.pila_atras.append(self.pagina_actual) #La pagina Actual, la mueve hacia Atras
        self.pagina_actual = self.pila_adelante.pop() #Extrae la Pagina que esta en la Pila Adelante y la mueve a la Actual
        return self.pagina_actual                     #Retorna la nueva Actual

    def __str__(self):
        return f"Página actual: {self.pagina_actual}" #muestra cual es la pagina Activa en la Pantalla. Al retroceder o avanzar


#Main del Programa

def main():                                
    historial = HistorialNavegacion()   #Creamos la Instancia de la clase, las paginas del Historial

    for i in range(4):                  #creamos un Bucle for que se va a repetir 3 veces, para ingresar 3 paginas al Historial
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