import pygame  # necessaire pour charger les images et les sons
import random  # necessaire pour faire apparaitre les ennemis de manière aléatoire

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 5
        self.score = 0

    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
           self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score +=1

class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        
    def bouger(self):    
        if self.etat == "chargee":
                self.depart = self.tireur.position + 16
                self.hauteur = 492
        elif self.etat == "tiree" :
                self.hauteur = self.hauteur - 5    
        if self.hauteur < 0:
            self.etat = "chargee"
            
    def toucher(self, Ennemi):
        pass
            
class Ennemi():
    NbEnnemis = 8
    def __init__(self):
        self.depart= random.randint(0, 800-64)
        self.hauteur= 64
        self.type= 0
        self.image = pygame.image.load("invader1.png")
        self.vitesse= 1
    
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
        if self.hauteur > 600:
            self.hauteur = 64
            self.hauteur = self.hauteur + self.vitesse
    
    def disparaitre(self):
        pass
        
        
        
                
            
        
        
        
    
    
                
        
        
        