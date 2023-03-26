import random



lista_miast = ["Warszawa","Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
plan_wycieczki=[]
index = 0

print("plan wycieczki: ")
for index in range(0, len(lista_miast)):
    losIndex = random.randint(0, len(lista_miast)-1)

    print(lista_miast[losIndex])
    del lista_miast[losIndex]
    len(lista_miast)-1



