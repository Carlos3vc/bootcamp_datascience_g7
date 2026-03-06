#permite repetir sentencias de codigo una determinada cantidad de veces
# for (valor inicial, valor final, incremento)
for contador in range(1,10,2):
    print (contador)
    
#hacer tabla de multiplicar
#entrada
tabla = int(input("ingrese tabla de multiplicar: "))
#proceso
for contador in range(1,13,1):
    resultado = tabla * contador
    print(f'{tabla} x {contador} = {resultado}')