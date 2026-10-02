import math
import matplotlib.pyplot as plt


class Noeud:
    """
    Représente un nœud d'un arbre d'expression.
    """

    def __init__(self, valeur, enfants=None):
        self.valeur = valeur

        if enfants is None:
            self.enfants = []
        else:
            self.enfants = enfants

    def ajouter_enfant(self, enfant):
        """
        Ajoute un nœud à la liste des enfants.
        """
        self.enfants.append(enfant)

    def afficher(self):
        """
        Affiche l'expression en notation polonaise.
        """

        resultat = str(self.valeur)

        for enfant in self.enfants:
            resultat += " " + enfant.afficher()

        return resultat

    def evaluer(self, variables):
        """
        Évalue l'expression avec les valeurs des variables.
        """

        # Si le nœud est un nombre
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur)

        # Si le nœud est une variable
        if self.valeur not in ["+", "-", "*", "/", "exp", "log", "sin", "cos"]:

            if self.valeur not in variables:
                raise ValueError(
                    "La variable " + self.valeur + " n'a pas de valeur."
                )

            return float(variables[self.valeur])

        # Addition
        if self.valeur == "+":
            return (
                self.enfants[0].evaluer(variables)
                + self.enfants[1].evaluer(variables)
            )

        # Soustraction
        if self.valeur == "-":
            return (
                self.enfants[0].evaluer(variables)
                - self.enfants[1].evaluer(variables)
            )

        # Multiplication
        if self.valeur == "*":
            return (
                self.enfants[0].evaluer(variables)
                * self.enfants[1].evaluer(variables)
            )

        # Division
        if self.valeur == "/":
            return (
                self.enfants[0].evaluer(variables)
                / self.enfants[1].evaluer(variables)
            )

        # Fonction exp
        if self.valeur == "exp":
            return math.exp(self.enfants[0].evaluer(variables))

        # Fonction log
        if self.valeur == "log":
            return math.log(self.enfants[0].evaluer(variables))

        # Fonction sin
        if self.valeur == "sin":
            return math.sin(self.enfants[0].evaluer(variables))

        # Fonction cos
        if self.valeur == "cos":
            return math.cos(self.enfants[0].evaluer(variables))

        raise ValueError("Opérateur inconnu : " + str(self.valeur))

    def tracer(self, variable, valeurs):
        """
        Trace la fonction correspondant à l'expression.
        """

        resultats = []

        for valeur in valeurs:
            resultats.append(
                self.evaluer({variable: valeur})
            )

        plt.plot(valeurs, resultats)
        plt.xlabel(variable)
        plt.ylabel("f(" + variable + ")")
        plt.grid()
        plt.show()