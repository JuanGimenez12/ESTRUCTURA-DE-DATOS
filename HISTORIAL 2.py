# EDD Pila
class Pila():
    # el usuario que use nuestra EDD se encuentra abstraido toda esta seccion
    def __init__(self): # Constructor 
        self.items = [] # inicailizamos una lista vacia al momento de crear nuetra pila
        self.size = 0 # inicializamos un contador el cual nos va a ayudar para saber si 
        # la pila cuenta con elementos cargardos
    
    #modificadoras # estas son todas la funciones que modifican internamente nuestra EDD
    def apilar(self,item):
        self.items.append(item) # agregamos el elemento dentro de la pila
        self.size +=1 # incrementamos en uno el tamaño de la pila
        return item # devolvemos el item agregado a la pila

    def desapilar(self):
        if self.esta_vacia(): # si no hay elementos para quitar mostramos el print
            return "La pila esta vacia"
        else: # si no 
            self.size -=1 # decrementamos en 1 el tamaño de la pila
            return self.items.pop() # devolvemos el elemento quitado de la pila

    # consultores # estas son todas la funciones que NO modifican internamente nuestra EDD
    def esta_vacia(self): # devolvemos True si la pila esta vacia o False si existe 1 o mas elementos dentro
        return self.size == 0
    
    def tamano(self):
        return self.size # devolvemos la cantidad de elementos dentro de la pila este numero se encuentra entre 0 o N
    
    def cima(self): #en caso de que no existan elementos dentro de la pila mostramos "La pila esta vacia"
        if self.esta_vacia():
            return "La pila esta vacia"
        else: # si existe por lo menos un elemento mostramos el elemento 1 o si hay N elemento mostramos el ultimo apilado
            return self.items[-1]
    

# inicio de las pruebas # esto es lo que ve el usuario que utiliza nuestra EDD
pila = Pila() # creamos la variable pila llamando a la clase Pila
print("La pila esta vacia?: ",pila.esta_vacia()) # mostramos por pantalla el estado actual de la pila
# al no contener elementos esta devuelve True

# comenzamos a apilar datos dentro de la pila
print("---------------------------------")

print("apilamos PAGINA 1: ",pila.apilar("WWW.YOUTUBE.COM"))
print("apilamos PAGINA 2: ",pila.apilar("WWWW.TWICH.COM"))
print("apilamos PAGINA 3: ",pila.apilar("WWW.INFOBAE.COM"))
print("apilamos PAGINA 4: ",pila.apilar("WWW.LANACION.COM"))

print("Elementos en el Hisotiral: ",pila.tamano())

print("-----------------------------")

print("Pagina Actual: ",pila.cima())

print("---------------------------------")

print("Una pagina hacia atras: ")
pila.desapilar()

print("---------------------------------")

print("Pagina Actual: ",pila.cima())

print("---------------------------------")

print("Una Pagina Hacia Adelante: ")
pila.apilar("WWW.LANACION.COM")

print("---------------------------------")

print("Pagina Actual: ",pila.cima())

print("---------------------------------")

print("3 Pagina Hacia Atras: ")
for i in range(3):
    pila.desapilar()
print("Pagina Actual: ",pila.cima())
pila.apilar("WWWW.TWICH.COM")
pila.apilar("WWW.INFOBAE.COM")
pila.apilar("WWW.LANACION.COM")

print("Elementos en el Hisotiral: ",pila.tamano())
print("...................")
print("Pagina Actual: ",pila.cima())








