import os
from utils import initBase, execute, createBase, insertFleurs, insertLieu, SupprDonneesFleurs, getFleursStr
from utils import SupprDonneesLieu, getFleursName, getFleursColor, deleteLieuid, deleteFleurid, RemplirLieudeCSV, RemplirFleursdeCSV
from configDB import dbConnect
import mkRequest


def printParFleur()-> None :
    """ affiche le contenu de la base, rangé par ordre alphabétique des fleurs """
    for e in getFleursName() :
        print (e)
        
def printParCouleur()-> None :
    """ affiche le contenu de la base, rangé par couleur des fleurs """
    for e in getFleursColor() :
        print (e)
            
def addFleur()-> None :
    """ ajout d'une fleur """
    nbFleur = input("Entrez le numFleur : ")
    couleur = input("Entrez la couleur : ")
    nom = input("Maintenant son nom : ")
    petales = input("le nombre de pétales : ")
    taille = input("la taille : ")
    typetige = input("le type de tige")
    eclosion = input("la date d'éclosion : ")
    saison = input("la saison d'éclosion : ")
    try :
        insertFleurs(nbFleur, couleur, nom, petales, taille, typetige, eclosion, saison)
    except Exception as e :
        print ("Erreur: ", e)

def addLieu()-> None :
    """ ajout d'un lieu """
    numLieu = input("Entrez le numLieu : ")
    region = input("Entrez la région : ")
    coordonnees = input("Maintenant ses coordonnées : ")
    departement = input("Entrez le département : ")
    ville = input("Entrez le nom d'une ville : ")
    try :
        insertLieu(numLieu, region, coordonnees, departement, ville)
    except Exception as e :
        print ("Erreur: ", e)


def removeLieuByNum()-> None :
    """ supprime un lieu à l'aide de son identifiant """
    numLieu = int(input("Entrez le numéro du lieu : "))
    try :
        deleteLieuid(numLieu)
        print("FAIT")
    except ValueError as e :
        print(f"\n*** ERREUR : {e}\n")

def removeFleurByNum()-> None :
    """ supprime une fleur à l'aide de son identifiant """
    nbFleur = int(input("Entrez le numéro de la fleur : "))
    try :
        deleteFleurid(nbFleur)
        print("FAIT")
    except ValueError as e :
        print(f"\n*** ERREUR : {e}\n")



def removeDonneesFleur()-> None :
    """ supprime les données de la table fleurs """
    try :
        SupprDonneesFleurs()
        print("Données de la table fleurs supprimées")
    except ValueError as e :
        print(f"\n*** ERREUR : {e}\n")

def removeDonneesLieu()-> None :
    """ supprime les données de la table lieu """
    try :
        SupprDonneesLieu()
        print("FAIT")
    except ValueError as e :
        print(f"\n*** ERREUR : {e}\n")


def MettreDonneesFleurs()-> None :
    """ met un échantillon de données dans la table fleurs """
    RemplirFleursdeCSV('fleurs.csv')
    print("Données de la table fleurs ajoutées")

def MettreDonneesLieu()-> None :
    """ met un échantillon de données dans la table lieu """
    RemplirLieudeCSV('lieu.csv')
    print("FAIT")

def afficheMenu(choixActions : list ) -> None :
    """ Affichage du menu """
    print ("Choix possibles :")
    for ch  in choixActions:
        print (f'{choixActions.index(ch)+1} : {ch[0]}')
    print (f'{len(choixActions)+1} : Quitter')
            
if __name__ == '__main__':
    print(f"Fichiers dans le répertoire courant : {os.listdir()}")
    initBase()
    listeChoix = [ 
             ("Afficher (ordre alphabétique)",printParFleur),
             ("Afficher la collection par couleur",printParCouleur),
             ("Insérer une fleur", addFleur),
             ("Insérer un lieu", addLieu),
             ("Supprimer un lieu (par son numéro)", removeLieuByNum),
             ("Supprimer une fleur (par son numéro)", removeFleurByNum),
             ("Supprimer les données de la table fleur", removeDonneesFleur),
             ("Supprimer les données de la table lieu", removeDonneesLieu),
             ("Mettre des données dans la table lieu", MettreDonneesLieu),
             ("Mettre des données dans la table fleurs", MettreDonneesFleurs),
             ]
    while True :
        afficheMenu(listeChoix)
        try :
            choix = int(input("Votre Choix ? : "))
            if ( choix == len(listeChoix) + 1 ):
                    break
            elif 1 <= choix and choix <= len(listeChoix):
                label, fct = listeChoix[choix-1] 
                fct()
            else :
                print ("*** Choix non valide, recommencez!")
        except IndexError as e:
            print(e)
            print ('*** Choix non valide, recommencez!')
        except ValueError as e :
            print(e)
            print ('*** Entrez un entier SVP')
    print ("BYE!")
        
