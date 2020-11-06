import pygame as pg
from Class import *
from Dico import *
import os
pg.font.init()
pg.init()


largeur, hauteur = 1300, 650
fenetre = pg.display.set_mode((largeur,hauteur))
horloge = pg.time.Clock()
fps = 30
time = 0
State = "Menu"
select = 1
ennemies = []

perso = Perso(fenetre, images['vaisseau1'],240, 300)
fond_0 = ElementGraphique(fenetre, images['fond_0'], 0, 0)
fond_1 = ElementGraphique(fenetre, images['fond_1'], 0, 0)
txt_play = ElementGraphique(fenetre, ecriture['play'], 500, 140)
txt_quit = ElementGraphique(fenetre, ecriture['quit'], 520, 350)
tirs = []

while State:
	horloge.tick(60)
	time += 1
	touches = pg.key.get_pressed()
	for event in pg.event.get():   
		if event.type==pg.QUIT:     
			State=False
		if touches [pg.K_ESCAPE]:
			State=False


	if State == "Menu":
		fond_0.afficher()
		txt_play.afficher()
		txt_quit.afficher()

		if touches [pg.K_DOWN]:
			select += 1
		if touches [pg.K_UP]:
			select -= 1
		if select == 1 :
			fenetre.blit(ecriture['play_select'],(500,140))
			if touches [pg.K_RETURN]:
				State = "Jeu"
		if select == 2 :
			fenetre.blit(ecriture['quit_select'],(520,350))
			if touches [pg.K_RETURN]:
				State = False
		if select == 0 :
			select = 2
		if select == 3 :
			select = 1    


	if State == "Jeu":
		fond_1.afficher()
		perso.afficher()
		perso.deplacer(touches, largeur, hauteur)

		tir(tirs, images, time, fps, 1)

		#for t in tirs:
		#	t.deplacer()
		#	t.afficher()
		
		if len(ennemies)<8 :
			ajouter(hauteur, largeur, images, ennemies)
		for ennemie in ennemies :
			ennemie.afficher()
			ennemie.move(largeur, hauteur, ennemies)


	pg.display.flip()
pg.quit()