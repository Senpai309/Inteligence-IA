# view.py
from tkinter import Label, StringVar
from PIL import Image, ImageTk

# Déclaration des variables globales pour l'interface
age_var = None
gender_var = None
emotion_var = None
advice_var = None
label_img = None

# Fonction pour configurer l'interface utilisateur
def setup_ui(root):
    global age_var, gender_var, emotion_var, advice_var, label_img

    # Variables pour afficher les résultats
    age_var = StringVar()
    gender_var = StringVar()
    emotion_var = StringVar()
    advice_var = StringVar()

    # Labels pour afficher les résultats
    Label(root, textvariable=age_var, font=("Helvetica", 14)).pack()
    Label(root, textvariable=gender_var, font=("Helvetica", 14)).pack()
    Label(root, textvariable=emotion_var, font=("Helvetica", 14)).pack()
    Label(root, textvariable=advice_var, font=("Helvetica", 14)).pack()

    # Label pour afficher la vidéo
    label_img = Label(root)
    label_img.pack()

# Fonction pour mettre à jour les informations affichées
def update_info(age, gender, emotion, advice):
    age_var.set(f'Âge: {age}')
    gender_var.set(f'Sexe: {gender}')
    emotion_var.set(f'Émotion: {emotion}')
    advice_var.set(f'Conseil: {advice}')

# Fonction pour afficher l'image de la vidéo dans l'interface
def display_frame(frame):
    img = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    label_img.imgtk = imgtk
    label_img.configure(image=imgtk)
