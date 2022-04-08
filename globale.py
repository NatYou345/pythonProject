############################################################################################################################################################################################################################################

###                 DEFINITION DES CONSTANTES ET MISE EN GLOBAL DE CERTAINES VARIABLES ###
### V4.0 : 18/04/2020 : Ajout dictionnaire Balllon
###                     et deplacement de la fonction fct_convCoord du module de Nathan vers globale
### V5.0 : 19/04/2020 : Ajout lListBallon et nbMaxBallon
### V6.0 : 26/04/2020 : Mise à jour Dictionnaire dBallon et ajout labelValeurScore='' dans le dictionnaire dVarGlobales
### V7.0 : 28/04/2020 : Mise à jour Dictionnaire  dVarGlobales
### V8.0 : 02/05/2020 : Mise à jour Dictionnaire dBallon ( hauteur et nombre ballon initialisation a 0 )
### V9.0 : 03/05/2020 : Mise à jour Dictionnaire  dVarGlobales
### V10.0: 03/05/2020 : Ajout d'un coef pour les valeur des ballon dans dBallon
### v11.0: 09/05/2020 : Modification des projectiles et du canon
### Dernière modification : 09/05/2020


############################################################################################################################################################################################################################################

###                 DEFINITION DES VARIABLES GLOBALES ###

dVarGlobales = dict(LargMax=170, HautMax=1, G=9.81, listIdProj=[], listIdLigne=[], can=0, canJauge=0, vMin=30, vMax=50,
                    delaiMin=50, delaiMax=5, delai=0, \
                    labelValeurScore=0, labelValeurTirs=0, niveauJeu='', temps=45, mode="S", nombreTirs=0,
                    partieEnCours=False, idLong=0, idLarg=0)

############################################################################################################################################################################################################################################

###                 DEFINITION DU CANON ###

dCanon = dict(x=3, y=1.1, longueurCanon=3.5, rayonCanon=1, epaisseurCanon=5, angleInclinaison=45, vitesseSortie=30,
              idRoue=0, idCanon=0)

############################################################################################################################################################################################################################################

###                 DEFINITION DU PROJECTILE ###

dProjectile = dict(xi=0, yi=0, x=0, y=0, rayonP=0.3, vitesse=0, vitesseX=0, idProjectile=0, masse=10, deplEnCours=0,
                   angleDepart=0, modeLancement="S")

dListeProjectiles = dict(lp=[])

############################################################################################################################################################################################################################################

###                 DEFINITION DES JAUGES ###

dJaugeEp = dict(vmin=0, vmax=0, valeur=0, posx=40, posy=220, hauteur=200, largeur=30, idJaugeFond=0, idJauge=0,
                labelVal=0, couleur="#2FA513", canvas=0)
dJaugeEc = dict(vmin=0, vmax=0, valeur=0, posx=40, posy=220, hauteur=200, largeur=30, idJaugeFond=0, idJauge=0,
                labelVal=0, couleur="#FFC000", canvas=0)
dJaugeEm = dict(vmin=0, vmax=0, valeur=0, posx=40, posy=220, hauteur=200, largeur=30, idJaugeFond=0, idJauge=0,
                labelVal=0, couleur="#FF0000", canvas=0)

############################################################################################################################################################################################################################################

###                 DEFINITION DES LABELS ###

dLabels = dict(LabVitesse=0)

############################################################################################################################################################################################################################################

###                 DEFINITION DU BALLON ###
# hauteurMin,hauteurMax en pixel ( hauteur min et max en pixel des ballons
# tempsMax,tempsMin en ms ( temps pour les ballon pour parcourir la hauteur de l'écran)
dBallon = dict(hauteurMin=0, hauteurMax=0, tempsMin=0, tempsMax=0, ratioHL=0.8, nbBallonMax=0,
               listeChoixCouleur=["slate blue", "lime green", "maroon", "orange"], CoefBaseScoreBallon=0)
lListBallon = []


############################################################################################################################################################################################################################################

### Conversion de coordonnées réelles vers des coordonnées en pixels


def fctConvCoord(pXReel, pYReel, pLargeurReelle, pHauteurReelle, pNomCan):
    xp = (float(pNomCan.cget("width")) * float(pXReel)) / float(pLargeurReelle)
    yp = float(pNomCan.cget("height")) - (float(pYReel) * float(pNomCan.cget("height"))) / float(pHauteurReelle)
    return xp, yp
