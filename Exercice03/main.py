words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

voyelles = "aeiouy"

resultat = [(word, sum(1 for char in word if char in voyelles)) for word in words]

print(resultat)
