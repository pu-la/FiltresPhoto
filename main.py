# IMPORTS

from PIL import Image
# On a besoin du Bibliotheque "Image" de Pillow (pip3 install Pillow)
import math
from tkinter import filedialog as fd
# On en aura probablement besoin
###
# VARS (init)

# FONCTIONS

def filtre_float(in_image, coeff_liste):
    """Donne une image et des coefficients pour les couleurs sous forme de liste (Tout) - supporte FLOAT pour des coeffs"""
    image = in_image # Plus facile pour travailler dessus
    for y in range(image.height):       # Balailler l'y de l'image 
        for x in range(image.width):    # Balailler le x de l'image
            image.putpixel((x, y),(int(round(image.getpixel((x, y))[0]*coeff_liste[0], 0)), int(round(image.getpixel((x, y))[1]*coeff_liste[1], 0)), int(round(image.getpixel((x, y))[2]*coeff_liste[2], 0))))    # Magique.
    return image

def filtre(in_image, coeff_liste):
    """Donne une image et des coefficients pour les couleurs sous forme de liste (Que des entires!) - ne supporte PAS les floats."""
    image = in_image # Plus facile pour travailler dessus
    for y in range(image.height):       # Balailler l'y de l'image 
        for x in range(image.width):    # Balailler le x de l'image
            image.putpixel((x, y),(image.getpixel((x, y))[0]*coeff_liste[0], image.getpixel((x, y))[1]*coeff_liste[1], image.getpixel((x, y))[2]*coeff_liste[2]))    # Magique.
    return image
    
def filtre_r(in_image):
    '''Filtre Rouge, passe une image'''
    return filtre(in_image, [1,0,0])
def filtre_g(in_image):
    '''Filtre Vert, passe une image'''
    return filtre(in_image, [0,1,0])
def filtre_b(in_image):
    '''Filtre Bleu, passe une image'''
    return filtre(in_image, [0,0,1])
def rienk_filtre_gris(in_image):
    """transforme une image couleur en nuance de gris, passe une image"""
    image = in_image # Plus facile pour travailler dessus
    for y in range(image.height):       # Balailler l'y de l'image 
        for x in range(image.width):    # Balailler le x de l'image
            moyenne = int(round((image.getpixel((x, y))[0]+image.getpixel((x, y))[1]+image.getpixel((x, y))[2])/3, 0))
            image.putpixel((x, y), (moyenne, moyenne, moyenne))    # Magique.
    return image

###<Tawana>

def filtre_bleu_vert(image):
    'Cet filtre est bas?? sur le fonctionnement du filtre rouge'
    #Identification du fonction
    rgb_image = image.convert("RGB")
    #Convertit "maison" en 3 coueurs: red, green, blue
    for i in range(image.width):
    #Balaye la largeur de "maison"
        for j in range(image.height):
    #Balaye la longueur de "maison"
            r, g, b = rgb_image.getpixel((i, j))
    #Retourne la couleur du pixel (i, j) de image.
            image.putpixel((i,j),(0, g, b))
    #Modifie la couleur du pixel (i, j) de image en (r, g, b).
    return image

def filtre_gris(image):
#identification du fonction
    rgb_image = image.convert("RGB")
#convertit "maison" en 3 coueurs: red, green, blue
    for i in range(image.width):
#balaye la largeur de "maison"
        for j in range(image.height):
#balaye la longueur de "maison"
            r, g, b = rgb_image.getpixel((i, j))
#Retourne la couleur du pixel (i, j) de image.
            moy = (r+g+b)/3
#Calcul de la moyenne 
            moyenne = int(moy)
#Transforme moy en un nombre entier
            image.putpixel((i, j),(moyenne, moyenne, moyenne))
#r, g et b prend la valeur de moyenne
#Modifie la couleur du pixel (i, j) de image en (r, g, b).
    return image


def temp_filtre_noir_blanc(image):
    'Ce filtre suit le filtre gris'
#Identification du fonction
    facteur = 128
    rgb_image = filtre_gris(image)
#Convertit "maison" en nuance de gris
#Enregistre le variable sur lequel va etre ex??cuter le fonction.
    for i in range(image.width):
#Balaye la largeur de "maison"
        for j in range(image.height):
#Balaye la longueur de "maison"
            r = rgb_image.getpixel((i, j))[0] # Couleur rouge - indice 0
#Retourne la couleur du pixel (i, j) de image.
#Nous avons seulement besoin d'un couleur car la fa??on dont le filtre de nuance de gris fonctionne, fait que tous les couleurs vaut le mem??e.
            if r<facteur:
                image.putpixel((i, j),(0, 0, 0))
            else:
                image.putpixel((i, j),(255, 255, 255))
    return image

def filtre_rouge(image):
#Identification du fonction
    rgb_image = image.convert("RGB")
#Convertit "maison" en 3 coueurs: red, green, blue
    for i in range(image.width):
#Balaye la largeur de "maison"
        for j in range(image.height):
#Balaye la longueur de "maison"
            r, g, b = rgb_image.getpixel((i, j))
#Retourne la couleur du pixel (i, j) de image.
            image.putpixel((i,j),(r, 0, 0))
#Modifie la couleur du pixel (i, j) de image en (r, g, b).
    return image



###</Tawana>

def rienk_noiretblanc(in_img, fact=128):
    """Filtre Noir et blanc, attend une image et un facteur optionnel"""
    image = filtre_gris(in_img)
    for y in range(image.height):
        for x in range(image.width):
            if image.getpixel((x,y))[0]<fact:
                image.putpixel((x, y), (0, 0, 0))
            else:
                image.putpixel((x, y), (255,255, 255))
    return image

def mirroir(in_img):
    """retourne l???image comme si on la voyait dans un miroir"""
    image = in_img.copy()
    out_img = in_img
    for y in range(image.height):       # Balailler l'y de l'image 
        for x in range(image.width):
            out_img.putpixel((image.width-x-1,y), (image.getpixel((x, y))[0], image.getpixel((x, y))[1], image.getpixel((x, y))[2]))
    return out_img
def pixelation(in_img, nb):
    """faire l???effet d???une image pixelis??e, attend une image et la taille des pixels."""
    image = in_img
    for x in range(1, image.width, nb):
        for y in range(1, image.height, nb):
            pixelval=[0, 0, 0]
            for i in range(-1, nb-1):
                for ii in range(-1, nb-1):
                    pixelval[0] += image.getpixel((x+ii,y+i))[0]
                    pixelval[1] += image.getpixel((x+ii,y+i))[1]
                    pixelval[2] += image.getpixel((x+ii,y+i))[2]
            pixelval[0] = int(round(pixelval[0]/(nb*nb), 0))
            pixelval[1] = int(round(pixelval[1]/(nb*nb), 0))
            pixelval[2] = int(round(pixelval[2]/(nb*nb), 0))
            for i in range(-1, nb-1):
                for ii in range(-1, nb-1):
                    image.putpixel((x+ii,y+i),(pixelval[0],pixelval[1],pixelval[2]))
    return image



def lum(in_image, nb):
    image = in_image # Plus facile pour travailler dessus
    for y in range(image.height):       # Balailler l'y de l'image 
        for x in range(image.width):    # Balailler le x de l'image
            image.putpixel((x, y),(image.getpixel((x, y))[0]+nb, image.getpixel((x, y))[1]+nb, image.getpixel((x, y))[2]+nb))    # Magique.
    return image

def color(in_image, couleur, nb):
    """Filtre pour faire resortir une couleur de l'image. Attend une image, une des 3 couleurs (R = 0, V = 1, B = 2) et un nombre entier k"""
    image = in_image
    for x in range(image.width):
        for y in range(image.height):
            if couleur == 0:
                image.putpixel((x, y), (image.getpixel((x, y))[0]+nb, int(round(image.getpixel((x, y))[1]/2, 0)), int(round(image.getpixel((x, y))[2]/2, 0))))
            elif couleur == 1:
                image.putpixel((x, y), (int(round(image.getpixel((x, y))[0]/2, 0)), image.getpixel((x, y))[1]+nb, int(round(image.getpixel((x, y))[2]/2, 0))))
            elif couleur == 2:
                image.putpixel((x, y), (int(round(image.getpixel((x, y))[0]/2, 0)), int(round(image.getpixel((x, y))[2]/2, 0)), image.getpixel((x, y))[2]+nb))
            else:
                print("error, lire help()")
                exit()
    return image

def color512(in_image, fact=8):
    """limite ?? 8 (ou fact=...) le nombre de valeurs pour chaque composante de fa??on ?? donner un effet ?? vieux jeu vid??o ?? ?? l'image. Attend une image et optionnellement un facteur."""
    image=in_image
    fact=int(round(256/fact))
    for x in range(image.width):
        for y in range(image.height):
            image.putpixel((x, y),(int(round(image.getpixel((x, y))[0]/fact, 0))*fact,int(round(image.getpixel((x, y))[1]/fact, 0))*fact,int(round(image.getpixel((x, y))[2]/fact, 0))*fact))
    return image


image = Image.open("maison.jpeg")

#PROGRAMME
saved=False
while True:
    print("[O]uvrir\n[E]nregistrer\n[P]review\n[Q]uitter\nFiltres: \n 1. Couleurs\n 2. Couleurs (avancee)\n 3. Gris\n 4. Noir et blanc\n 5. Mirroir\n 6. Pixelation\n 7. Luminosite\n 8. Color\n 9. Color512")
    choix = input().upper()
    if choix == "O":
        saved=False
        filename = fd.askopenfilename()
        image = Image.open(filename)
    elif choix =="P":
        image.show()
    elif choix =="Q":
        if saved == False:
            if input("Quitter sans enregistrer? y/n ").lower() == "y":
                exit()
        else:
            exit()
    elif choix == "E":
        saved = True
        image.save(input("Nom du fichier: "))
    elif choix == "1":
        couleur = input("[R]ouge, [V]ert, [B]leu ou ([VB]ert et Bleu)").upper()
        if couleur == "R":
            filtre_r(image)
        elif couleur == "V":
            filtre_g(image)
        elif couleur == "B":
            filtre_b(image)
        elif couleur == "VB":
            filtre_bleu_vert(image)
        else:
            print("Error")
            pass
    elif choix == "2":
        filtre_float(image, [float(input("Combien de Rouge(multiplication): ")), float(input("Combien de Vert: ")), float(input("Combien de Bleu: "))])
    elif choix == "3":
        filtre_gris(image)
    elif choix == "4":
        try:
            rienk_noiretblanc(image, int(input("Facteur (0 a 255, par defaut 128): ")))
        except ValueError:
            rienk_noiretblanc(image, 128)
    elif choix == "5":
        mirroir(image)
    elif choix == "6":
        try:
            pixelation(image, int(input("taille des pixels: ")))
        except IndexError:
            print(f"Choisir une autre valeur, votre taille de pixel n'est pas compatible avec cette image.")
    elif choix == "7":
        lum(image, int(input("Lumiere ajoute: ")))
    elif choix == "8":
        couleur = input("[R]ouge, [V]ert ou [B]leu: ").upper()
        if couleur == "R":
            color(image,0,int(input("Rajoute au couleur: ")))
        elif couleur == "V":
            color(image,1,int(input("Rajoute au couleur: ")))
        elif couleur == "B":
            color(image,2,int(input("Rajoute au couleur: ")))
        else:
            print("Error")
            pass
    elif choix == "9":
        color512(image, int(input("Nombre de couleurs: ")))
    else:
        print("Mauvais selection!")
        pass
