import pygame as pg, random as rd
pg.font.init()
pg.init()



class ElementGraphique:
	def __init__(self, fenetre, img, x, y): 
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x =x
		self.rect.y =y
		self.fenetre = fenetre

	def afficher(self):
		self.fenetre.blit(self.image, self.rect)



class ElementAnime(ElementGraphique):

	def __init__(self, fenetre, images, x=0, y=0):
		super().__init__(fenetre, images[0], x, y)
		self.images = images
		self.timer = 0 # timer pour l'animation
		self.numAnim = 0 # numéro de l'image courante

	def afficher(self):
		self.timer += 1
		if self.timer > 5:
			self.timer = 0
			self.numAnim += 1
			if self.numAnim >= len(self.images):
				self.numAnim = 0
			self.image = self.images[self.numAnim]

		super().afficher()


class DeplacementLineaire(ElementGraphique):
	"""docstring for DeplacementLineaire"""
	def __init__(self, fenetre, img, x=0, y=0):
		ElementGraphique.__init__(self, fenetre, img, x, y)
		self.dx = -3
		self.dy = 0
	
	def deplacer(self):
		self.rect.x += self.dx
		self.rect.y += self.dy

# CLASSES DU JOUEUR

class Perso(ElementGraphique):
	def __init__(self, fenetre, img, x=100, y=325):
		super().__init__(fenetre, img, x, y)
		self.vitesse = 7
		self.vie = 100
		


	def deplacer(self, touches, largeur, hauteur):
		if (touches[pg.K_UP] or touches[pg.K_w]) and self.rect.y > 0:
			self.rect.y -= self.vitesse 

		if (touches[pg.K_DOWN] or touches[pg.K_s]) and self.rect.y < hauteur - self.rect.h:
			self.rect.y += self.vitesse

	

	def collision(self, ennemie, Ennemis):
		if self.rect.colliderect(ennemie):
			if ennemie.pouvoir == "Pion":
				self.vie-=10
				ennemie.vie = 0
			if ennemie.pouvoir == "Boss":
				self.vie-=50
				ennemie.vie=0		
			

	def en_vie(self):
		if self.vie<=0:
			return "game_over" 
		return "Jeu"


class Shoot(ElementAnime):
	def __init__(self, fenetre, images, x=0, y=0, degats=0):
		super().__init__(fenetre, images, x, y)
		self.dx = 12
		self.dy = 0
		self.vie = 1
		self.degats = degats

	def deplacer(self):
		self.rect.x += self.dx
		self.rect.y += self.dy

	def collision(self, ennemie):
		if self.rect.colliderect(ennemie):
			self.vie = 0
			ennemie.retirer_vie(self)





# CLASSES DES ENNEMIS


class Ennemis(ElementGraphique):
	def __init__(self, fenetre, images, x, y, pouvoir):
		super().__init__(fenetre,images, x, y)
		self.vie = 20
		self.vitesse = 5	
		self.pouvoir = pouvoir



	def deplacer(self):
		self.rect.x -= 2
		self.rect.y -= 0




	def collision(self, t, tirs):
		if self.rect.colliderect(t):
			self.vie -= 20


	def retirer_vie(self, autre):
		self.vie-= autre.degats



class Boss(ElementAnime):
	def __init__(self, fenetre, images, x, y, pouvoir):
		super().__init__(fenetre,images, x, y)
		self.vie = 100
		self.vitesse = 2	
		self.pouvoir = pouvoir


	def deplacer(self):
		self.rect.x -= 2
		self.rect.y -= 0


	def collision(self, t, tirs):
		if self.rect.colliderect(t):
			self.vie -= 20


	def retirer_vie(self, autre):
		self.vie-= autre.degats		 
			

	

	