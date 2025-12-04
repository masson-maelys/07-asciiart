#### Imports et définition des variables globales
""" Module qui permet de retourner la liste de tuple d'une chaîne de caractères"""
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en 
    argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    liste = []
    caractere = s[0]
    compteur = 1
    chaine = s[1:]
    for i in chaine:
        if i==caractere:
            compteur += 1
        else :
            liste.append((caractere,compteur))
            caractere = i
            compteur = 1

    liste.append((caractere,compteur))
    return liste


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne
     de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    caractere = s[0]
    compteur = 0
    for i in s:
        if i == caractere:
            compteur += 1
        else:
            break
    reste = artcode_r(s[compteur:])
    return [(caractere, compteur)]+reste

#### Fonction principale


def main():
    """
    Docstring pour main
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
