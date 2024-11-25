# main.py
import tkinter as tk
from controller import start_capture, release_resources

def main():
    # Initialisation de la fenêtre principale
    root = tk.Tk()
    root.title("Détection d'Âge, Sexe et Humeur")
    
    # Lancement de la capture dans le contrôleur
    start_capture(root)
    
    # Exécuter l'application
    root.mainloop()
    
    # Libérer les ressources de la caméra après la fermeture de l'interface
    release_resources()

if __name__ == "__main__":
    main()
