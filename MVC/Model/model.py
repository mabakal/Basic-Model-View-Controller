
class Atlantic():
    """
        Definition of a class that modelize all observations
    """
    source = ""
    nom_latin = ""
    nom_anglais = ""
    nom_francais = ""
    annee = ""
    mois = ""
    nombre_otolithes = ""

    def __init__(self, source, nom_latin, nom_anglais, nom_francais, année, mois, nombre_otolithes):
        self.__source = source
        self.__nom_latin = nom_latin
        self.__nom_anglais = nom_anglais
        self.__nom_francais = nom_francais
        self.__annee = année
        self.__mois = mois
        self.__nombre_otolithes = nombre_otolithes

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6}".format(self.__source, self.__nom_latin, self.__nom_anglais, self.__nom_francais, self.__annee, self.__mois, self.__nombre_otolithes)
    """"
        Below is the definition of setters and getters.    
    """
    def set_source(self, source):
        self.__source = source
    def get_source(self):
        return str(self.__source)
    
    def set_nomLatin(self,nom_latin):
        self.__nom_latin= nom_latin
    def get_nomLatin(self):
        return str(self.__nom_latin)

    def set_nomAnglais(self,nom_anglais):
        self.__nom_anglais= nom_anglais
    def get_nomAnglais(self):
        return str(self.__nom_anglais)
    
    def set_nomFrancais(self,nom_francais):
        self.__nom_francais = nom_francais

    def get_nomFrancais(self):
        return str(self.__nom_francais)
    
    def set_mois(self,mois):
        self.mois = mois

    def get_mois(self):
        return str(self.__mois)

    def set_annee(self,annee):
        self.annee = annee

    def get_annee(self):
        return str(self.__annee)
    
    def set_nombreOtolithes(self, nombre_otolithes):
        self.__nombre_otholithes = nombre_otolithes

    def get_nombreOtolithes(self):
        return str(self.__nombre_otolithes)


