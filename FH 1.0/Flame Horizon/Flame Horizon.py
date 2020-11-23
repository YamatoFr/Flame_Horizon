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
i = 1
State = "Menu"
select = 1
ennemies = []
a=100
niveau = 1
score = 0



perso = Perso(fenetre, images['vaisseau1'],240, 300)
ennemis = Ennemis(fenetre, images['tribase1_nor'], largeur+20,randint(0,hauteur+20))
hunter = Hunter(fenetre, images['tribase3_chr'], largeur+20,randint(0,hauteur+20))
meteorite = Meteorite(fenetre, images['astéroide'], randint(0, largeur), randint(0, hauteur//hauteur))
fond_0 = ElementGraphique(fenetre, images['fond_0'], 0, 0)
fond_1 = ElementGraphique(fenetre, images['fond_1'], 0, 0)


tirs = []
last_tirs = 0



while State:
	horloge.tick(60)
	i += 1
	touches = pg.key.get_pressed()
	for event in pg.event.get():   
		if event.type==pg.QUIT:     
			State=False
		if touches [pg.K_ESCAPE]:
			State=False


	if State == "Menu":
		fond_0.afficher()
		

		if touches [pg.K_DOWN]:
			select += 1
		if touches [pg.K_UP]:
			select -= 1
		if select == 1 :
			if touches [pg.K_RETURN]:
				State = "Jeu"
		if select == 2 :
			if touches [pg.K_RETURN]:
				State = False
		if select == 0 :
			select = 2
		if select == 3 :
			select = 1    

		red = [255, 128, 128, 255]
		gray = [128, 128, 128, 255]
		image_play = font_1.render("Play", 1, red if select == 1 else gray)
		Image_play = ElementGraphique(fenetre,image_play,350,60)
		Image_play.afficher()

		image_Quit = font_1.render("Exit", 1, red if select == 2 else gray)
		Image_Quit = ElementGraphique(fenetre,image_Quit,350,200)
		Image_Quit.afficher()



	if State == "Jeu":
		image_score = font_2.render("score :" + str(score),1,(178,0,154))
		Image_score = ElementGraphique(fenetre, image_score,0,25)

		image_vie = font_2.render("vie :" + str(perso.vie),1, (178,0,154))
		Image_vie = ElementGraphique(fenetre, image_vie,50,0)

		
		fond_1.afficher()
		perso.afficher()
		perso.deplacer(touches, largeur, hauteur)
		
		
		if touches[pg.K_l] and i-last_tirs>30:
			tir(tirs, images, i, fps, 1, perso)
			son_tir.play()
			last_tirs = i

		if len(ennemies)<10:
			a = ajouter(i, hauteur, largeur, images, ennemies, a)

		State = perso.en_vie()

		new_en = []
		# new_tir = []
		for ennemie in ennemies:
			perso.collision(ennemie, ennemies)
			for t in tirs:
				ennemie.collision(t, tirs)
				# Cause un crash lors de la sortie de l'écran
				# if t.collision(ennemie, ennemies): 
						# new_tir.append(t)
			if ennemie.enVie(perso, ennemies, largeur, hauteur):
				new_en.append(ennemie)
			if not ennemie.enVie(perso, ennemies, largeur, hauteur):
				score+=10
					
			ennemies = new_en
			# tirs = new_tir

		deplacements(tirs, ennemies)
		affichage(tirs, ennemies)
		Image_score.afficher()
		Image_vie.afficher()
			
	pg.display.flip()
pg.quit()