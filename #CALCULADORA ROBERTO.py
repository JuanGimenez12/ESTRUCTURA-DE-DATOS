def suma():
    while True:
        num1 = input("\nIngrese el primer número: ")
        num2 = input("\nIngrese el segundo número: ")

        if not num1.isdigit() or not num2.isdigit():  # Verifica que sean numéricos
            print("\n⚠ Error: Debe ingresar solo números enteros positivos.")
            continue  # Repite la solicitud

        num1, num2 = int(num1), int(num2)  # Convierte a enteros

        if num1 < 0 or num2 < 0:  # Verifica que sean positivos
            print("\n⚠ Error: Debe ingresar solo números enteros POSITIVOS.")
            continue  # Repite la solicitud

        resultado = num1 + num2
        print(f"\nEl resultado de la suma es: {resultado}")
        break  # Sale del bucle al obtener datos válidos


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
        print(f"\nEl resultado de la división es: {resultado}")
    else:
        print("Error: No se puede dividir por cero")

def menu_principal():
    while True:
        print("\n      Calculadora BÁSICA -  Grupo 1 EDD     ")
        print("-------------------------------------------")
        print("\n[1] - SUMAR. ")
        print("\n[2] - RESTAR. ")
        print("\n[3] - MULTIPLICAR. ")
        print("\n[4] - DIVIDIR. ")
        print("\n[0] - SALIR DEL PROGRAMA ")
        opcion = input("\nSELECCIONAR UNA OPCIÓN [0 a 4] Y PRESIONAR ENTER: __  ")

        if not opcion.isdigit():  # Verifica si la entrada NO es numérica
            print("⚠ Error: Debe ingresar solo números entre 0 y 4.")
            continue  # Vuelve a pedir la opción

        if opcion == "1":
            while True:
                suma()  # Llama a la función suma

                print("\nS - Volver a Sumar")
                print("\nN - Volver al menú principal")
                sub_opcion = input("\nIngrese su opción: ").upper()  # Convierte a mayúsculas

                if sub_opcion == "S":
                    continue  # Repite la suma
                elif sub_opcion == "N":
                    return menu_principal()  # Vuelve al menú principal
                else:
                    print("Opción inválida. Regresando al menú principal.")
                    return menu_principal()


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


        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, inténtelo de nuevo.")

menu_principal()