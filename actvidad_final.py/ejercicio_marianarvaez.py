"""10. **Calculadora básica**
    Crea una función que reciba dos números y una operación (`"suma"`, `"resta"`, `"multiplicación"`, `"división"`) y devuelva el resultado correspondiente.
"""
#SOLUCION
def calculadora(numero1: float, numero2: float):

    print("\n\nMENU CALCULADORA")
    print("SUMA(+)\nRESTA(-)\nMULTIPLICACION(*)\nDIVISION (/)\n\n")
    
    operacion = input("Seleccione el signo de la operación: ")

    if operacion == "+":
        print(f"La suma es: {numero1 + numero2}")

    elif operacion == "-":
        print(f"La resta es: {numero1 - numero2}")

    elif operacion == "*":
        print(f"La multiplicación es: {numero1 * numero2}")

    elif operacion == "/":
        print(f"La división es: {numero1 / numero2}")

    else:
        print("Operación no válida")
        
calculadora(20, 15)