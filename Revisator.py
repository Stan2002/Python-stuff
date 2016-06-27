import random

dico = {

    "arbre" : "tree"

           }

print("=========")
print("REVISATOR")
print("=========")
print()

playing = True

while playing == True:

        score = 0

        num = int(input("\nNombre de questions : "))

        for i in range(num):

            question = (random.choice(list(dico.keys())))

            reponse = dico[question]

            print("\nQUESTION " + str(i + 1) + " :")
            print(question + " ?")

            guess = input("> ")

            if guess.lower() == reponse.lower():

                print("OUI !!!")
                score += 1
            else:
                print("NON")
                print(">>> " + reponse)
                print()
                print(question + str())
                guess = input("> ")

                if guess.lower() == reponse.lower():

                    print("OUI")

                else:
                    print("NON")
                    print(">>> " + reponse)
                    print()

        print("\nVotre score est de " + str(score) + " sur " + str(num))
        print("Votre pourcentage de bonnes réponses est de ", round(score / num * 100, 2), "%")
        print()


        again = input("Tapez une touche pour continuer, ou 'Q' pour quitter.")
        if again.lower() == 'q':
            playing = False


