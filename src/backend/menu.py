

def check_int(massage) :#Esta función se encarga de verificar que lo ingresado por el usuario sea realmente un número entero para poder convertirlo y agregarlo al valor del producto.
    entry = check_str(massage)
    if entry.isdigit():
        return int(entry)
    else :
        print("Dato ingresado invalido!")
        return check_int(massage)

def check_str(massage):#Esta función verifica que el valor ingresado no esté vacío.


    entry = input(massage).strip()
    if entry == "":
        print(" no puede estar vacio!")
        return check_str(massage)
    else :
        return entry


from colorama import init, Fore, Style




init()

print(f"""
 ------------------------
 | {Fore.BLUE} Menú principal {Style.RESET_ALL}     |
 |----------------------|
 | {Fore.GREEN} 1. Añadir {Style.RESET_ALL}          |
 | {Fore.GREEN} 2. Consultar {Style.RESET_ALL}       | 
 | {Fore.GREEN} 3. Generar Reporte {Style.RESET_ALL} |
 | {Fore.GREEN} 4. Actualizar {Style.RESET_ALL}      |
 | {Fore.GREEN} 5. Salir {Style.RESET_ALL}           |
 ------------------------""")

option = check_int("Ingrese la opcion a realizar: ")

match option : 
    case 1:
        print("1")

    case 2:
        print("1")

    case 3:
        print("1")

    case 4:
        print("1")
    
    case 5:
        exit

    case _:
        print("")