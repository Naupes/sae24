_requetes = {
    "drop" : "DROP DATABASE IF EXISTS fleur",
    "createBase" : "CREATE DATABASE IF NOT EXISTS fleur DEFAULT CHARACTER SET utf8",
    "use" : "USE fleur",

    "createTable1" : "CREATE TABLE fleurs ( nbFleur INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
    couleur ENUM('bleu','rouge','vert','orange','rose','jaune','violet','blanc') NOT NULL DEFAULT 'rouge',\
    nom VARCHAR(20) DEFAULT NULL,\
    petales INT(11) DEFAULT NULL,\
    taille INT(11) DEFAULT NULL,\
    typetige VARCHAR(10) DEFAULT NULL,\
    eclosion DATE DEFAULT NULL,\
    saison ENUM('Printemps', 'Été', 'Automne', 'Hiver') DEFAULT NULL )ENGINE=InnoDB;",
    
    "createTable2" : "CREATE TABLE lieu ( numLieu int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
    region VARCHAR(20) DEFAULT NULL,\
    coordonnees VARCHAR(30) DEFAULT NULL,\
    departement VARCHAR(30) DEFAULT NULL,\
    ville VARCHAR(20) DEFAULT NULL )ENGINE=InnoDB;",

    "createTable3" : "CREATE TABLE se_situer ( clefleur int(11) NOT NULL,\
    clelieu INT(11) NOT NULL,\
    cardinaux enum('Nord','Sud','Est','Ouest') DEFAULT NULL,\
    PRIMARY KEY (clefleur, clelieu),\
    FOREIGN KEY (clefleur) REFERENCES fleurs(nbFleur) ON UPDATE CASCADE ,\
    FOREIGN KEY (clelieu) REFERENCES lieu(numLieu) ON UPDATE CASCADE )ENGINE=InnoDB;",

    "createTable4" : "CREATE TABLE evenements ( numEvenement int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
    date DATE NOT NULL,\
    lieu VARCHAR(30) NOT NULL,\
    nb_participants INT(10) DEFAULT NULL,\
    numLieu INT(10) NOT NULL,\
    FOREIGN KEY (numLieu) REFERENCES lieu(numLieu) ON UPDATE CASCADE )ENGINE=InnoDB;",

    "createTable5" : "CREATE TABLE amateurs ( numAmateur int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,\
    nom VARCHAR(30) DEFAULT NULL,\
    prenom VARCHAR(30) DEFAULT NULL,\
    age int(3) DEFAULT NULL,\
    resi_ville VARCHAR(30) DEFAULT NULL,\
    resi_region VARCHAR(20) DEFAULT NULL)ENGINE=InnoDB;",

    "createTable6" : "CREATE TABLE participer_a ( cleevenement int(11) NOT NULL,\
    cleamateur INT(11) NOT NULL,\
    PRIMARY KEY (cleevenement, cleamateur),\
    FOREIGN KEY (cleevenement) REFERENCES evenements(numEvenement) ON UPDATE CASCADE ,\
    FOREIGN KEY (cleamateur) REFERENCES amateurs(numAmateur) ON UPDATE CASCADE )ENGINE=InnoDB;",


    "insertFleur" : "insert into fleurs (nbFleur, couleur, nom, petales, taille, typetige, eclosion, saison) values ('{}','{}','{}','{}','{}','{}','{}','{}');",
    "insertLieu" : "insert into lieu (numLieu, region, coordonnees, departement, ville) values ('{}','{}','{}','{}','{}');",

    "clearFleur" : "DELETE FROM fleurs;",
    "clearLieu" : "DELETE FROM lieu;",

    "getFleur" : "select * from fleurs where nbFleur = '{}';",
    "getLieu" : "select * from lieu where numLieu = '{}';",
    "deleteFleurById" : "delete from fleurs where nbFleur = '{}';",
    "deleteLieuById" : "delete from lieu where numLieu = '{}';",
    
    "getAllColor" : "select * from fleurs order by couleur;",
    "getAllName" : "select * from fleurs order by nom;",
    "getAllId" : "select * from fleurs order by nbFleur;",
    
    "reset" : "truncate table fleurs;",}

    
def mkInsertRequestFleur(nbFleur, couleur, nom, petales, taille, typetige, eclosion, saison) :
    s= _requetes["insertFleur"].format(nbFleur, couleur, nom, petales, taille, typetige, eclosion, saison)
    return s

def mkInsertRequestLieu(numLieu, region, coordonnees, departement, ville) :
    s= _requetes["insertLieu"].format(numLieu, region, coordonnees, departement, ville)
    return s

##def mkInsertRequest(prenom, nom, anniversaire) :                  à faire pour insert des données
##    s= _requetes["insert"].format(nbFleur)                        pour la partie publique
##    return set                                                    (les 2 autres tables)
##
##def mkInsertRequest(prenom, nom, anniversaire) :
##    s= _requetes["insert"].format(prenom.capitalize(),nom.upper(),anniversaire)
##    return s

def mkGetLieuID(numLieu) :
    s= _requetes["getLieu"].format(numLieu)
    return s

def mkDeleteLieuID(numLieu) :
    s= _requetes["deleteLieuById"].format(numLieu)
    return s


def mkGetFleurID(nbFleur) :
    s= _requetes["getFleur"].format(nbFleur)
    return s

def mkDeleteFleurID(nbFleur) :
    s= _requetes["deleteFleurById"].format(nbFleur)
    return s
        
