
from datetime import datetime
from IdGenerator import *
from MailSetValidator import *

curriculum = {
    "00000": {
        "name": "Daniel",
        "lastname": "Herrera",
        "birthday":("1987-07-15"),
        "id":("21909218219"),
        "contact": {
            "mail": "garyford@gmail.com",
            "phone": "001-512-801-0651",
            "adress": {
                "city": "Gonzalezmouth",
                "state": "Michigan",
                "postal_code": "92488",
                "country": "Bermuda"
            }
        },
        "references": {
            "name": "bradley",
            "relation": "coworker",
            "phone": "320-580-0647",
        },
        "professional_info":{
            "academic_training": 
                [{
                     "academic_center":"Andre Eloy",
                     "years_coused": 9,
                     "qualification": "C# with data base"
                     },
                {
                     "academic_center":"Cesde",
                     "years_coused": 1,
                     "qualification": "C# with data base"
                     }]
            },
            "profession_experiences": 
                [{
                    "company":"InPlease",
                    "rol":"FrontEnd Developer",
                    "duration_months":"13"
                     }, {
                    "company":"InPlease",
                    "rol":"FrontEnd Developer",
                    "duration_months":"13"
                    }],
            "Certifications":
                [{
                    "academic_center":"Cesde",
                    "years_coused": 1,
                    "qualification": "C# with data base"
                    }]
            ,
            "idioma": ["Francés", "Ingles"],
            "Skills": ["Responsavility", "Adaptivility"]
        }
    }

def calculate_age(birthday):
    today = datetime.today()
    birthday = datetime.strptime(birthday, "%Y-%m-%d")
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def calculate_work_duration(start_date, end_date=None):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if end_date is None:
        end_date = datetime.today()
    else:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    duration = end_date - start_date
    years = duration.days // 365
    months = (duration.days % 365) // 30
    return f"{years} años y {months} meses"

def register():
    print("\n--- Registro de Hoja de Vida ---\n")
    # Datos personales
    name = input("Nombre: ")
    lastname = input("Apellido: ")
    birthday = input("Fecha de nacimiento (YYYY-MM-DD): ")
    age = calculate_age(birthday)
    document = input("Número de documento: ")
    
    # Contacto
    mail = input("Correo electrónico: ")
    phone = input("Teléfono: ")
    city = input("Ciudad: ")
    state = input("Estado/Departamento: ")
    code_postal = input("Código postal: ")
    country = input("País: ")
    
    # Referencias
    references_name = input("Nombre de referencia: ")
    references_relation = input("Relación con la referencia: ")
    references_phone = input("Teléfono de la referencia: ")
    
    # Formación académica
    academic_training = []
    while True:
        print("\n-- Formación académica --")
        center = input("Centro académico: ")
        start_date = input("Fecha de inicio (YYYY-MM-DD): ")
        end_date = input("Fecha de fin (YYYY-MM-DD): ")
        qualification = input("Título/Certificación obtenida: ")
        duration = calculate_work_duration(start_date, end_date)
        academic_training.append({
            "academic_center": center,
            "duration": duration,
            "qualification": qualification
        })
        back_menu = input("¿Desea agregar otra experiencia? (s/n): ").lower()
        if back_menu != "s":
            break
    
    # Experiencia profesional
    experiences = []
    while True:
        print("\n-- Experiencia profesional --")
        company = input("Empresa: ")
        rol = input("Rol/Cargo: ")
        start_date = input("Fecha de inicio (YYYY-MM-DD): ")
        end_date = input("Fecha de fin (YYYY-MM-DD) o presiona Enter si aún trabajas aquí: ")
        if end_date == "":
            end_date = None
        duration = calculate_work_duration(start_date, end_date)
        experiences.append({
            "company": company,
            "rol": rol,
            "duration": duration
        })
        back_menu = input("¿Desea agregar otra experiencia? (s/n): ").lower()
        if back_menu != "s":
            break
    
    # Certificaciones
    certifications = []
    while True:
        print("\n-- Certificación --")
        center = input("Centro educativo: ")
        years = int(input("Duración (años): "))
        qualification = input("Título de la certificación: ")
        certifications.append({
            "academic_center": center,
            "years_coused": years,
            "qualification": qualification
        })
        back_menu = input("¿Desea agregar otra experiencia? (s/n): ").lower()
        if back_menu != "s":
            break
    
    # Idiomas
    lenguages = input("\nIdiomas (separados por coma): ").split(",")
    
    # Habilidades
    skills = input("Habilidades (separadas por coma): ").split(",")
    
    # Registro en el diccionario
    curriculum[id] = {
        "name": name.strip(),
        "lastname": lastname.strip(),
        "birthday": birthday,
        "age": age,
        "id": document,
        "contact": {
            "mail": mail,
            "phone": phone,
            "adress": {
                "city": city,
                "state": state,
                "postal_code": code_postal,
                "country": country
            }
        },
        "references": {
            "name": references_name,
            "relation": references_relation,
            "phone": references_phone,
        },
        "professional_info": {
            "academic_training": academic_training,
            "profession_experiences": experiences,
            "Certifications": certifications,
            }}
