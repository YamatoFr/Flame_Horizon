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
		self.vie = 20
		


	def deplacer(self, touches, largeur, hauteur):
		if (touches[pg.K_RIGHT] or touches[pg.K_d]) and self.rect.x < largeur - self.rect.w:
			self.rect.x += self.vitesse

		if (touches[pg.K_LEFT] or touches[pg.K_a]) and self.rect.x > 0:
			self.rect.x -= self.vitesse

		if (touches[pg.K_UP] or touches[pg.K_w]) and self.rect.y > 0:
			self.rect.y -= self.vitesse 

		if (touches[pg.K_DOWN] or touches[pg.K_s]) and self.rect.y < hauteur - self.rect.h:
			self.rect.y += self.vitesse
		#if touches[pg.K_C] :
	

	def collision(self, ennemie, ennemies):
		if self.rect.colliderect(ennemie):
			if ennemis.pouvoir == "Pion":
				self.vie-=10
			elif ennemis.pouvoir == "Boss":
				self.vie-=20	
			

	def en_vie(self):
		if self.vie<=0:
			return False 
		return "Jeu"


class Tirs(ElementAnime):
	def __init__(self, fenetre, images, x=0, y=0):
		super().__init__(fenetre, images, x, y)
		self.dx = 12
		self.dy = 0
		self.vie = 1

	def deplacer(self):
		self.rect.x += self.dx
		self.rect.y += self.dy

	def collision(self, ennemie, ennemies):
		if self.rect.colliderect(ennemie):
			return False
		return True


# CLASSES DES ENNEMIS


class Ennemis(ElementGraphique):
	def __init__(self, fenetre, images, x, y, pouvoir):
		super().__init__(fenetre,images, x, y)
		self.vie = 20
		self.vitesse = 5
		self.pouvoir = pouvoir
	
	def pouvoir(self):
		if pouvoir == "Pion":
			self.vie = 20
			self.vitesse = 10
		if pouvoir == "Boss":
			self.vie = 200
			self.vitesse = 5	


	def deplacer(self):
		self.rect.x -= 2
		self.rect.y -= 0

	def collision(self, t, tirs):
		if self.rect.colliderect(t):
			self.vie -= 20
			
	
	def enVie(self, perso, ennemies, largeur, hauteur):
		if self.vie <= 0 or self.rect.x < 0-self.rect.w or self.rect.colliderect(perso):
			return False
		return True

	