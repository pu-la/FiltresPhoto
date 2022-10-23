#
# IMPORTS
#
from tkinter import BOTTOM, LEFT, RIGHT, TOP, filedialog as fd
import tkinter as tk
from PIL import Image, ImageTk
# On a besoin du Bibliotheque "Image" de Pillow (pip3 install Pillow)
import math
# On en aura probablement besoin


#
# VARS
#


#
# FONCTIONS
#

def filtre_float(in_image, coeff_liste):
    """Donne une image et des coefficients pour les couleurs sous forme de liste (Tout) - supporte FLOAT pour des coeffs"""
    image = in_image
    for y in range(image.height):       # Balailler l'y de l'image 
        for x in range(image.width):    # Balailler le x de l'image
            image.putpixel((x, y),(int(round(image.getpixel((x, y))[0]*coeff_liste[0], 0)), int(round(image.getpixel((x, y))[1]*coeff_liste[1], 0)), int(round(image.getpixel((x, y))[2]*coeff_liste[2], 0))))    # Magique.
    return image

def filtre(in_image, coeff_liste):
    """Donne une image et des coefficients pour les couleurs sous forme de liste (Que des entires!) - ne supporte PAS les floats."""
    image = in_image
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





# tkinter fontions:

def select_file():
    filetypes = (
        ('Jpeg', '*.jpeg'),
        ('Jpg', '*.jpg'),
        ('Png', '*.png')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='../',
        filetypes=filetypes)
    
    return filename


# 
# PROGRAMME
#






original_image = Image.open(select_file()).copy()
current_image = original_image.copy()
root = tk.Tk()

current_image = filtre_b(current_image)

# Frames pour l'image

image_frame = tk.Frame(root)
image_frame.pack(side = LEFT)
t_image_frame = tk.Frame(image_frame)
t_image_frame.pack(side=TOP)
b_image_frame = tk.Frame(image_frame)
b_image_frame.pack(side=BOTTOM)

# Charger les photos
def load_photos():
    topimage=tk.Canvas(t_image_frame, width=700, height=350)
    topimage.pack(side=TOP)
    img=ImageTk.PhotoImage(image = original_image)
    topimage.create_image(350, 200, image=img, anchor="center")

    bottomimage=tk.Canvas(b_image_frame, width=700, height=350)
    bottomimage.pack(side=BOTTOM)
    img1=ImageTk.PhotoImage(image = current_image)
    bottomimage.create_image(350, 200, image=img1, anchor="center")

# Frames pour les modifications d'image
settings_frame = tk.Frame(root)
settings_frame.pack(side = RIGHT)

# Changements pour l'image



root.mainloop()