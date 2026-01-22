"""Module providing the logic of the 2048 game"""

import random
from typing import List, Tuple

TAILLE:int = 4


# ==========================================================
# 🎯 FONCTION PUBLIQUE (API POUR L’INTERFACE)
# ==========================================================

def nouvelle_partie() -> Tuple[List[List[int]], int]:
    """
    Crée une nouvelle partie du jeu 2048.

    :return: Une grille TAILLExTAILLE initialisée avec deux tuiles, ainsi que le score à 0.
    :rtype: Tuple[List[List[int]], int]
    """
    raise NotImplementedError("Fonction nouvelle_partie non implémentée.")

def jouer_coup(plateau: List[List[int]], direction: str) -> tuple[List[List[int]], int, bool]:
    """
    Effectuer un mouvement sur le plateau.

    :param plateau: Une grille TAILLExTAILLE du jeu.
    :type plateau: List[List[int]]
    :param direction: La direction du déplacement : 'g' (gauche), 'd' (droite), 'h' (haut), 'b' (bas).
    :type direction: str
    :return: Retourne un tuple (nouveau_plateau, points, est_fini).
    :rtype: tuple[List[List[int]], int, bool]
    """

    raise NotImplementedError("Fonction jouer_coup non implémentée.")

# ==========================================================
# 🔒 FONCTIONS PRIVÉES (LOGIQUE INTERNE)
# ==========================================================

def _creer_plateau_vide() -> List[List[int]]:
    """
    Crée une grille TAILLExTAILLE remplie de zéros.
    :return: Une grille vide.
    :rtype: List[List[int]]
    """
    grille = []
    for _ in range (TAILLE):
        ligne = []
        for _ in range(TAILLE) :
            ligne.append(0)
        grille.append(ligne)
    return grille

    raise NotImplementedError("Fonction _creer_plateau_vide non implémentée.")

def _get_cases_vides(plateau: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Retourne les coordonnées des cases vides sous forme d'une liste de coordonnées

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une liste de coordonnées
    :rtype: List[Tuple[int, int]]
    """
    raise NotImplementedError("Fonction _get_cases_vides non implémentée.")

def _ajouter_tuile(plateau: List[List[int]]) -> List[List[int]]:
    """
    Ajoute une tuile de valeur 2 sur une case vide.

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une nouvelle grille avec une tuile ajoutée.
    :rtype: List[List[int]]
    """
    raise NotImplementedError("Fonction _ajouter_tuile non implémentée.")

def _supprimer_zeros(ligne: List[int]) -> List[int]:
    """
    Supprime les zéros d'une ligne.

    :param ligne: Une ligne de la grille.
    :type ligne: List[int]
    :return: La ligne sans zéros.
    :rtype: List[int]
    """
    raise NotImplementedError("Fonction _supprimer_zeros non implémentée.")

def _fusionner(ligne: List[int]) -> Tuple[List[int], int]:
    """
    Fusionne les valeurs identiques consécutives d'une ligne.

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: La ligne après fusion, les points gagnés
    :rtype: Tuple[List[int], int]
    """
    raise NotImplementedError("Fonction _fusionner non implémentée.")

def _completer_zeros(ligne): # ajouter les annotations de type
    """
    DOCSTRING À ECIRE
    """
    raise NotImplementedError("Fonction _completer_zeros non implémentée.")

def _deplacer_gauche(plateau) : # ajouter les annotations de type
    """
    DOCSTRING À ÉCRIRE
    """
    raise NotImplementedError("Fonction _deplacer_gauche non implémentée.")

def _inverser_lignes(plateau): # ajouter les annotations de type
    """
    DOCSTRING À ÉCRIRE
    """
    raise NotImplementedError("Fonction _inverser_lignes non implémentée.")

def _deplacer_droite(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers la droite en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    :rtype: Tuple[List[List[int]], int]
    """
    raise NotImplementedError("Fonction _deplacer_droite non implémentée.")

def _transposer(plateau): # ajouter les annotations de type
    """
    DOCSTRING À ÉCRIRE
    """
    raise NotImplementedError("Fonction _transposer non implémentée.")

def _deplacer_haut(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le haut en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    raise NotImplementedError("Fonction _deplacer_haut non implémentée.")


def _deplacer_bas(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le bas en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    raise NotImplementedError("Fonction _deplacer_bas non implémentée.")

def _partie_terminee(plateau: List[List[int]]) -> bool:
    """
    DOCSTRING À ÉCRIRE
    """
    # Partie non terminee si il y a des cases vides
    # Partie non terminee si il y a des fusions possibles (horizontale ou verticale)
    # Sinon c'est vrai

    raise NotImplementedError("Fonction _partie_terminee non implémentée.")