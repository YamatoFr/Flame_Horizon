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

	def afficher():
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


class Perso(ElementGraphique):
	def __init__(self, fenetre, img, x=100, y=325):
		super().__init__(fenetre, img, x, y)
		self.vitesse = 7
		self.vie = 50


	def deplacer(self, touches, largeur, hauteur):
		if (touches[pg.K_RIGHT] or touches[pg.K_d]) and self.rect.x < largeur - self.rect.w:
			self.rect.x += self.vitesse

		if (touches[pg.K_LEFT] or touches[pg.K_a]) and self.rect.x > 0:
			self.rect.x -= self.vitesse

		if (touches[pg.K_UP] or touches[pg.K_w]) and self.rect.y > 0:
			self.rect.y -= self.vitesse 

		if (touches[pg.K_DOWN] or touches[pg.K_s]) and self.rect.y < hauteur - self.rect.h:
			self.rect.y += self.vitesse

class Ennemis(ElementAnime):
	"""docstring for Ennemis"""
	def __init__(self, fenetre, img, x, y):
		super().__init__(fenetre, images, x, y)
		self.vie = 20
		self.vitesse = 5
		
class Meteorite(ElementAnime):
	def __init__(self, fenetre, img, x , y):
		super().__init__(fenetre, img, x, y)
		self.damage = 10
		self.vy = 7

	def move(self, largeur, hauteur,ennemies):
		self.rect.y += self.vy

								