from tkinter import *
from tkinter.messagebox import *
from math import *
from globale import *
from module2 import *


### Dernière modification : 17/04/2020


############################################################################################################################################################################################################################################

# -------------------------------------------------------------------------------
# Changement de l'inclinaison du canon
# -------------------------------------------------------------------------------

def fctRotationCanon(pCanon, pNouvelAngleInclinaison):
    # pCanon : Dictionnaire du canon
    # pNouvelAngleInclinaison : nouvel angle d'inclinaison du canon

    if pNouvelAngleInclinaison > 0 and pNouvelAngleInclinaison < 90:
        pCanon["angleInclinaison"] = pNouvelAngleInclinaison


# -------------------------------------------------------------------------------
# Affichage du canon
# -------------------------------------------------------------------------------

def fctAfficherCanon(pCanon, pNomCan, pVarGlobales):
    # pCanon : Dictionnaire du canon
    # pNomCan : Canvas dans lequel le canon sera affiché
    # pVarGlobales : Dictionnaire des variables globales

    ### Affichage de la roue du canon ###

    xp, yp = fctConvCoord(pCanon["x"], pCanon["y"], pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    xp1, yp1 = fctConvCoord(pCanon["x"] - pCanon["rayonCanon"], pCanon["y"] - pCanon["rayonCanon"],
                            pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    xp2, yp2 = fctConvCoord(pCanon["x"] + pCanon["rayonCanon"], pCanon["y"] + pCanon["rayonCanon"],
                            pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    pCanon["idRoue"] = pNomCan.create_oval(xp1, yp1, xp2, yp2, fill="black", outline="black")

    ### Affichage du canon ###

    xr4 = pCanon["x"] + pCanon["longueurCanon"] * cos(radians(pCanon["angleInclinaison"]))
    yr4 = pCanon["y"] + pCanon["longueurCanon"] * sin(radians(pCanon["angleInclinaison"]))
    xp3, yp3 = fctConvCoord(pCanon["x"], pCanon["y"], pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    xp4, yp4 = fctConvCoord(xr4, yr4, pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    pCanon["idCanon"] = pNomCan.create_line(xp3, yp3, xp4, yp4, fill="black", width=pCanon["epaisseurCanon"])


# -------------------------------------------------------------------------------
# Effacer le canon
# -------------------------------------------------------------------------------

def fctEffacerCanon(pCanon, pNomCan):
    # pCanon : Dictionnaire du canon
    # pNomCan : Canvas dans lequel le canon sera effacé

    pNomCan.delete(pCanon["idCanon"])
    pNomCan.delete(pCanon["idRoue"])


# -------------------------------------------------------------------------------
# Changer l'orientation du canon
# -------------------------------------------------------------------------------

def fctBougerCanon(pCanon, pNomCan, pVarGlobales):
    # pCanon : Dictionnaire du canon
    # pNomCan : Canvas dans lequel le canon sera affiché
    # pVarGlobales : Dictionnaire des variables globales

    xr4 = pCanon["x"] + pCanon["longueurCanon"] * cos(radians(pCanon["angleInclinaison"]))
    yr4 = pCanon["y"] + pCanon["longueurCanon"] * sin(radians(pCanon["angleInclinaison"]))
    xp3, yp3 = fctConvCoord(pCanon["x"], pCanon["y"], pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    xp4, yp4 = fctConvCoord(xr4, yr4, pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    pNomCan.coords(pCanon["idCanon"], xp3, yp3, xp4, yp4)


# -------------------------------------------------------------------------------
# Changement de la vitesse de sortie du projectile du canon
# -------------------------------------------------------------------------------

def fctVitesseSortieCanon(pCanon, pNouvelleVitesseSortie):
    # pCanon : Dictionnaire du canon
    # pNouvelleVitesseSortie : nouvelle vitesse de sortie du projectile du canon

    if pNouvelleVitesseSortie >= int(dVarGlobales["vMin"]) and pNouvelleVitesseSortie <= int(dVarGlobales["vMax"]):
        pCanon["vitesseSortie"] = pNouvelleVitesseSortie


############################################################################################################################################################################################################################################

### DEFINITION DU PROJECTILE ###


# -------------------------------------------------------------------------------
# Affichage du projectile
# -------------------------------------------------------------------------------

def fctAfficherProjectile(pProjectile, pNomCan, pVarGlobales):
    # pProjectile : Dictionnaire du projectile
    # pNomCan : Canvas dans lequel le canon sera affiché
    # pVarGlobales : Dictionnaire des variables globales

    if dVarGlobales["niveauJeu"] == "F":
        pProjectile["rayonP"] = 6
    else:
        pProjectile["rayonP"] = 4

    xp, yp = fctConvCoord(pProjectile["x"], pProjectile["y"], pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    xp0, yp0 = xp - pProjectile["rayonP"], yp - pProjectile["rayonP"]
    xp1, yp1 = xp + pProjectile["rayonP"], yp + pProjectile["rayonP"]
    pProjectile["idProjectile"] = pNomCan.create_oval(xp0, yp0, xp1, yp1, fill="black", outline="black")


# -------------------------------------------------------------------------------
# Déplacement du projectile
# -------------------------------------------------------------------------------

def fctBougerProjectile(pProjectile, pNomCan, pVarGlobales):
    # pProjectile :     Dictionnaire du projectile
    # pNomCan :         Canvas dans lequel le canon sera affiché
    # pVarGlobales :    Dictionnaire des variables globales

    if dVarGlobales["niveauJeu"] == "F":
        pProjectile["rayonP"] = 6
    else:
        pProjectile["rayonP"] = 4

    xp, yp = fctConvCoord(pProjectile["x"], pProjectile["y"], pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)
    xp0, yp0 = xp - pProjectile["rayonP"], yp - pProjectile["rayonP"]
    xp1, yp1 = xp + pProjectile["rayonP"], yp + pProjectile["rayonP"]
    pNomCan.coords(pProjectile["idProjectile"], xp0, yp0, xp1, yp1)


# -------------------------------------------------------------------------------
# Effacer un projectile
# -------------------------------------------------------------------------------

def fctEffacerProjectile(pProjectile, pNomCan, pVarGlobales):
    # pProjectile :     Dictionnaire du projectile
    # pNomCan :         Canvas dans lequel le canon sera effacé
    # pVarGlobales :    Dictionnaire des variables globales

    pNomCan.delete(pProjectile["idProjectile"])


# -------------------------------------------------------------------------------
# Calcul des coordonnées initiales du projectile (extrémité du canon)
# -------------------------------------------------------------------------------

def fctXyProj(pProjectile, pCanon):
    # pProjectile : Données du projectile
    # pCanon :      Données du canon

    pProjectile["xi"] = pCanon["x"] + pCanon["longueurCanon"] * cos(radians(pCanon["angleInclinaison"]))
    pProjectile["yi"] = pCanon["y"] + pCanon["longueurCanon"] * sin(radians(pCanon["angleInclinaison"]))
    pProjectile["x"] = pCanon["x"] + pCanon["longueurCanon"] * cos(radians(pCanon["angleInclinaison"]))
    pProjectile["y"] = pCanon["y"] + pCanon["longueurCanon"] * sin(radians(pCanon["angleInclinaison"]))


# -------------------------------------------------------------------------------
# Calcul de la vitesse du projectile à une distance donnée
# -------------------------------------------------------------------------------

def fctVitesseProjectile(pDist, pProjectile):
    # pDist : distance parcourue par le projectile
    # pProjectile : données du projectile
    # retourne la vitesse du projectille à la dstance pDist

    vitesse = sqrt(carre(pProjectile["vitesse"]) - 2 * dVarGlobales["G"] * pDist * tan(
        radians(pProjectile["angleDepart"])) + carre(
        dVarGlobales["G"] * pDist / (pProjectile["vitesse"] * cos(radians(pProjectile["angleDepart"])))))
    return vitesse


### Conversion de coordonnées réelles vers des coordonnées en pixels


# -------------------------------------------------------------------------------
# Conversion des coordonnées réelles (métriques) du projectile en pixels
# -------------------------------------------------------------------------------

def fctConvCoord(pXReel, pYReel, pLargeurReelle, pHauteurReelle, pNomCan):
    xp = (float(pNomCan.cget("width")) * float(pXReel)) / float(pLargeurReelle)
    yp = float(pNomCan.cget("height")) - (float(pYReel) * float(pNomCan.cget("height"))) / float(pHauteurReelle)
    return xp, yp


# ---------------------------------------------------------------------------------------
# Calcul du délai de rafraichissement du canevas pour afficher la suite de la trajectoire
# ---------------------------------------------------------------------------------------

def fctCalculDelai(pVitesse, pVarGlobales):
    # pVitesse :        vitesse actuelle du projectile
    # pVarGlobales :    dictionnaire des variables globales

    delai = int((pVitesse - pVarGlobales["vMin"]) / (pVarGlobales["vMax"] - pVarGlobales["vMin"]) * (
                pVarGlobales["delaiMax"] - pVarGlobales["delaiMin"]) + pVarGlobales["delaiMin"])
    return delai


# -----------------------------------------
# Affichage de la trajectoire du projectile
# -----------------------------------------

def fctAfficherTrajectoire(pProjectile, pVarGlobales, pJaugeEp, pJaugeEc, pJaugeEm, pNomCan, pValeurHauteurActuelle,
                           pValeurDistanceParcourue, pValeurVitesseActuelle, \
                           pBoutonModeScientifique, pBoutonModeJeu, pLabelMode):
    # pProjectile :                 données du projectile à déplacer
    # pCanon :                      données du canon
    # pVarGlobales :                varibales globales
    # pJaugeEp :                    Données de la jauge pour Ep
    # pJaugeEc :                    Données de la jauge pour Ec
    # pJaugeEm :                    Données de l a jauge pour Em
    # pNomCan :                     Canevas ou affciher la trajectoire
    # pValeurHauteurActuelle :      label pour afficher la hauteur actuelle du projectile
    # pValeurDistanceParcourue :    label pour afficher la distance parcourue par le projectile
    # pValeurVitesseActuelle :      label pour afficher la vitesse actuelle du projectile
    # pBoutonModeScientifique :     bouton de sélection du mode scientifique
    # pBoutonModeJeu :              bouton de sélection du mode jeu
    # pLabelMode :                  label affichant le mode de jeu sélectionné

    # La fonction affiche la parabole représentant la trajectoire du projectile, en reliant par un segment deux positions successives du projectile.

    #   Le projectile est en cours de déplacement   #
    pProjectile["deplEnCours"] = 1
    departX = pProjectile["x"]
    departY = pProjectile["y"]

    # Conversion des coordonnées réelles du premier point du segment en coordonnées écran.
    departXP, departYP = fctConvCoord(departX, departY, pVarGlobales["LargMax"], pVarGlobales["HautMax"], pNomCan)

    arriveeY = 0

    listeIdLigne = pVarGlobales["listIdLigne"]

    # Calcul de l'abscisse du deuxième point du segment (décalage de 1)
    arriveeX = departX + 1

    # Calcul de l'ordonnée du deuxième point du segment
    temp, arriveeY = fctEquationTrajectoire(pProjectile["vitesse"], pProjectile["angleDepart"], pVarGlobales["G"],
                                            arriveeX - pProjectile["xi"], pProjectile["yi"])

    # Si la partie en cours est terminée (en mode jeu), l'affichage de la trajectoire doit s'arrêter :
    # On force l'abscisse du projectile à 0.

    if not pVarGlobales["partieEnCours"]:
        arriveeY = 0

    # Si le projectile est toujours en l'air :
    if arriveeY > 0:
        #       Conversion des coordonnées réelles du deuxième point du segment en coordonnées écran.
        arriveeXP, arriveeYP = fctConvCoord(arriveeX, arriveeY, pVarGlobales["LargMax"], pVarGlobales["HautMax"],
                                            pNomCan)

        #       Si le projectile est lancé en mode scientifique, on affiche la trajectoire.
        #       Si le projectile est lancé en mode jeu, on n'affiche que le projectile.
        if pProjectile["modeLancement"] == "S":
            idLine = pNomCan.create_line(departXP, departYP, arriveeXP, arriveeYP, width=2, smooth=1, fill="black")
            listeIdLigne.append(idLine)
            pVarGlobales["listIdLigne"] = listeIdLigne

        pProjectile["x"] = arriveeX
        pProjectile["y"] = arriveeY

        #       On affiche le projectile à sa nouvelle position
        fctBougerProjectile(pProjectile, pNomCan, pVarGlobales)

        #       Calcul de la vitesse du projectile à sa nouvelle position
        vitesse = fctVitesseProjectile(pProjectile["x"] - pProjectile["xi"], pProjectile)
        pProjectile["vitesseX"] = vitesse

        #       En mode scientifique, calcul des énergies potentielle, cinétique et mécanique
        #       Affichage des trois jauges correspondantes
        if pProjectile["modeLancement"] == "S":
            lEnergie = []
            lEnergie = fctEnergies(vitesse, pProjectile["masse"], pVarGlobales["G"], pProjectile["y"])
            pJaugeEp["valeur"] = lEnergie[1]
            pJaugeEp["idJauge"] = fctAfficherJauge(pJaugeEp, pJaugeEp["canvas"])
            pJaugeEc["valeur"] = lEnergie[0]
            pJaugeEc["idJauge"] = fctAfficherJauge(pJaugeEc, pJaugeEc["canvas"])
            pJaugeEm["valeur"] = lEnergie[2]
            pJaugeEm["idJauge"] = fctAfficherJauge(pJaugeEm, pJaugeEm["canvas"])
            fctAfficherValeur(arriveeY, pValeurHauteurActuelle)
            fctAfficherValeur(vitesse, pValeurVitesseActuelle)
            fctAfficherValeur(arriveeX - pProjectile["xi"], pValeurDistanceParcourue)

        #       Le point d'arrivée du segment affiché devient le point de départ du prochain segment.
        departX = arriveeX
        departY = arriveeY
        departXP = arriveeXP
        departYP = arriveeYP

        #       Vérifier s'il y a une collision entre le projectile actuellement affiché et les ballons.
        collision = fctDetectionCollision(arriveeXP, arriveeYP, lListBallon, pNomCan)
        #       Calcul du délai d'attente pour afficher le segment en fonction de la vitesse actuelle du projectile
        delai = fctCalculDelai(pProjectile["vitesseX"], pVarGlobales)

        #       Rappel de la fonction fctAfficherTrajectoire pour afficher le segment suivant de la parabole.
        pNomCan.after(delai, fctAfficherTrajectoire, pProjectile, pVarGlobales, pJaugeEp, pJaugeEc, pJaugeEm, pNomCan,
                      pValeurHauteurActuelle, pValeurDistanceParcourue, \
                      pValeurVitesseActuelle, pBoutonModeScientifique, pBoutonModeJeu, pLabelMode)
    else:
        #       Le projectile a atteint le sol.
        #       Le projectile ne se déplace plus
        pProjectile["deplEnCours"] = 0
        if dVarGlobales["mode"] == "S":
            #           En mode scientifique, la partie est considérée comme terminée.
            dVarGlobales["partieEnCours"] = False

        #       Calcul de la distance parcourue par le projectile au moment où il touche le sol
        #       afin d'afficher le boulet au sol à son abscisse exacte
        dist = fctDistanceParcourue(pProjectile["vitesse"], pProjectile["angleDepart"], pVarGlobales["G"],
                                    pProjectile["yi"])
        temp, arriveeY = fctEquationTrajectoire(pProjectile["vitesse"], pProjectile["angleDepart"], pVarGlobales["G"],
                                                dist, pProjectile["yi"])
        pProjectile["x"] = dist + pProjectile["xi"]
        pProjectile["y"] = abs(arriveeY) * 0
        arriveeXP, arriveeYP = fctConvCoord(pProjectile["x"], pProjectile["y"], pVarGlobales["LargMax"],
                                            pVarGlobales["HautMax"], pNomCan)

        #       Si le projectile est lancé en mode scientifique, on affiche la trajectoire.
        #       Si le projectile est lancé en mode jeu, on n'affiche que le projectile.
        if pProjectile["modeLancement"] == "S":
            idLine = pNomCan.create_line(departXP, departYP, arriveeXP, arriveeYP, width=2, smooth=1, fill="black")
            listeIdLigne.append(idLine)
            pVarGlobales["listIdLigne"] = listeIdLigne

        #       On affiche le projectile à sa nouvelle position
        fctBougerProjectile(pProjectile, pNomCan, pVarGlobales)

        #       En mode scientifique, calcul des énergies potentielle, cinétique et mécanique
        #       Affichage des trois jauges correspondantes
        if pProjectile["modeLancement"] == "S":
            vitesse = fctVitesseProjectile(pProjectile["x"] - pProjectile["xi"], pProjectile)
            lEnergie = []
            lEnergie = fctEnergies(vitesse, pProjectile["masse"], pVarGlobales["G"], pProjectile["y"])
            pJaugeEp["valeur"] = lEnergie[1]
            pJaugeEp["idJauge"] = fctAfficherJauge(pJaugeEp, pJaugeEp["canvas"])
            pJaugeEc["valeur"] = lEnergie[0]
            pJaugeEc["idJauge"] = fctAfficherJauge(pJaugeEc, pJaugeEc["canvas"])
            pJaugeEm["valeur"] = lEnergie[2]
            pJaugeEm["idJauge"] = fctAfficherJauge(pJaugeEm, pJaugeEm["canvas"])
            fctAfficherValeur(abs(arriveeY), pValeurHauteurActuelle)
            fctAfficherValeur(vitesse, pValeurVitesseActuelle)
            fctAfficherValeur(arriveeX - pProjectile["xi"], pValeurDistanceParcourue)
            fctReinitialisationJeuModeS(pVarGlobales, pProjectile, pBoutonModeScientifique, pBoutonModeJeu, pLabelMode)


# -----------------------------------------
# Affichage du fond de la jauge
# -----------------------------------------

def fctAfficherJaugeFond(pJauge, pNomCan):
    # pJauge :  jauge dont le fond est à afficher
    # pNomCan : canevas ou la jauge sera afichée

    haut = max(pJauge["posy"] - pJauge["hauteur"], 0)
    idFond = pNomCan.create_line(pJauge["posx"], pJauge["posy"], pJauge["posx"], pJauge["posy"] - pJauge["hauteur"],
                                 fill="white", width=pJauge["largeur"])

    return idFond


# -----------------------------------------
# Affichage du niveau actuel de la jauge
# -----------------------------------------

def fctAfficherJauge(pJauge, pNomCan):
    # pJauge :  jauge dont le niveau est à afficher
    # pNomCan : canevas ou la jauge sera afichée

    hauteur = (pJauge["hauteur"] * pJauge["valeur"]) / pJauge["vmax"]
    if pJauge["idJauge"] != 0:
        pNomCan.coords(pJauge["idJauge"], pJauge["posx"], pJauge["posy"], pJauge["posx"], pJauge["posy"] - hauteur)
    else:
        pJauge["idJauge"] = pNomCan.create_line(pJauge["posx"], pJauge["posy"], pJauge["posx"],
                                                pJauge["posy"] - hauteur, fill=pJauge["couleur"],
                                                width=pJauge["largeur"])

    fctAfficherValeur(pJauge["valeur"], pJauge["label"])
    return pJauge["idJauge"]


# -----------------------------------------
# Effacer la trajectoire du projectile
# -----------------------------------------

def fctEffacerTrajectoire(pIdLine, pNomCan):
    # pIdLine : liste des segments à effacer
    # pNoCan :  canevas contenant la trajectoire à effacer

    for i in range(0, len(dVarGlobales["listIdLigne"])):
        pNomCan.delete(dVarGlobales["listIdLigne"][i])

    pNomCan.delete(dProjectile["idProjectile"])
    dVarGlobales["listIdLigne"] = []


# -----------------------------------------
# Fonction carré
# -----------------------------------------
def carre(x):
    return x * x


# ---------------------------------------------------------------------------
# Calcul de la distance parcoure par le projectile lorsqu'il est tombé au sol
# ---------------------------------------------------------------------------

def fctDistanceParcourue(pVitesse, pAngle, pG, pHauteur):
    # pVitesse :    vitesse initiale du projectile
    # pAngle :      angle de tir
    # pG :          constante g
    # pHauteur :    hauteur initiale du projectile

    dist = pVitesse * cos(radians(pAngle)) / pG * (
                pVitesse * sin(radians(pAngle)) + sqrt(carre(pVitesse * sin(radians(pAngle))) + 2 * pG * pHauteur))
    return dist


# -------------------------------------------------------------------------------
# Calcul de la hauteur maximale atteinte par le projectile pdurant sa trajectoire
# -------------------------------------------------------------------------------

def fctHauteurMaximale(pVI, pAngle, pG, pHautInit):
    # pVI :         vitesse initiale du projectile
    # pAngle :      angle de tir
    # pG :          constante g
    # pHautInit :   hauteur initiale du projectile

    hauteurMax = (carre(float(pVI) * sin(radians(pAngle)))) / (2 * pG) + pHautInit
    return hauteurMax


# -------------------------------------------------------------------------------
# Affichage de la valeur d'un label
# -------------------------------------------------------------------------------

def fctAfficherValeur(pValeur, pNomLabel):
    # pValeur :     valeur à afficher
    # pNomLabel :   label dont la valeur est à afficher

    if pValeur == "":
        pNomLabel.config(text=pValeur)
    else:
        pValeur = round(pValeur, 2)
        pNomLabel.config(text=pValeur)


############################################################################################################################################################################################################################################

# -----------------------------------------------------------------------------------
# Détection de collisions entre le projectille et les ballons de la valeur d'un label
# -----------------------------------------------------------------------------------

def fctDetectionCollision(pXp, pYp, pListBallon, pNomCan):
    # pXp, pYp :    abscisse et ordonnée du projectile
    # pListBallon : liste des numéros de ballons
    # pNomCan :     canevas contenant le projectile et les ballons

    # Détection d'une intersection entre le rectangle contenant le projectile
    # et le rectangle contenant le ballon
    collision = False
    for i in range(0, len(pListBallon)):
        x1, y1, x2, y2 = pNomCan.coords(pListBallon[i])
        if pXp > x1 and pXp < x2:
            if pYp > y1 and pYp < y2:
                collision = True
                fctCollisionBallon(pNomCan, pListBallon[i], dBallon, dVarGlobales)
    return collision


#############################################################################################################################################################################################################################################
# -------------------------------------------------------------------------------
# Gestion du chronomètre
# -------------------------------------------------------------------------------

def fctHorloge(pCan, pVarGlobales, pProjectile, plabelValeurScore, plabelValeurTirs, plabelValeurTemps, pFen, \
               pBoutonModeJeu, pBoutonModeScientifique, pLabelMode, pBoutonNiveauFacile, pBoutonNiveauDifficile,
               pLabelNiveau):
    # pCan :                        canevas
    # pVarGlobales :                dictionnaire contenant les variables globales
    # pProjectile :                 dictionnaire du projectile
    # plabelValeurScore :           label affichant la valeur du score
    # pLabelValeursTirs :           label affichant le nombre de tirs
    # pLabelValeurTemps :           label affichant le temps restant
    # pFen :                        paramètre pour désigner la fenêtre
    # pBoutonModeJeu :              bouton pour sélectionner le mode Jeu
    # pBoutonModeScientifique :     bouton pour sélectionner le mode Scientifique
    # pLabelMode :                  label affichant le mode de jeu sélectionné (mode Jeu ou mode scientifique)
    # pBoutonNiveauFacile :         bouton pour sélectionner le niveau facile
    # pBoutonNiveauDifficile :      bouton pour sélectionner le niveau difficile
    # pLabelMode :                  label affichant le niveau de jeu sélectionné (mode facile ou difficile)

    # Exécution du compte à rebours.
    # Lors des dix dernières secondes, le compte à rebours clignote en rouge et en noir.
    pVarGlobales["temps"] -= 1
    plabelValeurTemps.configure(text=pVarGlobales["temps"])
    if pVarGlobales["temps"] <= 10:
        fctChangerCouleurTemps(plabelValeurTemps, "red")
        pFen.after(500, fctChangerCouleurTemps, plabelValeurTemps, "black")

    else:
        plabelValeurTemps.configure(font=("", 36, "bold"))
        fctChangerCouleurTemps(plabelValeurTemps, "black")

    # On relance dans 1 seconde
    if pVarGlobales["temps"] <= 0:
        fctReinitialisationJeuModeJ(pCan, pVarGlobales, pProjectile, plabelValeurScore, plabelValeurTirs,
                                    plabelValeurTemps, pBoutonModeJeu, pBoutonModeScientifique, pLabelMode,
                                    pBoutonNiveauFacile, pBoutonNiveauDifficile, pLabelNiveau)
    else:
        pFen.after(1000, fctHorloge, pCan, pVarGlobales, pProjectile, plabelValeurScore, plabelValeurTirs,
                   plabelValeurTemps, pFen, pBoutonModeJeu, pBoutonModeScientifique, pLabelMode, pBoutonNiveauFacile,
                   pBoutonNiveauDifficile, pLabelNiveau)


# -------------------------------------------------------------------------------
# Rénitialisation du jeu en mode Jeu
# -------------------------------------------------------------------------------

def fctReinitialisationJeuModeJ(pCan, pVarGlobales, pProjectile, plabelValeurScore, plabelValeurTirs, plabelValeurTemps,
                                pBoutonModeJeu, pBoutonModeScientifique, pLabelMode, pBoutonNiveauFacile,
                                pBoutonNiveauDifficile, pLabelNiveau):
    # pVarGlobales :                dictionnaire contenant les variables globales
    # pProjectile :                 dictionnaire du projectile
    # plabelValeurScore :           label affichant la valeur du score
    # pLabelValeursTirs :           label affichant le nombre de tirs
    # pLabelValeurTemps :           label affichant le temps restant
    # pBoutonModeJeu :              bouton pour sélectionner le mode Jeu
    # pBoutonModeScientifique :     bouton pour sélectionner le mode Scientifique
    # pLabelMode :                  label affichant le mode de jeu sélectionné (mode Jeu ou mode scientifique)

    pVarGlobales["temps"] = 45
    pVarGlobales["nombreTirs"] = 0
    pVarGlobales["partieEnCours"] = False
    plabelValeurTemps.configure(font=("", 36, "bold"), fg="black")

    score = str(plabelValeurScore.cget("text"))
    nbTirs = str(plabelValeurTirs.cget("text"))

    plabelValeurTemps.configure(text=pVarGlobales["temps"])
    plabelValeurScore.configure(text="0")
    plabelValeurTirs.configure(text="0")

    showinfo("Fin de jeu", "Le temps est écoulé\n Score: " + score + "\n Tirs: " + nbTirs)

    pBoutonModeScientifique.grid()
    pBoutonModeJeu.grid()
    pLabelMode.configure(text="Mode")

    pBoutonNiveauFacile.grid()
    pBoutonNiveauDifficile.grid()
    pLabelNiveau.configure(text="Niveau")


# -------------------------------------------------------------------------------
# Rénitialisation du jeu en mode scientifique
# -------------------------------------------------------------------------------

def fctReinitialisationJeuModeS(pVarGlobales, pProjectile, pBoutonModeScientifique, pBoutonModeJeu, pLabelMode):
    # pVarGlobales :                dictionnaire contenant les variables globales
    # pProjectile :                 dictionnaire du projectile
    # pBoutonModeJeu :              bouton pour sélectionner le mode Jeu
    # pBoutonModeScientifique :     bouton pour sélectionner le mode Scientifique
    # pLabelMode :                  label affichant le mode de jeu sélectionné (mode Jeu ou mode scientifique)

    pVarGlobales["partieEnCours"] = False
    pBoutonModeScientifique.grid()
    pBoutonModeJeu.grid()
    pLabelMode.configure(text="Mode")


# -------------------------------------------------------------------------------
# Changement de la couleur du temps
# -------------------------------------------------------------------------------
def fctChangerCouleurTemps(plabelValeurTemps, pCouleur):
    # pLabelValeurTemps :   label affichant le temps restant
    # pCouleur :            couleur de la valeur du temps

    plabelValeurTemps.configure(fg=pCouleur)
