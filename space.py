import pygame # necessaire pour charger les images et les sons
import random
import math


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 5
        self.score = 0
        self.attack = 10

    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
           self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score = self.score + 1
        

class Balle() :
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        self.vitesse = 5
    
    def bouger(self):
        if self.etat == "chargee":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        
        if self.hauteur < 0:
            self.etat = "chargee"
        
        
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            ennemie.dammage(self.Joueur.attack)
            self.etat = "chargee"
            return True
  
class Ennemi():
    NbEnnemis = 6
    
    def __init__(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
            self.health = 100
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2
            self.health = 50
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
    
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 3
            self.health = 100
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2
            self.health = 50
            
    def dammage(self, amount):
        #infliger les degats
        self.health -= amount
        
        #vérifier si ses PV sont inférieur à 0
        if self.health <= 0:
            ennemi.disparaitre()
            
            
    def update_health_bar(self, surface):
        #definir une couleur pour notre jauge de PV
        bar_color = (111, 210, 46)
        
        #définir une couleur pour l'arrière plan de la jauge (gris)
        back_bar_color = (60, 63, 60)
        
        #définir la position de l'arrière plan de notre jauge de PV
        back_bar_position = [self.depart, self.hauteur, self.max_health, 5]
        
        #définir la position de notre jauge de PV ainsi que sa largeur et son épaisseur
        bar_position = [self.depart, self.hauteur, self.health, 5]
        
        #dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        
        