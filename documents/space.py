import pygame  # necessaire pour charger les images et les sons
import random  # necessaire pour faire apparaitre les ennemis de manière aléatoire
import math
import time

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 3
        self.score = 0
    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
           self.position = self.position - self.vitesse
           
    def tirer(self):
        self.sens = "O"
        
    def marquer(self):
        self.score += 1
        
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
            
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40):
            self.etat = "chargee"
            return True
            
class Ennemi():
    NbEnnemis = 6
    
    def __init__(self):
        self.depart= random.randint(0, 800-64)
        self.hauteur= 64
        self.type= random.randint(1, 2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 0.5
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 0.25
    
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
        if self.hauteur > 600:
            self.hauteur = 0
    
    def disparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if  (self.type == 1):
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 0.5
        elif (self.type ==2):
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 0.25
            
            
            

class Sound():
    
    def __init__(self):
        pygame.mixer.init(frequency=16000)
        self.sounds = {
            "tir": "shooting.mp3",
            "explosion": "Explosion meme - Sound Effect.mp3",
            "fond" : "À travers la galaxie.mp3"
            }
        
    def play(self, name):
        if name != "fond":
            pygame.mixer.music.load(self.sounds[name])
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)
            time.sleep(1)
            pygame.mixer.music.load(self.sounds["fond"])
        
        else:
            pygame.mixer.music.load(self.sounds[name])
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
            
            
    """def music(self, name):
        pygame.mixer.music.load(self.sounds[name])
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)"""
        
        
        
        
        
        
        
                
            
        
        
        
    
    
                
        
        
        
