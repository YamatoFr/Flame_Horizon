import pygame as pg
from Class import *
from Dico import *
pg.font.init()
pg.init()



largeur, hauteur = 1300, 650
fenetre=pg.display.set_mode((largeur,hauteur))
horloge = pg.time.Clock()
i=1
State = "Menu"
select = 1
ennemies= []
perso = PERSO(images['vaisseau1'],240, 300)




while State:
    horloge.tick(60)
    i+=1
    touches = pg.key.get_pressed()
    for event in pg.event.get():   
        if event.type==pg.QUIT:     
            State=False
        if touches [pg.K_ESCAPE]:
            State=False



    if State == "Menu":
        fenetre.blit(images['fond2'],(0,0))
        fenetre.blit(ecriture['play'],(500,140))
        fenetre.blit(ecriture['quit'],(520,350))

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
        fenetre.blit(images['fond1'],(0,0))
        perso.afficher(fenetre)
        perso.déplacer(touches, largeur, hauteur)        
        
        if len(ennemies)<8 :
            ajouter(hauteur, largeur, images, ennemies)
        for ennemie in ennemies :
            ennemie.afficher(fenetre)
            ennemie.move(largeur, hauteur,ennemies)   



    pg.display.flip()
pg.quit()