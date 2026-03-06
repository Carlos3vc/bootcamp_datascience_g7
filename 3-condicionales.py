#calculadora
#programa para hacer operacion segun indicacion

#entrada
numero1 = int(input("numero 1 :"))
numero2 = int(input("numero 2 :"))
operacion = input("ingrese operacion: ")

#operacion
if operacion == "+":
    resultado = numero1 + numero2
elif operacion == "-":
    resultado = numero1 - numero2
elif operacion == "x":
    resultado = numero1 * numero2    
elif operacion == "/":
    resultado = numero1 / numero2   
else: 
    print("Operación no valida") 
    exit()
#salida
print(f'{numero1} {operacion} {numero2} = {resultado}')