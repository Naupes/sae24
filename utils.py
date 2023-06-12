import os,pymysql
from configDB import dbConnect,serveurConnect
from mkRequest import _requetes, mkInsertRequestLieu, mkInsertRequestFleur, mkGetLieuID, mkDeleteLieuID, mkGetFleurID, mkDeleteFleurID
import mkRequest

def createBaseMySQL() -> None :
     _dbEtudiant, _cursorEtudiant = serveurConnect()
     _cursorEtudiant.execute(_requetes["drop"])
     _cursorEtudiant.execute(_requetes["createBase"])
     _cursorEtudiant.execute(_requetes["use"])
     _cursorEtudiant.execute(_requetes["createTable1"])   
     _cursorEtudiant.execute(_requetes["createTable2"])
     _cursorEtudiant.execute(_requetes["createTable3"])
     _cursorEtudiant.execute(_requetes["createTable4"])
     _cursorEtudiant.execute(_requetes["createTable5"])
     _cursorEtudiant.execute(_requetes["createTable6"])
   
def initBase() -> None :
    """ Vérifie que la base existe, sinon propose de la créer en mode CLI.
            Jette une exception si paramètres de connexion incorrects """
    try :
        execute(_requetes["getFleur"])
    except pymysql.err.OperationalError as e:
        print(e)
        if '1044' in str(e) :
            print ("Vérifiez les paramètres de connexion")
            raise e
        elif '1049' in str(e) :
            choix = input("base inexistante, voulez-vouz créer une base 'fleur' standard? (y/n) :")
            if choix not in 'yYOo' :
                raise e
            createBaseMySQL()


def execute(req : str) :    
    _dbEtudiant, _cursorEtudiant = dbConnect()
    res = _cursorEtudiant.execute(req)
    if "select" in req :
        res = _cursorEtudiant.fetchall()
    else :
        _dbEtudiant.commit()
    return res



def createBase()-> None :
    """ Crée la base fleur (uniquement MySQL actuellement) """
    execute("")
    pass


def insertFleurs(nbFleur, couleur, nom, petales, taille, typetige, eclosion, saison) -> None :
    """ Insertion de Fleurs """
    req = mkRequest.mkInsertRequestFleur(nbFleur, couleur, nom, petales, taille, typetige, eclosion, saison)
    execute(req)

def insertLieu(numLieu, region, coordonnees, departement, ville) -> None :
    """ Insertion de Lieux """
    req = mkRequest.mkInsertRequestLieu(numLieu, region, coordonnees, departement, ville)
    execute(req)    


def SupprDonneesFleurs() -> None:
     req = mkRequest._requetes['clearFleur']
     return execute(req)

def SupprDonneesLieu() -> None:
     req = mkRequest._requetes['clearLieu']
     return execute(req)



def getFleursName() -> list :
    req = _requetes["getAllName"]
    fleurs = []
    for t in execute(req) :
        fleurs.append(t)
    return fleurs

def getFleursColor() -> list :
    req = _requetes["getAllColor"]
    fleurs = []
    for t in execute(req) :
        fleurs.append(t)
    return fleurs

def getFleursId() -> list :
    req = _requetes["getAllId"]
    fleurs = []
    for t in execute(req) :
        fleurs.append(t)
    return fleurs


def deleteLieuid(numLieu : int) -> None :  
    """ Suppression de materiel dans la collection par ID """
    reqVerif = mkRequest.mkGetLieuID(numLieu)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkRequest.mkDeleteLieuID(numLieu)
    execute(req)

def deleteFleurid(nbFleur : int) -> None :  
    """ Suppression de objet dans la collection par ID """
    reqVerif = mkRequest.mkGetFleurID(nbFleur)
    if len(execute(reqVerif)) == 0 :
        raise ValueError
    req = mkRequest.mkDeleteFleurID(nbFleur)
    execute(req)
############################################
def FToString(fl : tuple) -> str :
    eclos = fl[6].strftime("%d/%m/%Y")
    return f"{fl[2].title()} : n°{fl[0]} couleur : {fl[1]} éclos le {eclos}, possède {fl[3]} pétales avec une taille de tige de {fl[4]}cm et de type {fl[5]}"

          
def getFleursStr()-> list :
    """ getEtudiantsStr() -> liste de chaînes
    Rend le contenu de la base sous forme d'une liste de chaînes """
    req = _requetes["getAllName"]
    fleurs = []
    for t in execute(req) :
        fleurs.append(FToString(t))
    return fleurs






def FNumToString(fl : tuple) -> str :
##    eclos = fl[6].strftime("%d/%m/%Y")
    return f"{fl[2].title()} : n°{fl[0]} couleur : {fl[1]} éclos le possède {fl[3]} pétales avec une taille de tige de {fl[4]}"
          
def getFleursNumStr()-> list :
    """ getEtudiantsStr() -> liste de chaînes
    Rend le contenu de la base sous forme d'une liste de chaînes """
    req = _requetes["getAllId"]
    fleurs = []
    for t in execute(req) :
        fleurs.append(FNumToString(t))
    return fleurs




#############################################


def RemplirFleursdeCSV(path : str = "fleurs.csv") -> None:
    import csv
    with open(path, newline='\n',encoding='utf-8') as csvFile :
        lignes = csv.reader(csvFile,delimiter=';')
        for champs in lignes :
            nbFleur = champs[0]
            couleur = champs[1]
            nom = champs[2]
            petales = champs[3]
            taille = champs[4]
            typetige = champs[5]
            eclosion = champs[6]
            saison = champs[7]
            insertFleurs(nbFleur, couleur, nom, petales, taille, typetige, eclosion, saison)

def RemplirLieudeCSV(path : str = "lieu.csv") -> None:
    import csv
    with open(path, newline='\n',encoding='utf-8') as csvFile :
        lignes = csv.reader(csvFile,delimiter=';')
        for champs in lignes :
            numLieu = champs[0]
            region = champs[1]
            coordonnees = champs[2]
            departement = champs[3]
            ville = champs[4]
            insertLieu(numLieu, region, coordonnees, departement, ville)






