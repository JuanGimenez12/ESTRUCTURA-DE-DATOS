def suma():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")

def resta():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

def multiplicacion():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")

def division():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir por cero")

def menu_principal():
    while True:
        print("\n       Calculadora Grupo 1 EDD     ")
        print("-----------------------------------")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        opcion = input("Ingrese su opción: ")


        if opcion == "1":
            suma()
            print("1. Volver a Sumar")
            print("2. Volver al menú principal")
            sub_opcion = input("Ingrese su opción: ")
            if sub_opcion == "1":
                suma()
            elif sub_opcion == "2":
                return menu_principal()
            else:
                print("Opción inválida. Regresando al menú principal.")


        elif opcion == "2":
            resta()
            print("1. Volver a Restar")
            print("2. Volver al menú principal")
            sub_opcion = input("Ingrese su opción: ")
            if sub_opcion == "1":
                resta()
            elif sub_opcion == "2":
                return menu_principal()
            else:
                print("Opción inválida. Regresando al menú principal.")


        elif opcion == "3":
            multiplicacion()
            print("1. Volver a Multiplicar")
            print("2. Volver al menú principal")
            sub_opcion = input("Ingrese su opción: ")
            if sub_opcion == "1":
                multiplicacion()
            elif sub_opcion == "2":
                return menu_principal()
            else:
                print("Opción inválida. Regresando al menú principal.")

                
        elif opcion == "4":
            division()
            print("1. Volver a Dividir")
            print("2. Volver al menú principal")
            sub_opcion = input("Ingrese su opción: ")
            if sub_opcion == "1":
                division()
            elif sub_opcion == "2":
                return menu_principal()
            else:
                print("Opción inválida. Regresando al menú principal.")


        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, inténtelo de nuevo.")

menu_principal()
