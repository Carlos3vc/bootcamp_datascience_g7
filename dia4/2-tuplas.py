#tupla son como listas pero inmutables
dias = ("lunes","martes","miercoles","jueves","viernes")
print(dias)
print(dias[0])
print(dias[1:3])
print(dias[-2])
print(dias[:])
print(type(dias))

#no permite apped directamente, se tiene que convertir a lista primero
dias = list(dias) 
print(type(dias))
dias.append("sabado")
dias.append("domingo")
dias = tuple(dias)
print(dias)