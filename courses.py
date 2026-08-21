"""
affichage à l'écran
print("hello, world")
print("j'apprends python")
print(17+35*2)
"""

"""
declaration de variables
cours="mathématiques"
print(cours)
cours="anglais"
print(cours)

cours="hist-géo"
print(cours)
cours="philo"
print(f"Je suis plutot au cours de {cours}")

nourriture_preferee="igname pilée"
nouvelle_nourriture_preferee="amiwo"
nourriture_preferee="telibo"
print(f"Ma nourriture preferee est {nourriture_preferee}")


nom="Feliciano M."
age="20 ans"
print(f"Je m'appelle {nom} et j'ai {age} ")
age="30 ans"
print(f"Je m'appelle {nom} et j'ai {age} ")
"""

"""
nom= "Feliciano M."
age= "20 ans"
taille= "1.75m"
est_etudiant= "True"
print(f"Je m'appelle {nom} et j'ai {age}. Je mesure {taille}. Je suis un {est_etudiant}")
type_nom= type(nom)
type_age= type(age)
type_taille= type(taille)
type_est_etudiant= type(est_etudiant)

nom= 2
var_typed=type(nom)
print(f"Le type de la variable nom est {var_typed}")
"""

"""
Enregistrez des groupes de données avec les listes


#création d'une liste
mes_fruits= ["orange", "raisin", "banane", "pomme", "pasteque", "papaye"]
print(f"Les fruits sont {mes_fruits}")

#ajout d'un fruit avec append()
mes_fruits.append("mangue")
print(f"Votre nouvelle liste est {mes_fruits}")

#suppression d'un fruit avec remove()
mes_fruits.remove("pomme")
print(f"Les fruits restants sont {mes_fruits}")

#modification d'un fruit a une position donnée 
mes_fruits[2]= "ananas"
print(f"Votre nouvelle liste est {mes_fruits}")
len(mes_fruits)
print(f'Le nombre de fruits est {len(mes_fruits)}')

#Trie alphabetiquedes fruits avec sort()
mes_fruits.sort()
print(f"Les fruits triés sont {mes_fruits}")
"""

"""
Enregistrez des données complexes avec des dictionnaires

#creer un dictionnaire
fruits= {"pomme":"rouge", "banane":"jaune", "orange":"orange"}
print(f"Les fruits sont {fruits}")
#ajouter un element 
fruits["kiwi"]= "vert"
print(f"Les nouveaux fruits sont {fruits}")
#accédez à la valeur correspondant à la clé et la stockez dans une variable
couleur_banane = fruits["banane"]
print("La couleur de la banane est {}".format(couleur_banane))
#modifier la valeur associee a une cle
fruits["pomme"]= "vert"
print(f"Les fruits sont {fruits}")
#supprimer un element du dictionnaire avec del
del fruits["banane"]
#afficher le dictionnaire mis a jour
print(f"Les fruits sont {fruits}")
"""


"""
Contrôle du  déroulement d'un programme avec des conditions


les_nouveaux_stagiaires_sont_presents= True
if les_nouveaux_stagiaires_sont_presents:
    print("Appellez les moi")
else: 
    print("Appellez moi la secretaire")


les_nouveaux_stagiaires_sont_presents= False
il_pleut= True
if les_nouveaux_stagiaires_sont_presents:
    print("Appellez les moi")
elif il_pleut: 
    print("Dites leur de venir apres la pluie")
else: 
    print("Appellez moi la secretaire")


nombres_employées= 10
nombres_places= 15
if nombres_employées<nombres_places:
    print("Il y a assez de places pour tous les employés.")
else:
    print("Il n'y a pas assez de places pour tous les employés.")


forme= "cercle"
match forme: 
    case "cercle":
        print("La forme est un cercle")
    case "carre": 
        print("La forme n'est pas un carré")
    case "triangle":
        print("La forme n'est pas un triangle")
    case _:
        print("La forme n'est ni un carre ni un triangle")



#fournir deux nombres avec la fonction input. Stockez ces valeurs dans  nombre1 et  nombre2.
nombre1 = input("Saisissez le premier nombre: ")
nombre2 = input("Saisissez le deuxième nombre: ")

print(f"Le premier nombre est {nombre1.isnumeric()}")
print(f"Le deuxieme nombre est {nombre2.isnumeric()}")

if not nombre1.isnumeric() or not nombre2.isnumeric():
    raise SystemExit("Fin du programme")

nombre1 = int(input("Saisissez le premier nombre: "))
nombre2 = int(input("Saisissez le deuxième nombre: "))

operation= input("Saisissez l'opération à effectuer (+, -, *, /): ")

#methode1

match operation:
    case "+":
        resultat= nombre1 + nombre2
        print(f"Le resultat est {resultat}")

    case "-": 
        resultat= nombre1 - nombre2
        print(f"Le resultat est {resultat}")

    case "*": 
        resultat= nombre1 * nombre2 
        print(f"Le resultat est {resultat}")

    case "/": 
        resultat= nombre1 / nombre2 
        print(f"Le resultat est {resultat}")

    case _:
        print("L'operation que vous voulez n'est pas valide. Réessayez avec +, -, *, /")

#methode2
if operation == "+":
    resultat= nombre1 + nombre2
    print(f"Le resultat est {resultat}")

elif operation == "-":
    resultat= nombre1 - nombre2 
    print(f"Le resultat est {resultat}")

elif operation == "*": 
    resultat= nombre1 * nombre2 
    print(f"Le resultat est {resultat}")

elif operation == "/":
    resultat= nombre1 / nombre2 
    print(f"Le resultat est {resultat}")

else: 
    print("L'operation que vous voulez n'est pas valide. Réessayez avec +, -, *, /")

if operation == "/" and nombre2 == 0:
    print("Erreur: Division par zéro n'est pas autorisée. Re-saisissez le deuxieme nombre")
    print("Saisissez le deuxième nombre: ")
    nombre2 = int(input())

rounded_result = round(resultat, 2)
print(f"Le résultat est: {rounded_result}")
"""

"""
#Répétez des tâches facilement à l'aide de boucles


nombres= str(input("Saisissez une liste de nombres de votre choix séparés par des virgules : "))
print(f"Les nombres saisies sont:{nombres} {type(nombres)}")
liste = nombres.split(",")
print(f" liste de chaîne de caractères: {liste}")


liste_entiers = []

#methode1

for i in liste: 
    i = int(i)
    liste_entiers.append(i)
print(f"une liste d'entiers: {liste_entiers}")


#methode2

liste_entiers = [int(i) for i in liste]
print(f"une liste d'entiers: {liste_entiers}")

#somme= sum (liste_entiers) 
#print(f"La somme des nombres entrez est: {somme} ")

moyenne = sum(liste_entiers) / len(liste_entiers)
print(f"La moyenne des nombres saisies est: {moyenne}")

compteur= 0

for nombres in liste_entiers: 
    if nombres > moyenne: 

        compteur += 1
print(f"Le nombre de nombres dans la liste qui sont superieur a la moyenne est: {compteur}")
"""



"""
Regroupez des tâches en utilisant des fonctions

def afficher(nom, prenom, age=25): 
    print(f"Voici ton {nom} et ton {prenom} {age}")

prenom= input("saisissez votre prenom : ")
nom= input("saisissez votre nom : ")   

afficher(nom, prenom)



# Definitions des fonctions
# 1
def salaire_mensuel(salaire_annuel):
    sal_mensuel= (salaire_annuel/12)
    return sal_mensuel

# 2
def salaire_hebdomadaire(salaire_mensuel):
    sal_hebdomadaire= (salaire_mensuel/4)
    return sal_hebdomadaire

# 3
def salaire_horaire(salaire_hebdomadaire, heure_travaillee):
    sal_horaire= (salaire_hebdomadaire/heure_travaillee)
    return sal_horaire

# Demandes
salaire_annuel= float(input("Saisissez votre salaire annuel: "))
heure_travailee= int(input("Saisissez le nombre d'heure que vous travailler par semaine: "))

# sal_mensuel=salaire_mensuel(salaire_annuel)
# sal_hebdomadaire=salaire_hebdomadaire(salaire_mensuel(salaire_annuel))
sal_horaire=salaire_horaire(salaire_hebdomadaire(salaire_mensuel(salaire_annuel)), heure_travailee)


print(f"Votre salaire horaire est: {sal_horaire}")

"""



"""
Écrivez du code en évitant les erreurs courantes
"""


"""
Importez des packages Python


from operations import * 
a= float(int(input("Saisissez le premier nombre: ")))
b = float(int(input("Saisissez le deuxième nombre: ")))
resultat_addition = addition(a, b)
print(f"Le résultat est: {resultat_addition}")


from operations import * 
a= float(int(input("Saisissez le premier nombre: ")))
b = float(int(input("Saisissez le deuxième nombre: ")))
resultat_multiplication = multiplication(a, b)
print(f"Le résultat est: {resultat_multiplication}")

"""