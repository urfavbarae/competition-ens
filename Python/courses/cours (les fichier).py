# les fichier
#pour ouvrir un fichier:
#fonction open ( chemin , mode_d'ouverture ) the full list of paramrtre open(file,mode="r",buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)
#les modes d'ouverture:
#r=> pour lecture seulement, la fichier doit etre exicte
#w=> pour ecriture seulement, si le fichier n'existe pas il sera cree, si le fichier contient deja des donnes il sera suprimer
#a=> pour ecriture seulement, si le fichier n'existe pas il sera cree, si le fichier contient deja des donnes il sera ajouter
#r+=> pour lecture et ecriture
#w+=> pour lecture et ecriture
#a+=> pour lecture et ecriture
#rb / wb /r+b /w+b /a+b => pour lecture binaire et ecriture binaire
f=open(".\\courses\\files\\file2.txt","r")

##############################################################

#pour lire un fichier:
#methode file.read(): retourn le contenu d'un fichier sous forme d'une chaine de caractere
###print(f.read())
#methode : file.readlines(): retourn la liste des lignes d'un fichier sous forme de liste
###print(f.readlines())
#methode : file.readline():retourn la premiere ligne d'un fichier
###print(f.readline())

###############################################################
#methode f.seek() : permet de changer la position du curseur dans le fichier

#methode f.tell() : permet de connaitre la position du curseur dans le fichier

import os

#methode os.path.exists(chemin) : permet de connaitre si un fichier existe ou pas
if os.path.exists(".\\courses\\files\\file2.txt"):
    print("le fichier existe")
else:
    print("le fichier n'existe pas")

#methode os.path.getsize(chemin) : permet de connaitre la taille d'un fichier
print(os.path.getsize(".\\courses\\files\\file2.txt"))

##################################################################

#methode d'ecriture:
fi=open(".\\courses\\files\\file1.txt","a")
#methode file.write(string) : permet d'ecritre dans un fichier
for i in range(5):
    name=input("saisir votre nom:")
    fi.write(f"your name is {name}\n")

#methode file.wrtelines(iterable) : permet d'ecritre dans un fichier same as file.write saaaaaaaaaaaaaaaaaaaaaaaaaaaaaame

#there is an other methode to write in file
with open(".\\courses\\files\\file1.txt","a") as fi: #the file close automatically
    fi.writelines(["your name is bachir\n","your name is said\n","your name is rashid\n","your name is hamid\n"])

#methode .rstrip() / .lstrip() / .strip() : permet de supprimer les espaces d'une chaine de caract


f.close()
fi.close()















