n1 = input("ingresar numero 1: ")
n2 = input("ingresar numero 2: ")
n3 = input("ingresar numero 3: ")     
n4 = input("ingresar numero 4: ")
n5 = input("ingresar numero 5: ")

lista = []
lista.append(n1)  
lista.append(n2)  
lista.append(n3)  
lista.append(n4)  
lista.append(n5)  

mayor = max(lista)
menor = min(lista)
print ("El número mayor es ",mayor," y el menor es ",menor)

lista_ordenada = sorted(lista)
print(lista_ordenada)