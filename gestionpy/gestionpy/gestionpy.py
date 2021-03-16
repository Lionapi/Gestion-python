# coding: utf-8

## Débuts python 'https://python-django.dev' ##

################################################################

# petite variable
a = 14

# affichage de la variable avec la fonction psecial format
print("Toto a {} ans.".format(a))
print(f"Toto a {a}")

################################################################

# liste et tableau
tab = ["A", "B", "C"]

# ajout d'une valeur
tab.append("D")

# retirer un élèment de tab par sa valeur
#tab.remove("D")

# retirer un élèment de tab par son index
#del tab[3]

# affiche la liste ou le tableau
print("Le tableau compte {} élèment(s).".format(len(tab)))
#print(tab)

# affiche tous les élèments de tab
#for tb in tab:
    #print(tb)
    
# affiche tous les élèments de tab avec leur index
#for tb in enumerate(tab):
#    print(tb)

#copions la variable tab
#table = tab[:]
#print(table)
# ou
import copy
table = copy.deepcopy(tab)
print(table)
#tab.reverse()
#table.extend(tab)
#print(table[:2]) #table[-2:] #deux premiers et deux derniers élèments

################################################################

# un tuple permet une affectation multiple et renvoie plusieurs valeurs

def renvoie_tuple():
    v1, v2, v3 = 10, 11, 12
    _tuple = ("A", 1, 2)
    return v1, v2, v3, _tuple

print(renvoie_tuple())

################################################################

# dictionnaire / json
dct = {} # ou dct = dict()
dct["Nom"] = "Toto"
dct["Age"] = 25
dct["Autres"] = "{records:[{'A':1, 'B':2}]}"
#print(dct.get("Autres"))
#print("{} a {} ans aujourd'hui.".format(dct["Nom"], dct["Age"]))

#for k,v in dct.items():
    #print(k,v)

################################################################

# fonctions

def addition(x, y):
    print("La somme de {} et de {} donne {}".format(x, y, x+y))

def tablemultiplication(x):
    for y in range(1, 11):
        print("{} x {} = {}".format(x, y, x*y)) 
        
def test(*x):
    return x

def _test(**x):
    return x["Titi"]    
    
#addition(2,3)
#tablemultiplication(2)
#print(test())
#print(_test(Titi=0))
      
################################################################

# fonctions natives
#print("noM".capitalize()) #print(bin(5)) #print(all/any([True, 0])) #print(abs(-1))

#import random
#print(random.randint(1,11)) #print(random.choice([0,1,2,3,4,5]))

#bb = [2, 5, 10, 0]
#bb.sort()
#del bb[3]
#print(bb) #print(":".join('aaa')) #print("012345".isalpha()) #print("012345".find("6")) #print("012345".endswith("5")) #print([0,1,2,3,4,5].count(5))

################################################################

# condition et boucle
#cb = 1

#if cb == 0:
    #print(cb)
#elif cb > 0 or cb >= 1:
    #print("{} est positif.".format(cb))
#else:
    #print("{} est négatif.".format(cb))

#while cb < 3:
    #print("cc c'est moi {}".format(cb))
    #cb+=1

#for i in [1,2,3,4,5]:
    #if i == 2:
        #print("Stop i = {}".format(i))
        #break
    
################################################################

# Intercation avec un utilisateur
#import random
#r = random.randrange(0,6)

#ru = input("Entrez un nombre compris entre 1 et 5 : ")

#while int(ru) != r:
    #if int(ru) > r:
        #print("Le nombre cherché est plus petit")
        #ru = input("Entrez un nombre compris entre 1 et 5 : ")
    #elif int(ru) < r:
        #print("Le nombre cherché est plus grand")
        #ru = input("Entrez un nombre compris entre 1 et 5 : ")
    #else:
        #print("Vous avez trouvé")


################################################################

# exception
d, dd = 0, 3

try:
    print(dd/d)
except TypeError:
    print("utilisons des chiffres.")
except ZeroDivisionError:
    print("division par zéro impossible.")
finally:
    print(d/dd)

################################################################

# simple class
class Voiture:
    def __init__(self):
        self.couleur = "Yellow"

    def get_color(self):
        return self.couleur

    def set_color(self, col):
        self.couleur = col

# heritage surcharge polymorphisme
class Vehicule(Voiture):
    def __init__(self):
        self.couleur = ""
    
    def get_color(self):
        return self.couleur

    def set_color(self, col):
        #self.couleur = col
        Voiture.set_color(self, col)


v2 = Vehicule()
v2.set_color("blue")

print(v2.get_color())

#apercu des méthodes de la classe
#print(dir(v1))

################################################################

# décorateur
#user = "Kaka"

def con(fonction):

    def traitement(*cpt, **mdp):
        print("Login ou Mot de passe invalide.")
        fonction(*cpt, **mdp)
        print("Compte bloqué.")

    #if user != "mdp":
        #return traitement

    return fonction


@con
def dothis(v):
    print("Welcome %s" %v)


dothis("Geo3X")

################################################################

# expression régulière
import re
#regex = re.findall("([0-9]+)", "Bonjour 111 Aurevoir 222")
#print(regex)

email = "cc@yahoo.com"
regex = r"(^[a-z0-9._-]+@[a-z0-9._-]+\.[(com|fr)]+)"

if re.match(regex, email) is not None:
    print("Good mail.")
else:
    print("Bad mail.")

#print(re.search(regex, email).groups())

################################################################

# lire et editer un fichier
def ecrirefile(path, texte):
    fichier = open(path, "w")
    fichier.writelines(texte)
    fichier.close()

def lirefile(path):
    fichier = open(path, "r")
    lines = fichier.readlines()
    fichier.close()
    return print(lines)

#ecrirefile("coucou.txt", "Coucou c'est moi.")
#lirefile("coucou.txt")

################################################################

# package
#from utils.fonct import *

#print(give_name())

################################################################

# débugueur déboggueur debugger
#import ipdb

################################################################

# gestion de fichier
#import os

#help(os.path)

#print(os.listdir("/"))

################################################################

# interface graphique
from tkinter import *

fen = Tk()

label = Label(fen, text = "Nom", bg = "white").pack()
txt = Entry(fen, text = "", width = 30).pack()
chkb = Checkbutton(fen, text = "Activer").pack()
rb = Radiobutton(fen, text = "Avec").pack()
lstb = Listbox(fen)
lstb.insert(1, "Python")
lstb.insert(2, "Django")
lstb.pack()
btn = Button(fen, text = "Close", COMMAND = fen.quit()).pack()

#fen.mainloop()

################################################################

# création d'un executable

##-> pip installer Pyinstaller
#->pyinstaller -F filename.py

################################################################

# send mail
#import smtplib
#from email.mime.multipart import multipart
#from email.mime.text import text

#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText

#msg = MIMEMultipart()
#msg['From'] = 'XXX@gmail.com'
#msg['To'] = 'YYY@gmail.com'
#msg['Subject'] = 'Le sujet de mon mail' 
#message = 'Bonjour !'
#msg.attach(MIMEText(message))
#mailserver = smtplib.SMTP('smtp.gmail.com', 587)
#mailserver.ehlo()
#mailserver.starttls()
#mailserver.ehlo()
#mailserver.login('XXX@gmail.com', 'PASSWORD')
#mailserver.sendmail('XXX@gmail.com', 'XXX@gmail.com', msg.as_string())
#mailserver.quit()

################################################################

# base de données https://www.simplifiedpython.net/python-mysql-tutorial/#What_is_PyMySQL
import pymysql

def Baseconnection():
    con, h, u, p, _db = "", "localhost", "Franck-Lionel", "Franck-Lionel007", "appgestcom"

    try:
        con = pymysql.connect(host = h, user = u, password = p, db = _db)
    except Exception as e:
        print("Connection impossible à la base de données: {}".format(e))

    return con

try:
    with Baseconnection().cursor() as c:
        sql = "SELECT * FROM products" # sql = "SELECT * FROM products WHERE id=?"
        c.execute(sql) # c.execute(sql, 1)
        json, data, result = {}, [], c.fetchall()

        if len(result) > 0:
            for r in result:
                data.append({"id":r[0], "name":r[1], "Description":r[2], "Price":r[3], "Created":r[4].strftime('%Y/%m/%d %H:%M:%S'), "Modified":r[5].strftime('%Y/%m/%d %H:%M:%S')})

        json["record"] = data
        print(json)

    Baseconnection().commit()
except:
    print("Error")
    Baseconnection().rollback()
finally:
    Baseconnection().close()

################################################################

