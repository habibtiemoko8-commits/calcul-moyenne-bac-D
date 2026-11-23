# Projet Bac D - Calcul moyenne
# Par Habib Tiemoko - Terminale D

print("=== CALCUL MOYENNE BAC D ===")

# Tes notes - change avec tes vraies notes
maths = 13
physique = 12
svt = 14
francais = 11
philo = 10
anglais = 12
hist_geo = 11

# Calcul
matieres = [maths, physique, svt, francais, philo, anglais, hist_geo]
moyenne = sum(matieres) / len(matieres)

print(f"Ta moyenne est : {moyenne:.2f}/20")

if moyenne >= 14:
    print("Mention BIEN ! Objectif France validé")
elif moyenne >= 12:
    print("Mention Assez Bien ! Bon pour Campus France")
elif moyenne >= 10:
    print("Bac obtenu !")
else:
    print("Encore du travail, tu peux le faire")
