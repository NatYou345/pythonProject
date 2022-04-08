from tkinter import *
from math import *
from globale import *
from module1 import *



### Programme principal ###       ### (1366*768) résolution pc valentin ###

############################
#
# v 6.0 : 26/04/2020 : met a jour dVarGlobales["labelValeurScore"]= avec le label valeurScore
# v 7.0 : 28/04/2020 : modif label et ajout difficulté et nb tir
# v 8.0 : 02/05/2020 : nouvelle fonction fctActionBouttonNiveau pour tenir compte du niveau de difficulté
# v 9.0 : 03/05/2020 : nouveau design du bandeau d'entête
# v 10.0: 03/05/2020 : modif de la vitesse et valeur des ballon en fonction de la difficulté
# v 11.0: 03/05/2020 : Mise à jour et alignement des labels de l'entente
# v 12.0: 05/05/2020 : ajout de la valeur des ballons dans l'entete
# v 13.0: 10/05/2020 : adaptation du tir en fonction du mode de jeu
#                       - possibilité de lancer plusieurs projectiles en mode jeu
#                       - un seul projectile en mode scientifique
#                       - Ajout d'un objet scale permettant de modifier la masse du projectile
# v 14.0: 30/05/2020 : blocage du mode de jeu et niveau dificulté si partie en cours
# v 15.0: 31/05/2020 : appel la fonction fctAjusteNbBallons des le choix du mode de jeu
#
### Dernière modification : 10/05/2020
############################


### Gestionnaire d'évènements ###

def fctAction(evt):
    if evt.keysym == "Escape":
        fenetre.destroy()

    #   Augmentation de l'angle d'inclinaison du canon
    #   Réaffichage du canon
    #   Réaffichage de la valeur de l'angle, hauteur maximale atteinte
    if evt.keysym == "Up":
        fctRotationCanon(dCanon, dCanon["angleInclinaison"] + 3)
        fctBougerCanon(dCanon, can, dVarGlobales)

        if dVarGlobales["mode"] == "S" and dVarGlobales["partieEnCours"] == False:
            hauteurMax = fctHauteurMaximale(dProjectile["vitesse"], dCanon["angleInclinaison"], dVarGlobales["G"],
                                            dProjectile["y"])
            fctXyProj(dProjectile, dCanon)
            fctAfficherValeur(dCanon["angleInclinaison"], labelValeurAngleActuel)
            fctAfficherValeur(hauteurMax, labelValeurHauteurMaximale)
            fctAfficherValeur(dProjectile["yi"], labelValeurHauteurActuelle)
            fctAfficherValeur(0, labelValeurDistanceParcourue)
        elif dVarGlobales["mode"] == "J":
            fctAfficherValeur(dCanon["vitesseSortie"], labelValeurVitesseInitiale)
            fctAfficherValeur(dCanon["angleInclinaison"], labelValeurAngleActuel)

    #   Diminution de l'angle d'inclinaison du canon
    #   Réaffichage du canon
    #   Réaffichage de la valeur de l'angle, hauteur maximale atteinte
    if evt.keysym == "Down":
        fctRotationCanon(dCanon, dCanon["angleInclinaison"] - 3)
        fctBougerCanon(dCanon, can, dVarGlobales)

        if dVarGlobales["mode"] == "S" and dVarGlobales["partieEnCours"] == False:
            hauteurMax = fctHauteurMaximale(dProjectile["vitesse"], dCanon["angleInclinaison"], dVarGlobales["G"],
                                            dProjectile["y"])
            fctXyProj(dProjectile, dCanon)

            fctAfficherValeur(dCanon["angleInclinaison"], labelValeurAngleActuel)
            fctAfficherValeur(hauteurMax, labelValeurHauteurMaximale)
            fctAfficherValeur(dProjectile["yi"], labelValeurHauteurActuelle)
            fctAfficherValeur(0, labelValeurDistanceParcourue)
        elif dVarGlobales["mode"] == "J":
            fctAfficherValeur(dCanon["vitesseSortie"], labelValeurVitesseInitiale)
            fctAfficherValeur(dCanon["angleInclinaison"], labelValeurAngleActuel)

    #   Diminution de la vitesse initiale du projectile
    #   Réaffichage de la valeur initiale de la vitesse, hauteur maximale atteinte
    if evt.keysym == "Left":
        fctVitesseSortieCanon(dCanon, dCanon["vitesseSortie"] - 5)
        dProjectile["vitesse"] = dCanon["vitesseSortie"]
        if dVarGlobales["mode"] == "S" and dVarGlobales["partieEnCours"] == False:
            fctVitesseProjectile(dProjectile["xi"], dProjectile)
            hauteurMax = fctHauteurMaximale(dProjectile["vitesse"], dCanon["angleInclinaison"], dVarGlobales["G"],
                                            dProjectile["yi"])
            fctAfficherValeur(dCanon["vitesseSortie"], labelValeurVitesseInitiale)
            fctAfficherValeur(dProjectile["vitesse"], labelValeurVitesseActuelle)
            fctAfficherValeur(hauteurMax, labelValeurHauteurMaximale)
            fctAfficherValeur(dProjectile["yi"], labelValeurHauteurActuelle)
            fctAfficherValeur(0, labelValeurDistanceParcourue)
        elif dVarGlobales["mode"] == "J":
            fctAfficherValeur(dCanon["vitesseSortie"], labelValeurVitesseInitiale)

    #   Diminution de la vitesse initiale du projectile
    #   Réaffichage de la valeur initiale de la vitesse, hauteur maximale atteinte
    if evt.keysym == "Right":
        fctVitesseSortieCanon(dCanon, dCanon["vitesseSortie"] + 5)
        dProjectile["vitesse"] = dCanon["vitesseSortie"]

        if dVarGlobales["mode"] == "S" and dVarGlobales["partieEnCours"] == False:
            fctVitesseProjectile(dProjectile["xi"], dProjectile)
            hauteurMax = fctHauteurMaximale(dProjectile["vitesse"], dCanon["angleInclinaison"], dVarGlobales["G"],
                                            dProjectile["yi"])
            fctAfficherValeur(dCanon["vitesseSortie"], labelValeurVitesseInitiale)
            fctAfficherValeur(dProjectile["vitesse"], labelValeurVitesseActuelle)
            fctAfficherValeur(hauteurMax, labelValeurHauteurMaximale)
            fctAfficherValeur(dProjectile["yi"], labelValeurHauteurActuelle)
            fctAfficherValeur(0, labelValeurDistanceParcourue)
        elif dVarGlobales["mode"] == "J":
            fctAfficherValeur(dCanon["vitesseSortie"], labelValeurVitesseInitiale)

    if evt.keysym == "Return":
        #       Affichage de l'état du canon (vitesse initiale et angle d'inclinaison

        fctAfficherValeur(dCanon["vitesseSortie"], labelValeurVitesseInitiale)
        fctAfficherValeur(dCanon["angleInclinaison"], labelValeurAngleActuel)

        #       Lancement du projectile en mode Scientifique

        if dVarGlobales["mode"] == "S":
            #           En mode scientifique, on ne peut lancer qu'un seul projectile à la fois
            if dVarGlobales["partieEnCours"] == False:
                gListProjectile = []
                dProjectile["masse"] = float(gMasse.get())
                dProjectile["angleDepart"] = dCanon["angleInclinaison"]
                dProjectile["vitesse"] = dCanon["vitesseSortie"]
                dProjectileCopie = dProjectile.copy()
                gListProjectile.append(dProjectileCopie)

                #
                if dVarGlobales["listIdLigne"] != []:
                    fctEffacerTrajectoire(dVarGlobales["listIdLigne"], can)

                dVarGlobales["partieEnCours"] = True

                boutonModeJeu.grid_remove()
                boutonModeScientifique.grid_remove()
                labelMode.configure(text="Mode Scientifique")
                boutonNiveauFacile.grid_remove()
                boutonNiveauDifficile.grid_remove()
                labelNiveau.configure(text="Niveau")

                dVarGlobales["nombreProjectiles"] = 1
                i = 0
                dVarGlobales["nombreTirs"] += 1
                fctAfficherValeur(dVarGlobales["nombreTirs"], dVarGlobales["labelValeurTirs"])

                #               Adapter la longueur réelle du champ de tir en fonction de la distance totale parcourue par le projectile
                #               --------------------------------------------------------------------------------------------------------
                dist = fctDistanceParcourue(gListProjectile[i]["vitesse"], dCanon["angleInclinaison"],
                                            dVarGlobales["G"], gListProjectile[i]["yi"])
                dVarGlobales["LargMax"] = (int((dist + dProjectile[
                    "yi"]) / 10) + 2) * 10  # On arrondit la distance à deux dizaines supérieures.
                dVarGlobales["HautMax"] = dVarGlobales["LargMax"] * (
                            float(can.cget("height")) / float(can.cget("width")))
                if dVarGlobales["idLong"] > 0:
                    can.delete(dVarGlobales["idLong"])
                dVarGlobales["idLong"] = can.create_text(int(can.cget("width")) - 30, int(can.cget("height")) - 20,
                                                         fill="white",
                                                         text="Longeur\n" + str(int(dVarGlobales["LargMax"])) + " m",
                                                         font=("", -12, "bold"))
                if dVarGlobales["idLarg"] > 0:
                    can.delete(dVarGlobales["idLarg"])
                dVarGlobales["idLarg"] = can.create_text(30, 20,
                                                         text="Hauteur\n" + str(int(dVarGlobales["HautMax"])) + " m",
                                                         font=("", -12, "bold"))

                fctEffacerCanon(dCanon, can)
                fctAfficherCanon(dCanon, can, dVarGlobales)

                fctXyProj(gListProjectile[i], dCanon)

                fctAfficherProjectile(gListProjectile[i], can, dVarGlobales)

                vitesseMax = fctVitesseProjectile(dist + gListProjectile[i]["xi"], gListProjectile[i])
                hauteurMax = fctHauteurMaximale(gListProjectile[i]["vitesse"], gListProjectile[i]["angleDepart"],
                                                dVarGlobales["G"], gListProjectile[i]["yi"])
                fctAfficherValeur(hauteurMax, labelValeurHauteurMaximale)
                fctAfficherValeur(dCanon["angleInclinaison"], labelValeurAngleActuel)
                lEnergie = []
                lEnergie = fctEnergies(vitesseMax, gListProjectile[i]["masse"], dVarGlobales["G"], hauteurMax)
                dJaugeEp["vmax"] = lEnergie[2] * 1.1
                dJaugeEp["idJauge"] = fctAfficherJauge(dJaugeEp, canJaugeEp)
                dJaugeEc["vmax"] = lEnergie[2] * 1.1
                dJaugeEc["idJauge"] = fctAfficherJauge(dJaugeEc, canJaugeEc)
                dJaugeEm["vmax"] = lEnergie[2] * 1.1
                dJaugeEm["idJauge"] = fctAfficherJauge(dJaugeEm, canJaugeEm)
                lEnergie = fctEnergies(gListProjectile[i]["vitesse"], gListProjectile[i]["masse"], dVarGlobales["G"],
                                       gListProjectile[i]["yi"])
                gListProjectile[i]["modeLancement"] = dVarGlobales["mode"]
                fctAfficherTrajectoire(gListProjectile[i], dVarGlobales, dJaugeEp, dJaugeEc, dJaugeEm, can,
                                       labelValeurHauteurActuelle, labelValeurDistanceParcourue, \
                                       labelValeurVitesseActuelle, boutonModeScientifique, boutonModeJeu, labelMode)

        #       Lancement du projectile en mode Jeu

        if (dVarGlobales["mode"] == "J"):

            if not dVarGlobales["partieEnCours"]:
                gListProjectile = []
                dListeProjectiles["lp"] = []
                dVarGlobales["partieEnCours"] = True
                dVarGlobales["nombreTirs"] = 0

            boutonModeJeu.grid_remove()
            boutonModeScientifique.grid_remove()
            labelMode.configure(text="Mode Jeu")

            boutonNiveauFacile.grid_remove()
            boutonNiveauDifficile.grid_remove()
            if dVarGlobales["niveauJeu"] == "F":
                labelNiveau.configure(text="Niveau facile")
            else:
                labelNiveau.configure(text="Niveau difficile")

            if dVarGlobales["idLong"] > 0:
                can.delete(dVarGlobales["idLong"])
            if dVarGlobales["idLarg"] > 0:
                can.delete(dVarGlobales["idLarg"])

            dProjectile["angleDepart"] = dCanon["angleInclinaison"]
            dProjectile["vitesse"] = dCanon["vitesseSortie"]
            gListProjectile = dListeProjectiles["lp"]
            dProjectileCopie = dProjectile.copy()
            gListProjectile.append(dProjectileCopie)
            dListeProjectiles["lp"] = gListProjectile
            dVarGlobales["nombreTirs"] += 1
            i = dVarGlobales["nombreTirs"] - 1
            if i == 0:
                fctHorloge(can, dVarGlobales, gListProjectile[i], labelValeurScore, labelValeurTirs, labelValeurTemps,
                           fenetre, \
                           boutonModeJeu, boutonModeScientifique, labelMode, boutonNiveauFacile, boutonNiveauDifficile,
                           labelNiveau)

            if dVarGlobales["listIdLigne"] != []:
                fctEffacerTrajectoire(dVarGlobales["listIdLigne"], can)

            fctAfficherValeur(dVarGlobales["nombreTirs"], dVarGlobales["labelValeurTirs"])
            fctXyProj(gListProjectile[i], dCanon)

            fctAfficherProjectile(gListProjectile[i], can, dVarGlobales)

            gListProjectile[i]["modeLancement"] = dVarGlobales["mode"]
            fctAfficherTrajectoire(gListProjectile[i], dVarGlobales, dJaugeEp, dJaugeEc, dJaugeEm, can,
                                   labelValeurHauteurActuelle, labelValeurDistanceParcourue, \
                                   labelValeurVitesseActuelle, boutonModeScientifique, boutonModeJeu, labelMode)


# fonction appelée lors du changement de niveau de difficulté
def fctActionBouttonNiveau():
    if dVarGlobales["mode"] == "S":
        boutonNiveauFacile.grid_remove()
        boutonNiveauDifficile.grid_remove()
        labelNiveau.configure(text="     Niveau     ")
        return

    dVarGlobales["niveauJeu"] = choixNiveauJeu.get()

    if dVarGlobales["niveauJeu"] == "F":
        dBallon["nbBallonMax"] = 50
        dBallon["hauteurMin"] = 30
        dBallon["hauteurMax"] = 45
        dBallon["tempsMin"] = 15000
        dBallon["tempsMax"] = 30000
        dBallon["CoefBaseScoreBallon"] = 10
        fctAfficheLabelBallon(can, fBallon, dBallon, dVarGlobales)
    else:
        dBallon["nbBallonMax"] = 25
        dBallon["hauteurMin"] = 15
        dBallon["hauteurMax"] = 29
        dBallon["tempsMin"] = 3000
        dBallon["tempsMax"] = 15000
        dBallon["CoefBaseScoreBallon"] = 20
        fctAfficheLabelBallon(can, fBallon, dBallon, dVarGlobales)
    # creer ou ajuste le nombre de ballons
    fctAjusteNbBallon(can, dBallon, dVarGlobales, lListBallon)


def fctActionMode():
    if dVarGlobales["partieEnCours"] == False:
        dVarGlobales["mode"] = choixMode.get()
        if dVarGlobales["mode"] == "J":
            dProjectile["vitesse"] = 30
            dProjectile["vitesseX"] = ""
            canJaugeEp.delete(dJaugeEp["idJauge"])
            canJaugeEc.delete(dJaugeEc["idJauge"])
            canJaugeEm.delete(dJaugeEm["idJauge"])
            dJaugeEp["idJauge"] = 0
            dJaugeEc["idJauge"] = 0
            dJaugeEm["idJauge"] = 0
            fctAfficherValeur("", dJaugeEp["label"])
            fctAfficherValeur("", dJaugeEc["label"])
            fctAfficherValeur("", dJaugeEm["label"])
            fctBougerCanon(dCanon, can, dVarGlobales)
            fctXyProj(dProjectile, dCanon)

            fctAfficherValeur(dProjectile["vitesse"], labelValeurVitesseInitiale)
            fctAfficherValeur(dProjectile["vitesseX"], labelValeurVitesseActuelle)
            fctAfficherValeur(dCanon["angleInclinaison"], labelValeurAngleActuel)
            fctAfficherValeur("", labelValeurHauteurMaximale)
            fctAfficherValeur("", labelValeurHauteurActuelle)
            fctAfficherValeur(0, labelValeurDistanceParcourue)

            boutonNiveauFacile.grid()
            boutonNiveauDifficile.grid()
            labelNiveau.configure(text="     Niveau     ")

            fctActionBouttonNiveau()

    # Si on passe au mode jeu, on efface la trajectoire affichée
    if dVarGlobales["mode"] == "J":
        fctEffacerTrajectoire(dVarGlobales["listIdLigne"], can)

    # Si on passe au mode scientifique, on efface les ballons
    if dVarGlobales["mode"] == "S":
        boutonNiveauFacile.grid_remove()
        boutonNiveauDifficile.grid_remove()
        labelNiveau.configure(text="     Niveau     ")
        # plus de ballons
        dBallon["nbBallonMax"] = 0
        fctAjusteNbBallon(can, dBallon, dVarGlobales, lListBallon)


dVarGlobales["nombreProjectiles"] = 0
i = 0

fenetre = Tk()

fenetre.attributes("-fullscreen", 1)
fenetre.title("Conservation de l'énergie")
fenetre.bind("<Key>", fctAction)
fenetre.configure(background="white")
gWidth = fenetre.winfo_screenwidth()
gHeight = fenetre.winfo_screenheight()

##########################################################################################################

### DEFINITION DE LA FENETRE

fondEntete = "#FFFF99"
fondJeu = "#00FF00"
fondBallon = "#00FFFF"
tailleTexte = 12
tailleValeur = 12
tailleScore = 18

fEntete = Frame(fenetre, width=gWidth * 5 / 9, height=180, bg=fondEntete)
fEntete.grid(row=0, column=0, columnspan=2, sticky="wnes")
fEntete.grid_propagate(0)

fBallon = Frame(fenetre, width=gWidth * 1 / 9, height=180, bg=fondBallon)
fBallon.grid(row=0, column=2, columnspan=1, sticky="wnes")
fBallon.grid_propagate(0)

fJeu = Frame(fenetre, width=gWidth * 1 / 3, height=180, bg=fondJeu)
fJeu.grid(row=0, column=3, columnspan=1, sticky="wnes")
fJeu.grid_propagate(0)

fJauges = Frame(fenetre, bg="white")
fJauges.grid(row=1, column=0, sticky="nw")

fGraphique = Frame(fenetre, bg="cyan")
fGraphique.grid(row=1, column=1, columnspan=3, rowspan=2, sticky="nw")
can = Canvas(fGraphique, background="cyan", width=gWidth - 220, height=gHeight - 180, bd=0)

imageFond = PhotoImage(file="imageFond.png")
can.create_image(0, 0, image=imageFond, anchor="nw")
can.pack()

labelTitre = Label(fEntete, text="Conservation de l'énergie mécanique -------- The Canon Game\n", font=("", 18, "bold"),
                   bg=fondEntete)
labelTitre.grid(row=0, column=0, columnspan=13, sticky="ew")

labelVitesseInitiale = Label(fEntete, text="Vitesse initiale (m/s): ", font=("", tailleTexte, "bold"), bg=fondEntete)
labelVitesseInitiale.grid(row=2, column=0, sticky="e")

labelValeurVitesseInitiale = Label(fEntete, text="", fg="red", bg=fondEntete, font=("", tailleValeur, "bold"))
labelValeurVitesseInitiale.grid(row=2, column=1, sticky="e")

labelAngleActuel = Label(fEntete, text="Angle actuel (° deg): ", font=("", tailleTexte, "bold"), bg=fondEntete)
labelAngleActuel.grid(row=3, column=0, sticky="e")

labelValeurAngleActuel = Label(fEntete, text="0", fg="red", bg=fondEntete, font=("", tailleValeur, "bold"))
labelValeurAngleActuel.grid(row=3, column=1, sticky="e")

labelVitesseActuelle = Label(fEntete, text="Vitesse actuelle (m/s): ", font=("", tailleTexte, "bold"), bg=fondEntete)
labelVitesseActuelle.grid(row=2, column=2, sticky="e")

labelValeurVitesseActuelle = Label(fEntete, text="", fg="red", bg=fondEntete, font=("", tailleValeur, "bold"))
labelValeurVitesseActuelle.grid(row=2, column=3, sticky="e")

labelHauteurActuelle = Label(fEntete, text="Hauteur actuelle (m): ", font=("", tailleTexte, "bold"), bg=fondEntete)
labelHauteurActuelle.grid(row=3, column=2, sticky="e")

labelValeurHauteurActuelle = Label(fEntete, text="", fg="red", bg=fondEntete, font=("", tailleValeur, "bold"))
labelValeurHauteurActuelle.grid(row=3, column=3, sticky="e")

labelHauteurMaximale = Label(fEntete, text="Hauteur maximale (m): ", font=("", tailleTexte, "bold"), bg=fondEntete)
labelHauteurMaximale.grid(row=2, column=4, sticky="e")

labelValeurHauteurMaximale = Label(fEntete, text="", fg="red", bg=fondEntete, font=("", tailleValeur, "bold"))
labelValeurHauteurMaximale.grid(row=2, column=5, sticky="e")

labelDistanceParcourue = Label(fEntete, text="Distance parcourue (m): ", font=("", tailleTexte, "bold"), bg=fondEntete)
labelDistanceParcourue.grid(row=3, column=4, sticky="e")

labelValeurDistanceParcourue = Label(fEntete, text="", fg="red", bg=fondEntete, font=("", tailleValeur, "bold"))
labelValeurDistanceParcourue.grid(row=3, column=5, sticky="e")

gMasse = IntVar()
gMasse.set(10)
sScale = Scale(fEntete, orient='horizontal', from_=5, to=20, resolution=1, tickinterval=0, length=100,
               label='Masse (kg)', bg=fondEntete, \
               variable=gMasse, font=("", 10, "bold"))
sScale.grid(row=4, column=0)

labelMode = Label(fJeu, text="Mode", font=("", 10, "bold"), bg=fondJeu)
labelMode.grid(row=0, column=0)

dVarGlobales["mode"] = "S"

choixMode = StringVar()
choixMode.set(dVarGlobales["mode"])

boutonModeScientifique = Radiobutton(fJeu, command=fctActionMode, variable=choixMode, text="Scientifique", value="S",
                                     bg=fondJeu, font=("", 10, "bold"))
boutonModeScientifique.grid(row=1, column=0, sticky="w")

boutonModeJeu = Radiobutton(fJeu, command=fctActionMode, variable=choixMode, text="Jeu", value="J", bg=fondJeu,
                            font=("", 10, "bold"))
boutonModeJeu.grid(row=2, column=0, sticky="w")

labelNiveau = Label(fJeu, text="Niveau", font=("", 10, "bold"), bg=fondJeu)
labelNiveau.grid(row=0, column=1)

dVarGlobales["niveauJeu"] = "F"

choixNiveauJeu = StringVar()
choixNiveauJeu.set(dVarGlobales["niveauJeu"])

boutonNiveauFacile = Radiobutton(fJeu, command=fctActionBouttonNiveau, variable=choixNiveauJeu, text="Facile",
                                 value="F", bg=fondJeu, font=("", 10, "bold"))
boutonNiveauFacile.grid(row=1, column=1, sticky="w")

boutonNiveauDifficile = Radiobutton(fJeu, command=fctActionBouttonNiveau, variable=choixNiveauJeu, text="Difficile",
                                    value="D", bg=fondJeu, font=("", 10, "bold"))
boutonNiveauDifficile.grid(row=2, column=1, sticky="w")

labelTirs = Label(fJeu, text=" Tirs ", font=("", tailleScore, "bold"), bg=fondJeu)
labelTirs.grid(row=0, column=2)

labelValeurTirs = Label(fJeu, text="0", fg="red", bg=fondJeu, font=("", tailleScore, "bold"))
labelValeurTirs.grid(row=1, column=2, rowspan=2)
dVarGlobales["labelValeurTirs"] = labelValeurTirs

labelScore = Label(fJeu, text=" Score ", font=("", tailleScore, "bold"), bg=fondJeu)
labelScore.grid(row=0, column=3)

labelValeurScore = Label(fJeu, text="0", fg="red", bg=fondJeu, font=("", tailleScore, "bold"))
labelValeurScore.grid(row=1, column=3, rowspan=2)
dVarGlobales["labelValeurScore"] = labelValeurScore

labelTemps = Label(fJeu, text="Fin dans", font=("", tailleScore, "bold"), bg=fondJeu)
labelTemps.grid(row=0, column=4, sticky="e")

labelValeurTemps = Label(fJeu, text=dVarGlobales["temps"], font=("", 36, "bold"), bg=fondJeu)
labelValeurTemps.grid(row=1, column=4, rowspan=2, sticky="e")

##########################################################################################################

##########################################################################################################

#                       DEFINITION DES IMAGES

toucheEntree = PhotoImage(file="enter.png")
toucheFlecheBas = PhotoImage(file="flèche bas.png")
toucheFlecheHaut = PhotoImage(file="flèche haut.png")
toucheFlecheDroite = PhotoImage(file="flèche droite.png")
toucheFlecheGauche = PhotoImage(file="flèche gauche.png")
toucheEchap = PhotoImage(file="échap.png")

###########################################################################################################

### DEFINITION DES LABELS ET FRAMES POUR LES ENERGIES


labelEnergies = Label(fJauges, text="\nEnergies\n", font=("", 14, "bold"), bg="white")
labelEnergies.grid(row=0, column=0, columnspan=3)

labelEp = Label(fJauges, text="0", bg="white")
labelEp.grid(row=1, column=0)

labelEc = Label(fJauges, text="0", bg="white")
labelEc.grid(row=1, column=1)

labelEm = Label(fJauges, text="0", bg="white")
labelEm.grid(row=1, column=2)

hjauge = 200

fJaugeEp = Frame(fJauges, bg="blue")
fJaugeEp.grid(row=2, column=0)
canJaugeEp = Canvas(fJaugeEp, background="white", width=60, height=hjauge, bd=0)
canJaugeEp.pack()

dJaugeEp["canvas"] = canJaugeEp
dJaugeEp["hauteur"] = int(canJaugeEp.cget("height"))
dJaugeEp["posx"] = int(canJaugeEp.cget("width")) / 2
dJaugeEp["posy"] = dJaugeEp["hauteur"]

fJaugeEc = Frame(fJauges, bg="blue")
fJaugeEc.grid(row=2, column=1)
canJaugeEc = Canvas(fJaugeEc, background="white", width=60, height=hjauge, bd=0)
canJaugeEc.pack()

dJaugeEc["canvas"] = canJaugeEc
dJaugeEc["hauteur"] = int(canJaugeEc.cget("height"))
dJaugeEc["posx"] = int(canJaugeEc.cget("width")) / 2
dJaugeEc["posy"] = dJaugeEc["hauteur"]

fJaugeEm = Frame(fJauges, bg="blue")
fJaugeEm.grid(row=2, column=2)
canJaugeEm = Canvas(fJaugeEm, background="white", width=60, height=hjauge, bd=0)
canJaugeEm.pack()

dJaugeEm["canvas"] = canJaugeEm
dJaugeEm["hauteur"] = int(canJaugeEm.cget("height"))
dJaugeEm["posx"] = int(canJaugeEm.cget("width")) / 2
dJaugeEm["posy"] = dJaugeEm["hauteur"]

labelLegEp = Label(fJauges, text="Ep (J)", font=("", 8, "bold"), bg="white")
labelLegEp.grid(row=3, column=0)

labelLegEc = Label(fJauges, text="Ec (J)", font=("", 8, "bold"), bg="white")
labelLegEc.grid(row=3, column=1)

labelLegEm = Label(fJauges, text="Em (J)", font=("", 8, "bold"), bg="white")
labelLegEm.grid(row=3, column=2)

labelAideTitre = Label(fJauges, text="\n\nAide :\n", font=("", 14, "bold"), bg="white")
labelAideTitre.grid(row=4, column=0, columnspan=3)

labelAide1 = Label(fJauges, text="Angle", bg="white")
labelAide1.grid(row=5, column=0)

labelTouche1 = Label(fJauges, image=toucheFlecheHaut)
labelTouche1.grid(row=5, column=1)

labelTouche2 = Label(fJauges, image=toucheFlecheBas)
labelTouche2.grid(row=5, column=2)

labelAide2 = Label(fJauges, text="Vitesse", bg="white")
labelAide2.grid(row=6, column=0)

labelTouche3 = Label(fJauges, image=toucheFlecheGauche)
labelTouche3.grid(row=6, column=1)

labelTouche4 = Label(fJauges, image=toucheFlecheDroite)
labelTouche4.grid(row=6, column=2)

labelAide3 = Label(fJauges, text="Tir", bg="white")
labelAide3.grid(row=7, column=0)

labelTouche5 = Label(fJauges, image=toucheEntree)
labelTouche5.grid(row=7, column=1, columnspan=2)

labelAide4 = Label(fJauges, text="Quitter : ", bg="white")
labelAide4.grid(row=8, column=0)

labelTouche6 = Label(fJauges, image=toucheEchap)
labelTouche6.grid(row=8, column=1, columnspan=2)

dVarGlobales["can"] = can

dVarGlobales["HautMax"] = dVarGlobales["LargMax"] * (float(can.cget("height")) / float(can.cget("width")))

fctAfficherCanon(dCanon, can, dVarGlobales)
fctXyProj(dProjectile, dCanon)
dProjectile["vitesse"] = 30
dProjectile["vitesseX"] = 30

hauteurMax = fctHauteurMaximale(dProjectile["vitesse"], dCanon["angleInclinaison"], dVarGlobales["G"], dProjectile["y"])

fctAfficherValeur(dProjectile["vitesse"], labelValeurVitesseInitiale)
fctAfficherValeur(dProjectile["vitesse"], labelValeurVitesseActuelle)
fctAfficherValeur(dCanon["angleInclinaison"], labelValeurAngleActuel)
fctAfficherValeur(hauteurMax, labelValeurHauteurMaximale)
fctAfficherValeur(dProjectile["yi"], labelValeurHauteurActuelle)
fctAfficherValeur(0, labelValeurDistanceParcourue)

lEnergie = []
lEnergie = fctEnergies(dProjectile["vitesse"], dProjectile["masse"], dVarGlobales["G"], hauteurMax)
dJaugeEp["vmax"] = lEnergie[1] * 1.1
dJaugeEc["vmax"] = lEnergie[0] * 1.1
dJaugeEm["vmax"] = lEnergie[2] * 1.1

dJaugeEp["idJaugeFond"] = fctAfficherJaugeFond(dJaugeEp, canJaugeEp)
dJaugeEp["label"] = labelEp

dJaugeEc["idJaugeFond"] = fctAfficherJaugeFond(dJaugeEc, canJaugeEc)
dJaugeEc["label"] = labelEc

dJaugeEm["idJaugeFond"] = fctAfficherJaugeFond(dJaugeEm, canJaugeEm)
dJaugeEm["label"] = labelEm

fctActionBouttonNiveau()  # pour initialiser la première fois les ballons en fonction du niveau de jeux

fenetre.mainloop()


