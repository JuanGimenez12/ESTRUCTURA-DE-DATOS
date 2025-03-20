class Pagina:
    def __init__(self, url, titulo):
        self.url = url
        self.titulo = titulo

    def __str__(self):
        return f"{self.titulo} - {self.url}"

class HistorialNavegacion:
    def __init__(self):
        self.pila_adelante = []
        self.pila_atras = []
        self.pagina_actual = None

    def agregar_pagina(self, pagina):
        if self.pagina_actual:
            self.pila_atras.append(self.pagina_actual)
        self.pagina_actual = pagina
        self.pila_adelante.clear()

    def retroceder(self):
        if not self.pila_atras:
            return None
        self.pila_adelante.append(self.pagina_actual)
        self.pagina_actual = self.pila_atras.pop()
        return self.pagina_actual

    def avanzar(self):
        if not self.pila_adelante:
            return None
        self.pila_atras.append(self.pagina_actual)
        self.pagina_actual = self.pila_adelante.pop()
        return self.pagina_actual

    def __str__(self):
        return f"Página actual: {self.pagina_actual}\nAtrás: {self.pila_atras}\nAdelante: {self.pila_adelante}"

def main():
    historial = HistorialNavegacion()

    for i in range(4):
        url = input(f"Ingrese la URL de la página {i+1}: ")
        titulo = input(f"Ingrese el título de la página {i+1}: ")
        pagina = Pagina(url, titulo)
        historial.agregar_pagina(pagina)
        print(historial)

    while True:
        print("\nOpciones:")
        print("1. Retroceder")
        print("2. Avanzar")
        print("3. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            pagina = historial.retroceder()
            if pagina:
                print(historial)
            else:
                print("No hay páginas atrás")
        elif opcion == "2":
            pagina = historial.avanzar()
            if pagina:
                print(historial)
            else:
                print("No hay páginas adelante")
        elif opcion == "3":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()