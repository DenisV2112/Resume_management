import random
ids_generates = set() #Automatic ID Generator for list length
def id():
    while True:
        idNum = random.randint(1, 9999)
        idFormated = f"{idNum:04d}"
        if idFormated not in ids_generates:
            ids_generates.add(idFormated)
            return f"C{idFormated}"