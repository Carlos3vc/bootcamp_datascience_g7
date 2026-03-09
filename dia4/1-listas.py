dias = ["lunes","martes","miercoles","jueves","viernes"]

print(dias)
print(dias[0])
print(dias[1:3])
print(dias[-2])
print(dias[:])

#agregar valores
dias.append("sabado")  
dias.append("domingo") 
print(dias)

#eliminar valores de lista
dias.pop() #elimina el ultimo elemento de la lista
print(dias)
dias.pop(3) #
print(dias)

#modidicar elementos
dias[3] = "test" #
print(dias)

#recorrer una lista con blucle for
print(f"total de la lista dias: {len(dias)}")
for contador in range(len(dias)):
    print(f"hoy es el {dias[contador]}")
    
"forma mejorada"  
for dia in dias:
    print(f'hoy es {dia}')  