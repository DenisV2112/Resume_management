
from ConsultCurriculum import *
from Curriculum import *
from Update import *
from Reports import *

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar hoja de vida")
    print("2. Consultar hojas de vida")
    print("3. Actualizar información")
    print("4. Generar reportes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case '1':
            register()
        case '2':
            consult_curriculum(curriculum)
        case '3':
            show_menu()
        case '4':
            reports(curriculum)
        case '5':
            print("Saliendo del sistema.")
            break
        case _:
            print("Opción inválida. Intente nuevamente.")