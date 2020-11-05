import pygame as pg
import random
from Class import *

largeur, hauteur = 1300, 650
fenetre=pg.display.set_mode((largeur,hauteur))
font_1 = pg.font.Font("ecriture/STJEDISE.TTF",100)



images = {}
images['fond_0']= pg.image.load("image/bg/fond_0.jpg").convert()
images['fond_1'] = pg.image.load("image/bg/fond_1.jpg").convert()
images['vaisseau1'] = pg.image.load("image/perso/perso_1.png").convert_alpha()
images['vaisseau2'] = pg.image.load("image/perso/perso_2.png").convert_alpha()
images['vaisseau3'] = pg.image.load("image/perso/perso_3.png").convert_alpha()
images['vaisseau4'] = pg.image.load("image/perso/perso_4.png").convert_alpha()
images['vaisseau5'] = pg.image.load("image/perso/perso_5.png").convert_alpha()
images['astéroide'] = pg.image.load("image/ennemies/astéroide.png").convert_alpha()
#images['tribase1_nor'] = pg.image.load("image/ennemies/tribase1_nor.png").convert_alpha()
#images['tribase1_chr'] = pg.image.load("image/ennemies/tribase1_chr.png").convert_alpha()
#images['tribase2_nor'] = pg.image.load("image/ennemies/tribase2_nor.png").convert_alpha()
#images['tribase2_chr'] = pg.image.load("image/ennemies/tribase2_chr.png").convert_alpha()
#images['tribase3_nor'] = pg.image.load("image/ennemies/tribase3_nor.png").convert_alpha()
#images['tribase3_chr'] = pg.image.load("image/ennemies/tribase3_chr.png").convert_alpha()
images['flame'] = []
for i in range(4):
	images['flame'].append(pg.image.load('image/tirs/flameBall_'+str(i)+'.png').convert_alpha())


ecriture ={}
ecriture['play'] = font_1.render("PLAY", 1, (255,255,255))
ecriture['quit'] = font_1.render("exit", 1, (255,255,255))
ecriture['play_select'] = font_1.render("PLAY", 1, (255,0,0))
ecriture['quit_select'] = font_1.render("exit", 1, (255,0,0))

def tir(tirs, images, compteur, fps, duree):
	if compteur/fps % duree ==0:
		tirs.append(Tirs(fenetre, images['flame'], random.randint(0, largeur), random.randint(0, hauteur)))
		#L'aléatoire n'est ici que pour le test

def ajouter(hauteur, largeur, images, ennemies):
	ennemies.append(Meteorite(fenetre, images["astéroide"], randint(0, largeur), randint(0, hauteur//hauteur)))