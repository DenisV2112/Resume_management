# Resume_management

## Group: 
### Ritchie: Cristian Chaverra, Samuel Quintero
### Van Rossum: Denis Sanchez

## Documentation


### We desided to use git flow: 
#### - main: to the main production branch, representing the stable, released code. 
#### - feature: Branches created for developing specific features.
#### - hotfix: Branches created from main to address  bugs in the production code.


![alt text](image-1.png)



### Also to describe variables we use "snake_case" (variable_case) and "camelCase" (funtionName) to named def in the proyect.


![alt text](image-2.png)



## Library used:
1. • datetime (to calculate time of age and experiences)
2. • json (To export curriculums)


### Our proyect structure:

![alt text](image-3.png)

 ### Work Organization

#### • Jira [Link Text](#)

![alt text](Jira_Table-First-Sprim.png)

## About project:

Resume management system that allows you to record personal, educational, professional, reference, and other data, with options to view, update, and export each registered resume.

### Dependences:
#### Python 3.10 [Link Text](#https://www.python.org/downloads/)
#### or also you can watch this video: https://www.youtube.com/watch?v=cu_ykIfBprI(https://www.youtube.com/watch?v=9o4gDQvVkLU)

### Functions:
 1. Register new curriculum
 2. Get some curriculum from database
 3. Update the curriculum by ID, Name or Mail
 4. Create a Report 
 5. Close the program

### Simulated Data:
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

### Librarys:

`json`: To serialize and save data in `.json` files
`datetime`: To obtain report generation dates       



### How to run:

 1. Donwload Python 3.10
 2. Donwload Resume management zip
 3. Open cmd (Terminal) [Link text](#https://www.youtube.com/watch?v=JvHHgnOqW4w)
 4. Go to the folder with App and type in terminal *python App.py*
