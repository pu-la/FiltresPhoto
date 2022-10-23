# IMPORTS

from PIL import Image
# On a besoin du Bibliotheque "Image" de Pillow (pip3 install Pillow)
import math
# On en aura probablement besoin

# VARS

# FONCTIONS

def filtre_float(in_image, coeff_liste):
    """Donne une image et des coefficients pour les couleurs sous forme de liste (Tout) - supporte FLOAT pour des coeffs"""
    image = Image.open(in_image).copy() # Plus facile pour travailler dessus
    for y in range(image.height):       # Balailler l'y de l'image 
        for x in range(image.width):    # Balailler le x de l'image
            image.putpixel((x, y),(int(round(image.getpixel((x, y))[0]*coeff_liste[0], 0)), int(round(image.getpixel((x, y))[1]*coeff_liste[1], 0)), int(round(image.getpixel((x, y))[2]*coeff_liste[2], 0))))    # Magique.
    return image

def filtre(in_image, coeff_liste):
    """Donne une image et des coefficients pour les couleurs sous forme de liste (Que des entires!) - ne supporte PAS les floats."""
    image = Image.open(in_image).copy() # Plus facile pour travailler dessus
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
#PROGRAMME