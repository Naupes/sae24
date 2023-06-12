from configDB import dbConnect
import cherrypy, os, os.path
from mako.template import Template
from mako.lookup import TemplateLookup
from utils import initBase, execute, createBase, insertFleurs, insertLieu, SupprDonneesFleurs, FToString, getFleursStr, getFleursNumStr, FNumToString
from utils import SupprDonneesLieu, getFleursName, getFleursColor, deleteLieuid, deleteFleurid, RemplirLieudeCSV, RemplirFleursdeCSV
from interfaceCLI import MettreDonneesFleurs, MettreDonneesLieu, removeDonneesFleur, removeDonneesLieu
import mkRequest

mylookup = TemplateLookup(directories=['tamp/templates'], input_encoding='utf-8', module_directory='tamp/mako/mako_modules')

## index

class FullInterface(object):
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()

#############################################################################   Affichages 
    @cherrypy.expose
    def affParOrdre(self):
        mytemplate = mylookup.get_template("affich.html")
        return mytemplate.render(mesFleurs=getFleursStr())


    @cherrypy.expose
    def affParNum(self):
        mytemplate = mylookup.get_template("affich_num.html")
        return mytemplate.render(mesFleurs=getFleursNumStr())

################################################################################    Insertion
    @cherrypy.expose
    def insertPage(self):
                mytemplate = mylookup.get_template("insert.html")
                return mytemplate.render(message="Veuillez remplir tous les champs", type="info")

    @cherrypy.expose
    def insertDone(self, nbFleur=None, couleur=None, nom=None, petales=None, taille=None, typetige=None, eclosion=None, saison=None):
        if nbFleur and couleur and nom and petales and taille and typetige and eclosion and saison :
            print(eclosion, " -:- ", type(eclosion))
            try:
                insertFleurs(nbFleur, couleur, nom, petales, taille, typetige, eclosion, saison)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("insert.html")        
        return mytemplate.render(message=message, type=typ)

############################################################################    Suppression

    @cherrypy.expose
    def suppressById(self, numFleur=None):
        if numFleur :
            try:
                deleteFleurid(int(numFleur))
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Veuillez remplir tous les champs."
            typ = "warning"
        mytemplate = mylookup.get_template("delete.html")        
        return mytemplate.render(message=message, type=typ)




############################################### évènement(non fait)            
    @cherrypy.expose
    def insertEvent(self):
                mytemplate = mylookup.get_template("event.html")
                return mytemplate.render()



if __name__ == '__main__':
    initBase()
    removeDonneesFleur()
    MettreDonneesFleurs()
    removeDonneesLieu()
    MettreDonneesLieu()
    cherrypy.quickstart(FullInterface(), '/', 'config.txt')
