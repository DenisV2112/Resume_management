
def validar_entrada_menu(opcion, opciones_validas):
    """Valida que la opción del menú sea una de las permitidas."""
    opcion = opcion.strip()
    if opcion not in opciones_validas:
        print("Error: Opción inválida.")
        return False
    return True

def validar_criterio_busqueda(criterio):
    """Valida que el criterio de búsqueda sea uno de los permitidos."""
    criterios_validos = ["nombre", "documento", "correo"]
    if criterio.lower() not in criterios_validos:
        print("Error: Criterio de búsqueda inválido. Debe ser 'nombre', 'documento' o 'correo'.")
        return False
    return True

def validar_entero_positivo(valor, nombre_campo):
    """Valida que un valor sea un entero positivo."""
    valor = valor.strip()
    try:
        valor_int = int(valor)
        if valor_int < 0:
            print(f"Error: {nombre_campo} debe ser un número entero no negativo.")
            return False
        return True
    except ValueError:
        print(f"Error: Ingrese un número entero válido para {nombre_campo}.")
        return False

def validar_flotante_positivo(valor, nombre_campo):
    """Valida que un valor sea un número flotante positivo."""
    valor = valor.strip()
    try:
        valor_float = float(valor)
        if valor_float < 0:
            print(f"Error: {nombre_campo} debe ser un número no negativo.")
            return False
        return True
    except ValueError:
        print(f"Error: Ingrese un número válido para {nombre_campo}.")
        return False

def buscar_hoja_de_vida(curriculum, criterio, valor):
    """Busca hojas de vida en 'curriculum' por el 'criterio' y 'valor'."""

    resultados = []
    for id_hv, hv in curriculum.items():
        if criterio == "nombre" and valor.lower() in hv["name"].lower():
            resultados.append((id_hv, hv))
        elif criterio == "documento" and valor == hv["id"]:
            resultados.append((id_hv, hv))
        elif criterio == "correo" and valor.lower() == hv["contact"]["mail"].lower():
            resultados.append((id_hv, hv))
    return resultados

def filtrar_hojas_de_vida(curriculum, filtros):
    """Filtra hojas de vida en 'curriculum' según los 'filtros'."""

    resultados = []
    for id_hv, hv in curriculum.items():
        cumple_filtros = True
        if "años_experiencia" in filtros:
            experiencia_total_meses = 0
            for exp in hv["professional_info"]["profeccional_experiences"]:
                experiencia_total_meses += int(exp["duration_months"])
            experiencia_total_años = experiencia_total_meses / 12
            if experiencia_total_años < filtros["años_experiencia"]:
                cumple_filtros = False
        if "formacion" in filtros:
            formaciones = [form["qualification"].lower() for academic_group in hv["professional_info"].get("academic_training", []) for form in academic_group]
            if filtros["formacion"] not in formaciones:
                cumple_filtros = False
        if "habilidades" in filtros:
            if not all(h in [skill.lower() for skill in hv["professional_info"]["Skills"]] for h in filtros["habilidades"]):
                cumple_filtros = False
        if cumple_filtros:
            resultados.append((id_hv, hv))
    return resultados

def visualizar_hoja_de_vida(hoja_de_vida, seccion=None):
    """Muestra la 'hoja_de_vida' en formato legible."""

    def imprimir_seccion(titulo, datos):
        print(f"\n--- {titulo} ---")
        if isinstance(datos, list):
            for item in datos:
                if isinstance(item, dict):
                    for clave, valor in item.items():
                        print(f"  {clave.capitalize()}: {valor}")
                else:
                    print(f"  {item}")
        elif isinstance(datos, dict):
            for clave, valor in datos.items():
                print(f"  {clave.capitalize()}: {valor}")
        else:
            print(f"  {datos}")

    if seccion:
        seccion = seccion.lower()
        if seccion == "datos_personales":
            imprimir_seccion("Datos Personales", {"name": hoja_de_vida["name"], "lastname": hoja_de_vida["lastname"], "birthday": hoja_de_vida["birthday"], "id": hoja_de_vida["id"]})
            # Imprimir contacto formateado
            print("\n--- Contacto ---")
            print(f"  Mail: {hoja_de_vida['contact']['mail']}")
            print(f"  Phone: {hoja_de_vida['contact']['phone']}")
            print("  Adress:")
            print(f"    City: {hoja_de_vida['contact']['adress']['city']}")
            print(f"    State: {hoja_de_vida['contact']['adress']['state']}")
            print(f"    Postal Code: {hoja_de_vida['contact']['adress']['postal_code']}")
            print(f"    Country: {hoja_de_vida['contact']['adress']['country']}")

        elif seccion == "referencias":
            imprimir_seccion("Referencias", hoja_de_vida["references"])
        elif seccion == "formacion_academica":
            imprimir_seccion("Formación Académica", hoja_de_vida["professional_info"].get("academic_training", []))
        elif seccion == "experiencia_profesional":
            imprimir_seccion("Experiencia Profesional", hoja_de_vida["professional_info"].get("profeccional_experiences", []))
        elif seccion == "certificaciones":
            imprimir_seccion("Certificaciones", hoja_de_vida["professional_info"].get("Certifications", []))
        elif seccion == "idiomas":
            imprimir_seccion("Idiomas", hoja_de_vida["professional_info"].get("idioma", []))
        elif seccion == "habilidades":
            imprimir_seccion("Habilidades", hoja_de_vida["professional_info"].get("Skills", []))
        else:
            print(f"Error: Sección '{seccion}' no encontrada.")
    else:
        print("--- Hoja de Vida Completa ---")
        imprimir_seccion("Datos Personales", {"name": hoja_de_vida["name"], "lastname": hoja_de_vida["lastname"], "birthday": hoja_de_vida["birthday"], "id": hoja_de_vida["id"]})
        # Imprimir contacto formateado
        print("\n--- Contacto ---")
        print(f"  Mail: {hoja_de_vida['contact']['mail']}")
        print(f"  Phone: {hoja_de_vida['contact']['phone']}")
        print("  Adress:")
        print(f"    City: {hoja_de_vida['contact']['adress']['city']}")
        print(f"    State: {hoja_de_vida['contact']['adress']['state']}")
        print(f"    Postal Code: {hoja_de_vida['contact']['adress']['postal_code']}")
        print(f"    Country: {hoja_de_vida['contact']['adress']['country']}")
        imprimir_seccion("Referencias", hoja_de_vida["references"])
        imprimir_seccion("Formación Académica", hoja_de_vida["professional_info"].get("academic_training", []))
        imprimir_seccion("Experiencia Profesional", hoja_de_vida["professional_info"].get("profeccional_experiences", []))
        imprimir_seccion("Certificaciones", hoja_de_vida["professional_info"].get("Certifications", []))
        imprimir_seccion("Idiomas", hoja_de_vida["professional_info"].get("idioma", []))
        imprimir_seccion("Habilidades", hoja_de_vida["professional_info"].get("Skills", []))

def consult_curriculum(curriculum):
    while True:
        print("\n--- Consultar Hojas de Vida ---")
        print("1. Buscar hoja de vida")
        print("2. Filtrar hojas de vida")
        print("3. Visualizar hoja de vida")
        print("4. Salir")

        while True:  # Bucle para validar la opción del menú
            opcion = input("Seleccione una opción: ").strip()
            if validar_entrada_menu(opcion, ["1", "2", "3", "4"]):
                break
            print("Por favor, ingrese una opción válida del menú.")

        if opcion == "1":
            while True:  # Bucle para validar el criterio de búsqueda
                criterio = input("Ingrese el criterio de búsqueda (nombre, documento, correo): ").strip()
                if validar_criterio_busqueda(criterio):
                    break
                print("Por favor, ingrese un criterio válido (nombre, documento, correo).")
            
            valor = input(f"Ingrese el valor a buscar por {criterio}: ").strip()
            resultados = buscar_hoja_de_vida(curriculum, criterio, valor)
            if resultados:
                print("Resultados de la búsqueda:")
                for i, (id_hv, resultado) in enumerate(resultados):
                    print(f"  {i + 1}. {resultado['name']} ({resultado['id']})")
                
                while True:  # Bucle para validar la selección de la hoja de vida
                    seleccion = input("Ingrese el número de la hoja de vida a visualizar (o 0 para volver): ").strip()
                    if validar_entero_positivo(seleccion, "Selección") and (0 <= int(seleccion) <= len(resultados)):
                        seleccion_int = int(seleccion)
                        if seleccion_int != 0:
                            visualizar_hoja_de_vida(resultados[seleccion_int - 1][1])
                        break
                    print("Por favor, ingrese una selección válida.")
            else:
                print("No se encontraron hojas de vida con ese criterio.")

        elif opcion == "2":
            filtros = {}
            while True:  # Bucle para validar años de experiencia
                años_experiencia_str = input("Ingrese años de experiencia mínimos (o deje vacío para omitir): ").strip()
                if años_experiencia_str == "":
                    break  # Permitir campo vacío
                if validar_flotante_positivo(años_experiencia_str, "Años de experiencia"):
                    filtros["años_experiencia"] = float(años_experiencia_str)
                    break
                print("Por favor, ingrese un número válido para años de experiencia.")
            
            formacion = input("Ingrese formación requerida (o deje vacío para omitir): ").strip()
            if formacion:
                filtros["formacion"] = formacion.lower()
            habilidades_str = input("Ingrese habilidades requeridas (separadas por coma, o deje vacío para omitir): ").strip()
            if habilidades_str:
                filtros["habilidades"] = [h.strip().lower() for h in habilidades_str.split(",")]

            resultados = filtrar_hojas_de_vida(curriculum, filtros)
            if resultados:
                print("Resultados del filtro:")
                for i, (id_hv, resultado) in enumerate(resultados):
                    print(f"  {i + 1}. {resultado['name']} ({resultado['id']})")
                
                while True:  # Bucle para validar la selección de la hoja de vida
                    seleccion = input("Ingrese el número de la hoja de vida a visualizar (o 0 para volver): ").strip()
                    if validar_entero_positivo(seleccion, "Selección") and (0 <= int(seleccion) <= len(resultados)):
                        seleccion_int = int(seleccion)
                        if seleccion_int != 0:
                            visualizar_hoja_de_vida(resultados[seleccion_int - 1][1])
                        break
                    print("Por favor, ingrese una selección válida.")
            else:
                print("No se encontraron hojas de vida que cumplan con los filtros.")

        elif opcion == "3":
            print("Lista de Hojas de Vida:")
            for i, (id_hv, hv) in enumerate(curriculum.items()):
                print(f"  {i + 1}. {hv['name']} ({hv['id']})")
            
            while True:  # Bucle para validar la selección de la hoja de vida
                seleccion = input("Ingrese el número de la hoja de vida a visualizar: ").strip()
                if validar_entero_positivo(seleccion, "Selección") and (0 < int(seleccion) <= len(curriculum)):
                    seleccion_int = int(seleccion)
                    hoja_de_vida_id = list(curriculum.keys())[seleccion_int - 1]
                    seccion = input("Ingrese la sección a visualizar (o deje vacío para ver la hoja de vida completa): ").strip()
                    visualizar_hoja_de_vida(curriculum[hoja_de_vida_id], seccion.lower() if seccion else None)
                    break
                print("Por favor, ingrese una selección válida.")

        elif opcion == "4":
            print("Saliendo...")
            break