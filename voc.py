# coding: utf-8

continuer = True
while continuer :

    en = input("MOT EN ANGLAIS : ")
    fr = input("MOT EN FRANÇAIS : ")
    print("\n")

    with open("def.txt", "a") as fich :
        fich.write('"')
        fich.write(en)
        fich.write("          =          ")
        fich.write(fr)
        fich.write('"')
        fich.write(',')
        fich.write("\n")



