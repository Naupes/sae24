import os
import pymysql

def getParamsConnexion() -> tuple:

    base = 'etudiants'
    serveur = "localhost"
    utilisateur = "admin"
    mdp = "admin"
    numPort = 3306     # port MySQL standard (par défaut)
    try :
        with open("configDBcours.txt") as f :
            for ligne in f :
                if len(ligne)<5 or ligne[0] == '#' :
                    continue
                champs = ligne.split(':')
                if 'nombase' in champs[0] :
                    base = champs[1].strip()
                elif 'host' in champs[0] :
                    serveur = champs[1].strip()
                elif 'user' in champs[0] :
                    utilisateur = champs[1].strip()
                elif 'pass' in champs[0] :
                    mdp = champs[1].strip()
                elif 'port' in champs[0] and len(champs[1].strip()) < 3 :          # pas obligatoire!
                    numPort = int(champs[1].strip())
    except FileNotFoundError as e :
        print("'configDB.txt' absent, utilisation des valeurs par défaut")
    return (serveur,utilisateur,mdp,base,numPort)

        
def dbConnect():
    s,u,m,b,p = getParamsConnexion()                         
    db = pymysql.connect(host=s, charset="utf8", user=u, passwd=m, db=b, port=p)
    return (db,db.cursor())


def serveurConnect():
    s,u,m,b,p = getParamsConnexion()     
    db = pymysql.connect(host=s, charset="utf8", user=u, passwd=m, port=p)
    return (db,db.cursor())












