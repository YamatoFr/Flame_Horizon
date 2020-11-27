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
a=100
niveau = 1
score = 0
last_tirs = 0
ennemies = []
tirs = []
l_bonus = []

perso = Perso(fenetre, images['vaisseau1'],0,247)
ennemis = Ennemis(fenetre, images['tribase1_nor'], largeur+20,randint(0,hauteur+20), "pouvoir")
fond_0 = ElementGraphique(fenetre, images['fond_0'], 0, 0)
fond_1 = ElementGraphique(fenetre, images['fond_1'], 0, 0)


def suppTrucs(liste, largeur, hauteur):
	newliste = []
	for element in liste:
		if element.vie > 0 and element.rect.colliderect(fenetre.get_rect()):
			newliste.append(element)
	score = len(liste)-len(newliste)
	return newliste,score






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

		red = [211, 4, 4 ]
		white = [255,255,255]
		image_titre = font_1.render("Flame Horizon", 1,white)
		Image_titre = ElementGraphique(fenetre,image_titre,200,50)
		Image_titre.afficher()

		image_play = font_1.render("Play", 1, red if select == 1 else white)
		Image_play = ElementGraphique(fenetre,image_play,500,300)
		Image_play.afficher()

		image_Quit = font_1.render("Exit", 1, red if select == 2 else white)
		Image_Quit = ElementGraphique(fenetre,image_Quit,530,400)
		Image_Quit.afficher()
		



	if State == "Jeu":
		image_score = font_2.render("score :" + str(score),1,(178,0,154))
		Image_score = ElementGraphique(fenetre, image_score,0,25)

		image_vie = font_2.render("vie :" + str(perso.vie),1, (178,0,154))
		Image_vie = ElementGraphique(fenetre, image_vie,50,0)

		fond_1.afficher()
		perso.afficher()
		perso.deplacer(touches, largeur, hauteur)
		State = perso.en_vie()
		

		if touches[pg.K_l] and i-last_tirs>30:
			tir(tirs, images,fenetre, perso)
			son_tir.play()
			last_tirs = i

		if i%100==0:
			ajouter_ennemis(ennemies,images,largeur, hauteur, fenetre)
		
		if i%200 == 0:
			ajouter_bonus(l_bonus, images,largeur, hauteur, fenetre)


		for ennemie in ennemies:
			perso.collision(ennemie, Ennemis)
			for t in tirs:
				t.collision(ennemie)

		for bonus in l_bonus:
			bonus.collisionn(perso)
			print(bonus.vie)		
	

		tirs,s = suppTrucs(tirs, largeur, hauteur)
		ennemies,z = suppTrucs(ennemies, largeur, hauteur)
		bonus, j = suppTrucs(l_bonus, largeur, hauteur)
		score+=s

		

		deplacements(tirs, ennemies, l_bonus)
		affichage(tirs, ennemies, l_bonus)
		Image_score.afficher()
		Image_vie.afficher()	
		



	if State == "game_over":
		fond_1.afficher()
		image_resultat = font_2.render("votre score est :" + str(score),1,(178,0,154))
		Image_resultat = ElementGraphique(fenetre, image_resultat,0,200)		
		Image_resultat.afficher()
		if touches [pg.K_ESCAPE]:
			State = "Menu"

			
		
			
	pg.display.flip()
pg.quit()