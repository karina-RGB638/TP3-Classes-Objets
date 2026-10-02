from noeud import Noeud


# Création des nœuds
n_exp = Noeud("exp")
n_plus = Noeud("+")
n_2 = Noeud(2)
n_y = Noeud("y")


# Construction de l'arbre
n_plus.ajouter_enfant(n_2)
n_plus.ajouter_enfant(n_y)

n_exp.ajouter_enfant(n_plus)


# Affichage de l'expression
print("Expression en notation polonaise :")
print(n_exp.afficher())


# Évaluation avec y = 3
resultat = n_exp.evaluer({"y": 3})

print("Résultat avec y = 3 :")
print(resultat)


# Tracé de l'expression
valeurs = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

n_exp.tracer("y", valeurs)