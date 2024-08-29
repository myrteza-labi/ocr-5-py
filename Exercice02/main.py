students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

nom_etudiant = input("Entrez le nom de l’étudiant : ")

if nom_etudiant in students:
    notes = students[nom_etudiant]
    total = 0
    for matiere, note in notes.items():
        total += note
    
    moyenne = total / len(notes)
    print(f"Moyenne de {nom_etudiant} : {moyenne:.2f}")
else:
    print(f"L'étudiant {nom_etudiant} n'existe pas dans la liste.")
