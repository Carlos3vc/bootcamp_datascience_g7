import os
from time import sleep

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""
ANCHO = 50

dic_alumnos = {
    '12345678':{
        'nombre':'Juan Perez',
        'email':'juanperez@gmail.com'
    },
    '10010010':{
        'nombre':'Ana Lopez',
        'email':'analopez@gmail.com'
    }
}

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE ALUMNOS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR ALUMNO
         [2] MOSTRAR ALUMNOS
         [3] ACTUALIZAR ALUMNO
         [4] ELIMINAR ALUMNO
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR ALUMNO")
        print("=" * ANCHO)
        
        codigo = input("INGRESE DNI : ")
        nombre = input("INGRESE NOMBRE : ")
        email = input("INGRESE EMAIL : ")
        dic_nuevo_alumno = {
            'nombre':nombre,
            'email':email
        }
        dic_alumnos[codigo] = dic_nuevo_alumno
        print("Alumno registrado exitosamente.")
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR ALUMNOS")
        print("=" * ANCHO)
        
        for codigo,info in dic_alumnos.items():
            print(f"DNI : {codigo}")
            print(f"NOMBRE : {info['nombre']}")
            print(f"EMAIL : {info['email']}")
            print("*"*ANCHO)
            
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR ALUMNO")
        print("=" * ANCHO)
        
        codigo = input("INGRESE DNI : ")
        os.system("clear")
        if codigo in dic_alumnos:
            
            info = dic_alumnos[codigo]
            
            print(f"DNI : {codigo}")
            print(f"NOMBRE : {info['nombre']}")
            print(f"EMAIL : {info['email']}")
            print("*"*ANCHO)
        else:
            print("No existe código")   
            break
        nombre_act= input("INGRESE NOMBRE A ACTUALIZAR : ")
        email_act = input("INGRESE EMAIL A ACTUALIZAR : ")
        dic_info_act = {
            'nombre':nombre_act,
            'email':email_act
        }
        
        os.system("clear")
        print("*"*ANCHO)             
        info.update(dic_info_act)
        print("Alumno actualizado exitosamente.")
        print(f"DNI : {codigo}")
        print(f"NOMBRE : {info['nombre']}")
        print(f"EMAIL : {info['email']}")
        print("*"*ANCHO)
        
        

    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR ALUMNO")
        print("=" * ANCHO)
        
        codigo = input("INGRESE DNI DE ALUMNO A ELIMINAR: ")
        os.system("clear")
        if codigo in dic_alumnos:
            info = dic_alumnos[codigo]
            del_nombre = info['nombre']
            del_email = info['email']
            del_alumno = dic_alumnos.pop(codigo)
            
            os.system("clear")   
            print("*"*ANCHO)             

            print("Alumno eliminado exitosamente.")                    
            print(f"DNI : {codigo}")
            print(f"NOMBRE : {del_nombre}")
            print(f"EMAIL : {del_alumno}")
            print("*"*ANCHO)
        else:
            print("No existe código")   
            break
  
                
        
        
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")