# Calcul Moyenne Bac D - Terminale D

Mon premier projet Python pour calculer ma moyenne du Bac D.
Objectif : Avoir 12,50+ pour dossier Campus France Licence Informatique.

## Mon code

```python
# Projet Bac D - par un futur ingénieur
notes = {
  "Maths": 13,
  "Physique-Chimie": 12,
  "SVT": 14,
  "Français": 11,
  "Philo": 10
}

moyenne = sum(notes.values()) / len(notes)
print(f"Moyenne : {moyenne}/20")

if moyenne >= 12.5:
  print("Objectif France validé ! Licence Info")
else:
  print("Encore un peu de travail")
