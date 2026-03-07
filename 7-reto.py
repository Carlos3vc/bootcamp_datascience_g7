
opcion = 0
while (opcion != 3):
        print("=============================================")
        print("          CONVERTIDOR DE MONEDAS"             )
        print("=============================================")
        print("       [1] CONVERTIR SOLES A DOLARES         ")
        print("       [2] CONVERTIR DOLARES A SOLES         ")
        print("       [3] SALIR                             ")
        print("=============================================")

        opcion = int(input("Ingrese la opción que desee (1, 2, 3): "))
        if opcion == 1:
                monto = int(input("Ingrese el monto en soles a convertir: "))
                print("Tu monto es soles a convertir es: ")
                print(f'Tu monto es dolares es: {monto/3}')
        elif opcion == 2:
                monto = int(input("Ingrese el monto en dolares a convertir: "))
                print("Tu monto es dolares a convertir es: ")
                print(f'Tu monto es soles es: {monto*3}')
        elif opcion == 3:
                print("saldrá del convertidor")                
                break
        else:
                print("opción no valida...")
                
            
                