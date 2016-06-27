liste = list()
somme = 0

print()
print("1 - Calculer une moyenne")
print("2 - Convertir une note sur 20")
print()
choix = (input("Que voulez-vous faire ? "))
print()

if choix == "2":
    note = float(input("Note : "))
    surkoi = float(input("Sur combien ? : "))
    print(round(note / surkoi * 20, 2), "sur 20")

if choix == "1":
    nb_note = int(input("Nombre de notes : "))

    print()

    for i in range(0, nb_note):
        liste.append([float(input("Note : "))])

    for n in liste:
        somme += n[0]

    print()

    res = round(somme / nb_note, 2)
    print(res)

    print()

    mat = input("Matière de la moyenne : ")

    with open("notes.txt", "a") as fichier:
        fichier.write("\n" + mat + " : " + str(res) + " " + str(liste))
        fichier.close()
