import pygame as pg, random as rd
pg.font.init()
pg.init()


class ElementGraphique:
	def __init__(self, img, x, y): 
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x, self.rect.y = x, y


	def afficher(self, fenetre):
		fenetre.blit(self.image, self.rect)



class PERSO(ElementGraphique):
	def __init__(self, img, x=100, y=325):
		super(PERSO, self).__init__(img, x, y)
		self.vitesse = 7


	def déplacer(self, touches, largeur, hauteur):
		if (touches[pg.K_RIGHT]) and self.rect.x<largeur - 900:
			self.rect.x += self.vitesse

		if (touches[pg.K_LEFT]) and self.rect.x>0:
			self.rect.x -= self.vitesse

		if (touches[pg.K_UP]) and self.rect.y>0:
			self.rect.y -= self.vitesse 

		if (touches[pg.K_DOWN]) and self.rect.y<hauteur - self.rect.h:
			self.rect.y += self.vitesse