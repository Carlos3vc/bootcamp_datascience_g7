contador = 1
while contador < 10:
    print(contador)
    contador += 1
    
numero_adivinar = 5
print("adivina el numero que estoy pensando")
while(contador != numero_adivinar):
    contador = int(input())
    if contador == numero_adivinar:
        print("acertaste")
    else:
        print("intenta de nuevo")
