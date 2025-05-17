from pprint import pprint
from Curriculum import curriculum

def add_experience(user_id):
    experience = {
        "company": input("Nombre de la empresa: "),
        "role": input("Rol desempeñado: "),
        "duration_months": int(input("Duración (meses): "))
    }
    curriculum[user_id]["professional_info"]["professional_experiences"].append(experience)
    print("Experiencia añadida correctamente.")


def add_education(user_id):
    training = {
        "academic_center": input("Centro académico: "),
        "years_coursed": int(input("Años cursados: ")),
        "qualification": input("Título obtenido: ")
    }
    curriculum[user_id]["professional_info"]["academic_training"].append(training)
    print("Formación añadida correctamente.")


def edit_contact(user_id):
    key = input("¿Qué dato de contacto deseas editar? (mail/phone/city/state/postal_code/country): ").strip().lower()
    if key in ["mail", "phone"]:
        curriculum[user_id]["contact"][key] = input(f"Nuevo valor para {key}: ")
    elif key in curriculum[user_id]["contact"]["address"]:
        curriculum[user_id]["contact"]["address"][key] = input(f"Nuevo valor para {key}: ")
    else:
        print("Campo no válido.")
        return
    print("Dato de contacto actualizado correctamente.")


def update_skills(user_id):
    new_skill = input("Nueva habilidad a agregar: ")
    curriculum[user_id]["professional_info"]["skills"].append(new_skill)
    print("Habilidad agregada.")


def update_references(user_id):
    curriculum[user_id]["references"] = {
        "name": input("Nombre de la referencia: "),
        "relation": input("Relación: "),
        "phone": input("Teléfono: ")
    }
    print("Referencia actualizada.")


def ver_curriculum(user_id):
    print(f"\n--- Hoja de Vida de {curriculum[user_id]['name']} {curriculum[user_id]['lastname']} ---")
    pprint(curriculum[user_id])


def show_menu():
    user_id = input("Ingresa el ID del usuario: ")
    if user_id not in curriculum:
        print("ID no encontrado.")
        return

    while True:
        print("\n--- Menú de Actualización ---")
        print("1. Añadir nueva experiencia")
        print("2. Añadir nueva formación")
        print("3. Editar datos de contacto")
        print("4. Agregar habilidad")
        print("5. Cambiar referencias")
        print("6. Ver hoja de vida")
        print("7. Salir")
        option = input("Selecciona una opción: ")

        if option == "1":
            add_experience(user_id)
        elif option == "2":
            add_education(user_id)
        elif option == "3":
            edit_contact(user_id)
        elif option == "4":
            update_skills(user_id)
        elif option == "5":
            update_references(user_id)
        elif option == "6":
            ver_curriculum(user_id)
        elif option == "7":
            print("Saliendo del menú.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecuta el menú
show_menu()