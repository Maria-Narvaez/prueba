#input () = + , - , * , /, datos alfabeticos
numero_uno = int(input("Por favor, ingrese un numero: "))
numero_dos = int(input("Por favor, ingrese otro numero: "))

print("Por favor, ingrese el operador de la calculadora: + , - , * , /")
opcion = input("Seleccione un operador: ")

#Condicionales: if, if-elif-else
if opcion =="+":
    print(f"El resultado de la suma es = {numero_uno + numero_dos}")
if opcion =="-":
    print(f"El resultado de la suma es = {numero_uno - numero_dos}")
if opcion =="*":
    print(f"El resultado de la suma es = {numero_uno * numero_dos}")
if opcion =="/":
    print(f"El resultado de la suma es = {numero_uno / numero_dos}")