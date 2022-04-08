from math import *
from tkinter import *
from globale import *
from random import *
from time import *


############################
# V 4.0 : 15/04/2020 : p prefix devant variables parametres fonction
# V 5.0 : 18/04/2020 : Creation d'un ballon
# V 6.0 : 19/04/2020 : fait bouger les ballons
# V 7.0 : 26/04/2020 : Ajout collision et taille,vitesse variable des ballons
# v 8.0 : 02/05/2020 : Ajout du test si le ballon existe toujours dans la fonction fctBougerBallon
# v 9.0 : 03/05/2020 : Ajout de l'affichage du nb points du ballon lors de la collision
# v 10.0: 05/05/2020 : Ajout de la valeur des ballons dans l'entete fctAfficheLabelBallon
# v 11.0: 23/05/2020 : Ajout quelques commentaires
# v 12.0: 30/05/2020 : Suppression de la boucle d'appel entre fctBougerBallon et fctReinitialisationBallon
# v 13.0: 31/05/2020 : Ajout d'un fonction ajustant le nombres de ballon
############################

def fctEnergies(pv, pm, pg, ph):  ###respecter l'ordre des paramètres###
    ### pm masse en kg
    ### pv vitesse en m.s^-1
    ### ph hauteur en m
    ### pg en m.s^2
    ### renvoie une liste comprenant d abord l energie cinétique puis potentielle puis mécanique [c,p,m]###

    eCinetique = float(pv * pv * pm * 0.5)
    ePotentielle = float(pm * pg * ph)
    eMecanique = float(eCinetique + ePotentielle)
    liste = [eCinetique, ePotentielle, eMecanique]

    return liste


def fctEquationTrajectoire(pvinit, pangle, pg, px, phinit):
    ### pvinit en m.s^-1
    ### pg en m.s^2
    ### px abscisse en m
    ### phinit auteur initiale en m
    ### renvoie  une liste avec l abscisse et l ordonnée du boulet en fonction du temps

    abscisse = float(px)
    pangle = pangle * pi / 180
    ordonnees = float(
        - 0.5 * pg * ((abscisse) / (pvinit * cos(pangle))) * ((abscisse) / (pvinit * cos(pangle))) + (abscisse) * tan(
            pangle)) + phinit
    coordonnees = [abscisse, ordonnees]
    ##global coordonnees##

    return coordonnees


def fctVitesse(pvinit, pangleinit, pg, ptemps):
    ### pvinit vitesse initiale en m.s^-1)
    ### pangleinit en degres
    ### pg en m.s^2
    ### ptemps en s
    ### renvoie la vitesse a l'instant "temps"

    pangleinit = float(radians(pangleinit))
    x = float(pvinit * cos(pangleinit))
    y = float(-pg * ptemps + pvinit * sin(pangleinit))
    vitesse = (sqrt(x * x + y * y))
    return vitesse


def fctCreationBallon(pCan, pdBallon, pdVarGlobales):
    ### pCan Canevas ou creer le ballon
    ### pdBallon dictionnaire du ballon
    ### pdVarGlobales dictionnaire Variable Globale
    ### renvoi un objet ballon

    xDepart = fctPointDeDepartBallon(pCan)
    lBallon, hBallon = fctChoixTailleBallon(pdBallon)
    ballon = pCan.create_oval(xDepart, pCan.winfo_reqheight(), xDepart - lBallon, pCan.winfo_reqheight() - hBallon,
                              fill=fctChoixCouleurBallon(pdBallon))
    pCan.pack()
    delaims = fctCalculVitesseRafraichissementBallon(pCan, pdBallon)
    fctBougerBallon(pCan, ballon, pdBallon, pdVarGlobales, delaims)

    return ballon


def fctChoixTailleBallon(pdBallon):
    ### pdBallon dictionnaire du ballon
    ### renvoie une lise avec largeur et hauteur du ballon en pixel

    hauteur = randint(pdBallon["hauteurMin"], pdBallon["hauteurMax"])
    largeur = hauteur * pdBallon["ratioHL"]
    taille = [largeur, hauteur]

    return taille


def fctPointDeDepartBallon(pCan):
    ### pCan Canevas ou creer le ballon
    ### renvoie les coordonées x du point de depart

    largeurCan = pCan.winfo_reqwidth()
    depart = randint(10, largeurCan)

    return depart


def fctChoixCouleurBallon(pdBallon):
    ### pdBallon dictionnaire du ballon

    listeCouleur = pdBallon["listeChoixCouleur"]
    couleur = listeCouleur[randint(0, len(listeCouleur) - 1)]

    return couleur


def fctCalculVitesseRafraichissementBallon(pCan, pdBallon):
    ### pCan Canevas ou creer le ballon
    ### pdBallon dictionnaire du ballon
    ### renvoi la vitesse de rafraichissement en ms

    hauteurCan = pCan.winfo_reqheight()
    tempsDeParcoursEcran = randint(pdBallon["tempsMin"], pdBallon["tempsMax"])
    tempsPourUnPixel = float(tempsDeParcoursEcran / hauteurCan)

    return tempsPourUnPixel


def fctBougerBallon(pCan, pBallon, pdBallon, pdVarGlobales, pDelaims):
    ### pCan Canevas ou creer le ballon
    ### pBallon ballon a faire bouger
    ### pdBallon dictionnaire du ballon
    ### pdVarGlobales dictionnaire Variable Globale
    ### pdDelaisms delai rafraichissement en ms

    pCan.move(pBallon, 0, -1)
    coordBallon = pCan.coords(pBallon)
    if len(coordBallon) != 0:  # si coordonéés inexistance le ballon a déja été supprimé
        if coordBallon[3] <= 0:
            #  Ballon est sorti de l'écran
            #  on repart du bas de l'ecran
            fctReinitialisationBallon(pCan, pBallon, pdBallon, pdVarGlobales)
            pDelaims = fctCalculVitesseRafraichissementBallon(pCan, pdBallon)
            # test si la vitesse est toujours dans l'intervalle sinon
        #  il faut re-cacluler la vitesse (certainment du au changement de
        # niveau de dificulté)
        if pDelaims < pdBallon["tempsMin"] / pCan.winfo_reqheight() or int(pDelaims) > pdBallon[
            "tempsMax"] / pCan.winfo_reqheight():
            pDelaims = fctCalculVitesseRafraichissementBallon(pCan, pdBallon)
        pCan.after(int(pDelaims), fctBougerBallon, pCan, pBallon, pdBallon, pdVarGlobales, pDelaims)


def fctReinitialisationBallon(pCan, pBallon, pdBallon, pdVarGlobales):
    ### pCan Canevas ou creer le ballon
    ### pBallon ballon a faire bouger
    ### pdBallon dictionnaire du ballon
    ### pdVarGlobales dictionnaire Variable Globale

    nouveauPointDeDepart = fctPointDeDepartBallon(pCan)
    nouvelleCouleur = fctChoixCouleurBallon(pdBallon)
    pCan.itemconfig(pBallon, fill=nouvelleCouleur)
    # calcul nouvelle largeur/hauteur ballon
    largeurBallon, hauteurBallon = fctChoixTailleBallon(pdBallon)
    pCan.coords(pBallon, nouveauPointDeDepart, pCan.winfo_reqheight(), nouveauPointDeDepart + largeurBallon,
                pCan.winfo_reqheight() - hauteurBallon)


def fctAjusteNbBallon(pCan, pdBallon, pdVarGlobales, plListBallon):
    ### pCan Canevas ou creer le ballon
    ### pdBallon dictionnaire du ballon
    ### pdVarGlobales dictionnaire Variable Globale
    ### plListBallon liste des ballons

    nBallon = len(plListBallon)
    # pas assez de ballons
    if nBallon < pdBallon["nbBallonMax"]:
        # reinitialise les ballons existants
        for i in range(0, nBallon):
            fctReinitialisationBallon(pCan, plListBallon[i], pdBallon, pdVarGlobales)
        # ajout des ballons manquants
        for i in range(0, pdBallon["nbBallonMax"] - nBallon):
            plListBallon.append(fctCreationBallon(pCan, pdBallon, pdVarGlobales))
    # trop de ballons
    if nBallon > pdBallon["nbBallonMax"]:
        for i in range(0, nBallon - pdBallon["nbBallonMax"]):
            pCan.delete(plListBallon[0])
            plListBallon.remove(plListBallon[0])
        # reinitialise les ballons restants
        for i in range(0, len(plListBallon)):
            fctReinitialisationBallon(pCan, plListBallon[i], pdBallon, pdVarGlobales)


def fctCollisionBallon(pCan, pBallon, pdBallon, pdVarGlobales):
    ### pCan Canevas ou creer le ballon
    ### pBallon ballon a faire bouger
    ### pdBallon dictionnaire du ballon
    ### pdVarGlobales dictionnaire Variable Globale
    ### La fonction affiche l'explosion et met à jour le score

    x1, y1, x2, y2 = pCan.coords(pBallon)
    couleurBallon = pCan.itemcget(pBallon, "fill")
    listeCouleur = pdBallon["listeChoixCouleur"]
    scoreBallon = (listeCouleur.index(couleurBallon) + 1) * pdBallon["CoefBaseScoreBallon"]
    fctReinitialisationBallon(pCan, pBallon, pdBallon, pdVarGlobales)

    x, y = int((x2 + x1) / 2), int((y2 + y1) / 2)
    # image explosion
    listePoints = [(x - 31, y - 30), (x - 10, y - 13), (x - 7, y - 12), (x - 7, y - 17), (x - 2, y - 12), (x, y - 10),
                   (x + 13, y - 15), (x + 11, y - 8), (x + 28, y - 13), (x + 12, y), (x + 12, y + 5), (x + 21, y + 14),
                   (x + 10, y + 6), (x + 7, y + 6), (x + 6, y + 18), (x + 2, y + 7), (x - 5, y + 15), (x - 8, y + 7),
                   (x - 27, y + 22), (x - 16, y + 5), (x - 18, y), (x - 39, y - 6), (x - 17, y - 9), (x - 31, y - 30)]
    image = pCan.create_polygon(listePoints, fill=couleurBallon, outline="black")
    # on affiche le score du ballon
    texte = pCan.create_text(x, y1, text="+" + str(scoreBallon), font=('Arial', 11, 'bold'))
    # on supprime l'image apres une seconde
    pCan.after(1000, fctSupprimerImageCollision, image, texte, pCan)

    # on calcul et on affiche le nouveau score
    labelScore = pdVarGlobales["labelValeurScore"]
    ancienScore = labelScore.cget("text")
    nouveauScore = str(int(ancienScore) + scoreBallon)
    labelScore['text'] = nouveauScore


def fctSupprimerImageCollision(pImage, pTexte, pCan):
    pCan.delete(pImage)
    pCan.delete(pTexte)


def fctAfficheLabelBallon(pCan, pFrame, pdBallon, pdVarGlobales):
    ### pFrame frame ou creer le ballon
    ### pdBallon dictionnaire du ballon
    ### pdVarGlobales dictionnaire Variable Globale
    ### La fonction affiche la valeur des Ballons dans l'entete

    listeCouleur = pdBallon["listeChoixCouleur"]
    # on efface les objet de la frame avant de re-afficher les elements
    for widget in pFrame.winfo_children():
        widget.destroy()
    labelTitre = Label(pFrame, text="--- Valeurs des Ballons --- ", font=("", 9, "bold"), bg=pFrame["background"])
    labelTitre.grid(row=0, column=0, columnspan=2, sticky="ew")

    for i in range(0, len(listeCouleur)):
        scoreBallon = (i + 1) * pdBallon["CoefBaseScoreBallon"]
        labelTitre = Label(pFrame, text="Ballon " + listeCouleur[i], font=("", 9, "bold"), bg=listeCouleur[i])
        labelTitre.grid(row=i + 1, column=0, columnspan=1, sticky="ew")
        labelTitre = Label(pFrame, text=str(scoreBallon) + " pts", font=("", 9, "bold"), bg=pFrame["background"])
        labelTitre.grid(row=i + 1, column=1, columnspan=1, sticky="ew")


###test ( pas executer lors d un import)###
def fct_test_action(evt):
    if evt.keysym == "Escape":
        test_fenetre.destroy()


if __name__ == "__main__":
    maliste = fctEnergies(1, 1, 1, 1)
    vitesse = fctVitesse(10, 45, 9.81, 2)
    print("vitesse", vitesse)
    print("energie", maliste)
    test_fenetre = Tk()
    test_fenetre.attributes("-fullscreen", 1)
    test_fenetre.bind("<Key>", fct_test_action)
    fLarge = test_fenetre.winfo_screenwidth()
    fHaut = test_fenetre.winfo_screenheight()
    print("Ecran:", fLarge, fHaut)
    test_frame = Frame(test_fenetre, bg="blue")
    test_can = Canvas(test_fenetre, background="cyan", width=fLarge - 210, height=fHaut - 120, bd=0)
    test_can.pack()
    dVarGlobales["HautMax"] = dVarGlobales["LargMax"] * (float(test_can.cget("height")) / float(test_can.cget("width")))
    label_test = Label(test_fenetre, text="10", font=("", 10, "bold"), bg="yellow")
    label_test.pack()

    dVarGlobales["labelValeurScore"] = label_test
    ballon1 = fctCreationBallon(test_can, dBallon, dVarGlobales)
    # fctBougerBallon(test_can,ballon1,dBallon,dVarGlobales)
    ballon2 = fctCreationBallon(test_can, dBallon, dVarGlobales)
    # fctBougerBallon(test_can,ballon2,dBallon,dVarGlobales)
    test_can.after(5000, fctCollisionBallon, test_can, ballon2, dBallon, dVarGlobales)
    # fctCollisionBallon(test_can,ballon2,dBallon,dVarGlobales)
    test_fenetre.mainloop()