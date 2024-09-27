import pygame  # necessaire pour charger les images et les sons

rapidité=1
class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens="centre"
        self.image="vaisseau.png"
        self.position=368
    
    def deplacer(self):
        if player.sens == "gauche":
            self.position -= 0,5
            if self.position < 0:
                self.position = 0
                
        if player.sens == "droite":
            self.position += rapidité
            if self.position > 772:
                self.position = 772
                
        
        
        