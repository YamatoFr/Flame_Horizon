import pygame as pg
from random import randint
from Class import *

largeur, hauteur = 1300, 650
fenetre=pg.display.set_mode((largeur,hauteur))
font_1 = pg.font.Font("ecriture/STJEDISE.ttf",100)



images = {}
images['fond_0']= pg.image.load("image/bg/fond_0.jpg").convert()
images['fond_1'] = pg.image.load("image/bg/fond_1.jpg").convert()
images['vaisseau1'] = pg.image.load("image/perso/perso_1.png").convert_alpha()
images['vaisseau2'] = pg.image.load("image/perso/perso_2.png").convert_alpha()
images['vaisseau3'] = pg.image.load("image/perso/perso_3.png").convert_alpha()
images['vaisseau4'] = pg.image.load("image/perso/perso_4.png").convert_alpha()
images['vaisseau5'] = pg.image.load("image/perso/perso_5.png").convert_alpha()
images['ennemie1'] = pg.image.load("image/ennemies/astéroide.png").convert_alpha()
images['flame'] = []
for i in range(4):
	images['flame'].append(pg.image.load('image/tirs/flameBall_'+str(i)+'.png').convert_alpha())


ecriture ={}
ecriture['play'] = font_1.render("PLAY", 1, (255,255,255))
ecriture['quit'] = font_1.render("exit", 1, (255,255,255))
ecriture['play_select'] = font_1.render("PLAY", 1, (255,0,0))
ecriture['quit_select'] = font_1.render("exit", 1, (255,0,0))



def ajouter(hauteur, largeur, images, ennemies):
	ennemies.append(Meteorite(fenetre, images["ennemie1"], randint(0, largeur), randint(0, hauteur//hauteur)))