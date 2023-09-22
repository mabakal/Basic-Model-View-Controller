import csv
from skeleton.Model.model import *
data_list = []

def readData():
    
    path_ = "../NAFO-4TVN-Atlantic-Cod-otoliths.csv"
    try:
        file = open(path_, 'r')
        csv_reader = csv.reader(file)
        for line in csv_reader:
            obj = Atlantic(line[0], line[1], line[2],line[3],line[4],line[5],line[6])
            data_list.append(obj)
        print("Data load successifuly")
        data_list.remove(data_list[0])
        file.close()
    except IOError:
        print("error")
    

def persitData():

    """
        This function take a data and write it to a new file as comma separate value in memory
    """

    file_ = "new_data_file.csv"
    try:
        file = open(file_, 'w')
        for obj in data_list:
            l = str(obj.get_source()) + "," + str(obj.get_nomLatin()) + "," + str(obj.get_nomAnglais()) + "," + str(obj.get_nomFrancais()) + "," + str(obj.get_annee()) + "," + str(obj.get_mois()) + "," + str(obj.get_nombreOtolithes()) + "\n"
            file.writelines(l)
        file.close()
    except IOError:
        print("Input error")

def display(n):

    """
        This function dispaly data on the screen
        parameters:
            n- the number of data to be display
    """
    i = 0
    for data in data_list:
        if i < n:
            print(data)
            i = i + 1
        
def createData():
    """
        This function will create a new record and store it in the data structure 
    """

    source = input("Source:")
    nom_latin = input("nom lation:")
    nom_anglais = input("nom anglais:")
    nom_francais = input("Nom francais:")
    annee = input("Annee:")
    mois = input("Mois:")
    nombre = input("nombre otolithes:")
    obj = Atlantic(source=source, nom_latin=nom_latin, nom_anglais=nom_anglais, nom_francais=nom_francais, année=annee, mois=mois, nombre_otolithes=nombre)
    data_list.append(obj)
    print("The recoord is created")


def editData():
    """
        This function first will select data availible in the memory then edite it
    """
    for l in data_list:
        print(l)
    source = input("Enter source nomber:")
    print("Enter the number \n")
    print("1: edit source \n")
    print("2: edit nom latin \n")
    print("3: edit nom anglais \n")
    print("4: edit nom francais \n")
    print("5: edit annee \n")
    print("6: edit mois \n")
    print("7: edit nombre otolithes")
    nombre = int(input("Enter the number:"))
    for obj in data_list:
        if obj.get_source() == source:
            if nombre == 1:
                source = input("new source:")
                obj.set_source(source)
                break
            elif nombre == 2:
                nom_l = input("new nom latin:")
                obj.set_nomLatin(nom_l)
                break
            elif nombre == 3:
                nom_ang = input("new nom anglais:")
                obj.set_nomAnglais(nom_ang)
                break
            elif nombre == 4:
                nom_fran = input("new nom francais:")
                obj.set_nomFrancais(nom_fran)
                break
            elif nombre == 5:
                annee = input("new annee:")
                obj.set_annee(annee)
                break
            elif nombre == 6:
                mois = input("new mois:")
                obj.set_mois(mois)
                break
            else:
                nbre = input("new nombre otolithes:")
                obj.set_nombreOtolithes(nbre)
                break
    print("Update successfully")
    
def deleteDate():

    """
        This function delete a record in memory. First it display avaible record 
        then the user select the source of the record to be deleted    
    """
            
    for l in data_list:
        print(l)
    source = input("Enter source nomber:")

    for obj in data_list:
        if obj.get_source() == source:
            data_list.remove(obj)
    print("record deleted")

