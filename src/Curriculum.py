import random
mails_registed = set("garyford@gmail.com")
ids_generates = set() #Automatic ID Generator for list length

def id():
    while True:
        idNum = random.randint(1, curriculum.__len__ + 9)
        idFormated = f"{idNum:04d}"
        if idFormated not in ids_generates:
            ids_generates.add(idFormated)
            return f"COMP{idFormated}"
curriculum = {
    id(): {
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
            "academic_training": {
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
            "profeccional_experiences": {
                [{
                    "company":"InPlease",
                    "rol":"FrontEnd Developer",
                    "duration_months":"13"
                    }]
            },
            "Certifications":{
                [{
                    "academic_center":"Cesde",
                    "years_coused": 1,
                    "qualification": "C# with data base"
                    }]
            },
            "idioma": ["Francés", "Ingles"],
            "Skills": ["Responsavility", "Adaptivility"]
        }
    },
    }

