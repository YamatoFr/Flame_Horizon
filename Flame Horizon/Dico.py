import pygame as pg
import random
from random import randint
from Class import *

largeur, hauteur = 1300, 650
fenetre=pg.display.set_mode((largeur,hauteur))
font_1 = pg.font.Font("ecriture/STJEDISE.TTF",100)



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


ecriture ={}
ecriture['play'] = font_1.render("PLAY", 1, (255,255,255))
ecriture['quit'] = font_1.render("exit", 1, (255,255,255))
ecriture['play_select'] = font_1.render("PLAY", 1, (255,0,0))
ecriture['quit_select'] = font_1.render("exit", 1, (255,0,0))
ecriture['vie'] = font_1.render("vie",1, (178,0,154))

def tir(tirs, images, compteur, fps, duree, perso):
	tirs.append(Tirs(fenetre, images['flame'], perso.rect.x + perso.rect.w, perso.rect.y+10))
		
def ajouter(i,hauteur, largeur, images, ennemies, a):
	if i%a == 0:
		rdn = random.random()
		if 0 <rdn< 0.2:
			ennemies.append(Meteorite(fenetre, images["astéroide"], randint(0, largeur), randint(0, hauteur//hauteur)))
		elif 0.2 <rdn< 0.6:
			ennemies.append(Ennemis(fenetre, images["tribase1_nor"], largeur+20,randint(0,hauteur-20)))
		# elif 0.6 <rdn< 1:
			# ennemies.append(Hunter(fenetre, images["tribase3_chr"], largeur+20,randint(0,hauteur-20)))	
	return a	
	
def deplacements(tirs, ennemies):
	for t in tirs:
		t.deplacer()

	# for hunter in ennemies:
		# hunter.deplacer(hauteur, largeur, ennemies)

	for ennemie in ennemies :
		ennemie.deplacer()

def affichage(tirs, ennemies):
	for t in tirs:
		t.afficher()

	for ennemie in ennemies :
		ennemie.afficher()

	# for hunter in ennemies:
		# hunter.afficher()


# def nettoyage(tirs, ennemies):
	# new_en = []
	# new_tir = []
	# for ennemie in ennemies:
		#perso.collision(ennemie, ennemies)
		# for t in tirs:
			# ennemie.collision(t, tirs)
			# Cause un crash lors de la sortie de l'écran
			# if t.collision(ennemie, ennemies): 
					# new_tir.append(t)
		# if ennemie.enVie(perso, ennemies, largeur, hauteur):
			# new_en.append(ennemie)
		# if not ennemie.enVie(perso, ennemies, largeur, hauteur):
			# score+=10
				
		# ennemies = new_en
		# tirs = new_tir