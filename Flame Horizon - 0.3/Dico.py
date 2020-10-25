import pygame as pg, random as rd
pg.font.init()
pg.init()

largeur, hauteur = 1300, 650
fenetre=pg.display.set_mode((largeur,hauteur))
font_1 = pg.font.Font("STJEDISE.ttf",100) 


images = {
    'fond1' : pg.image.load("image/bg/fond1.jpg").convert(),
    'fond2': pg.image.load("image/bg/fond_2.jpg").convert(),
    'vaisseau1' : pg.image.load("image/perso/perso_1.png").convert_alpha(),
    'vaisseau2' : pg.image.load("image/perso/perso_2.png").convert_alpha(),
    'vaisseau3' : pg.image.load("image/perso/perso_3.png").convert_alpha(),
    'vaisseau4' : pg.image.load("image/perso/perso_4.png").convert_alpha(),
    'vaisseau5' : pg.image.load("image/perso/perso_5.png").convert_alpha(),
    'ennemie1' : pg.image.load("image/ennemies/astéroide.png").convert_alpha() 
}


ecriture ={
	'play' : font_1.render("PLAY",1, (255,255,255)),
	'quit' : font_1.render("exit",1, (255,255,255)),
	'play_select' : font_1.render("PLAY",1, (255,0,0)),
	'quit_select' : font_1.render("exit",1, (255,0,0))
}

