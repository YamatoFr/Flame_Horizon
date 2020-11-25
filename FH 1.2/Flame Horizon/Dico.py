import pygame as pg
import random
from random import randint
from Class import *

largeur, hauteur = 1300, 650
fenetre=pg.display.set_mode((largeur,hauteur))
font_1 = pg.font.Font("ecriture/STJEDISE.TTF",100)
font_2 = pg.font.Font("ecriture/STJEDISE.TTF",30)
score = 0



images = {}
images['fond_0']= pg.image.load("image/bg/fond_0.jpg").convert()
images['fond_1'] = pg.image.load("image/bg/fond_1.jpg").convert()
images['vaisseau1'] = pg.image.load("image/perso/perso_1.png").convert_alpha()
images['astéroide'] = pg.image.load("image/ennemies/astéroide.png").convert_alpha()
images['tribase1_nor'] = pg.image.load("image/ennemies/tribase1_nor.png").convert_alpha()
images['tribase1_chr'] = pg.image.load("image/ennemies/tribase1_chr.png").convert_alpha()
images['tribase2_nor'] = pg.image.load("image/ennemies/tribase2_nor.png").convert_alpha()
images['tribase2_chr'] = pg.image.load("image/ennemies/tribase2_chr.png").convert_alpha()
images['tribase3_nor'] = pg.image.load("image/ennemies/tribase3_nor.png").convert_alpha()
images['tribase3_chr'] = pg.image.load("image/ennemies/tribase3_chr.png").convert_alpha()
images['flame'] = []
for i in range(4):
	images['flame'].append(pg.image.load('image/tirs/flameBall_'+str(i)+'.png').convert_alpha())

perso = Perso(fenetre, images['vaisseau1'],240, 300)

son_tir = pg.mixer.Sound("sons/Laser Shot.wav")


def tir(tirs, images,fenetre, perso):
	tirs.append(Shoot(fenetre, images['flame'], perso.rect.x + perso.rect.w, perso.rect.y+10, 20))



		
def ajouter(i,hauteur, largeur, images, ennemies,ennemis, a):
	if i%450 == 0:
		if a > 20: 
			a -= 20

	if i%a == 0:
		rdn = random.random()
		if 0 <rdn< 0.50:
			ennemies.append(Ennemis(fenetre, images["tribase1_nor"], largeur-20,randint(0,hauteur-20), "Pion"))
		elif 0.50 <rdn< 1:
			ennemies.append(Ennemis(fenetre, images["tribase3_chr"], largeur-20,randint(0,hauteur-20), "Boss"))	
	return a	
	
def deplacements(tirs, ennemies):
	for t in tirs:
		t.deplacer()

	
	for ennemie in ennemies :
		ennemie.deplacer()

def affichage(tirs, ennemies):
	for t in tirs:
		t.afficher()

	for ennemie in ennemies :
		ennemie.afficher()



