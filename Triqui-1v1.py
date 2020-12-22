import pygame,sys
from pygame.locals import *
from random import randint
from collections import *


#usar siempre antes de usar cualquier modulo
pygame.init()
jugar = True
#creacion de ventana________________________________

window= pygame.display.set_mode ((495,500))
#mensaje sobre la ventana
pygame.display.set_caption("3 en raya")
#________________________________________________

#gargar una imagenes:

tablero =pygame.image.load("tablero.png")
x =pygame.image.load("x.png")
o =pygame.image.load("o.png")

#pintar tablero de forma estatica
window.blit(tablero,[0,0])


## DEFINICION DE  GLOBALES------------------------------------------------------
j_uno= 0 ## saber cuantas va ganando el jugador uno 
j_dos= 0 ## saber cuantas va ganando el jugador dos

fuente = pygame.font.Font( None , 30 ) ##imprimer texto en pantalla
turno_uno = fuente.render ("TURNO JUGADOR", 0 ,(255,255,255))
turno_dos = fuente.render ("TURNO MAQUINA", 0 ,(255,255,255))

gano_uno = fuente.render ("-- JUGADOR  UNO GANO LA PARTIDA --", 4 ,(0,100,100))
gano_dos = fuente.render ( "-- JUGADOR DOS GANO LA PARTIDA --", 4 ,(255,255,255))
empate =    fuente.render ( "--                EMPATADOS                --", 5 ,(0,0,0))

#para disminuir la velocidad de ejecucion cuando alguien gane
reloj = pygame.time.Clock()

## estas son las posiciones de las imagenes en el plano coordenado de pixeles
### los indices indicaran la posicion en el tablero del triqui
posiciones_imagenes = [  (40,40),(185,40),(325,40),(40,170),(185,170), (325,170),(40,300),(185,300),(325,300)]
area_imagenes = [ (165,165),(310,165),(450,165),(165,280),(310,280),(450,280),(165,410),(310,410),(450,410)]
##------------------------------------------------------------------------------------------

def Ganador (ocupado,jugador):
       
    i = 0
    #para disminuir la velocidad de ejecucion
    
   
    while i < 9 : ## validamos las 3 horizontales
        if ocupado[i] == jugador and ocupado[i+1] == jugador and ocupado[i+2] == jugador:

            if jugador==1:  ## sumele al jugador que gano en el puntaje
                   window.blit(gano_uno,(55,450))
                   return True                  
            else:                    
                    window.blit(gano_dos,(55,450))
                    return True                     
        i+=3

    i=0
    ## validar verticales 
    while i < 3 : ## validamos las 3 horizontales
        if ocupado[i] == jugador and ocupado[i+3] == jugador and ocupado[i+6] == jugador:

            if jugador==1:  ## sumele al jugador que gano en el puntaje
                   window.blit(gano_uno,(55,450))
                   return True                   
            else:                    
                    window.blit(gano_dos,(55,450))
                    return True                     
        i+=1

    ## Validamos las 2 diagonales
    if ocupado[0] == jugador and ocupado[4] == jugador and ocupado[8] == jugador:

            if jugador==1:  ## sumele al jugador que gano en el puntaje
                   window.blit(gano_uno,(55,450))
                   return True                   
            else:                    
                    window.blit(gano_dos,(55,450))
                    return True
    if ocupado[2] == jugador and ocupado[4] == jugador and ocupado[6] == jugador:

            if jugador==1:  ## sumele al jugador que gano en el puntaje
                   window.blit(gano_uno,(55,450))
                   return True                   
            else:                    
                    window.blit(gano_dos,(55,450))
                    return True         
    return False



############################################################################



def Funcion_Juego (jugar,ocupado):         
        
        turno = True ## cuando el turno es true, significa que le daremos nosotros con la X
        ocupado = [0,0,0,0,0,0,0,0,0] ##lista que indicara que lugar esta ocupado
        
        ## bucle principal que ejecuta el juego
        while jugar :

           
            ## for de eventos
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if evento.type == MOUSEBUTTONDOWN:
                     pos = pygame.mouse.get_pos()

                     i = 0

                     while i < 9 : ## recorremos las 9 casillas del tablero para saber donde pintar, es una busqueda de donde ocurrio el click.
                         
                         ##si el clik es ta en el rango o area de la imagen, pinte
                         if pos[0] > posiciones_imagenes[i][0] and pos[1] > posiciones_imagenes[i][1]:

                             if pos[0] < area_imagenes[i][0] and pos[1] < area_imagenes[i][1] :
           
                                 if ocupado[i] == 0 : ##condicion que valida si se puede dar en ese lugar
                                     if turno : ## condicion que cambia el turno
                                         
                                            window.blit(x,posiciones_imagenes[i]) # pinta la imagen X en la pocision
                                            ##window.blit(turno_uno,(55,450)) ## pintar texto
                                            
                                            turno = False
                                            
                                            ocupado[i] = 1 # en caso de estar vacio, le asignamos 1 que esta lleno con X

                                            ## en cada turno comprobamos si alguno gano lugo del 5 turno                                            
                                            ## 3 son el minimo numero de movimientos para ganar 
                                            if ocupado.count(1)>=3: ## fi 1 aparese mas o igual de 5 veses, vaya y compruebe si gano
                                                
                                                if Ganador (ocupado,1) :
                                                    jugar = False
                                                    
                                                    ##Funcion_Juego (True,[0,0,0,0,0,0,0,0,0])
                                                
                                     else:
                                            window.blit(o,posiciones_imagenes[i]) # pinta la imagen O en la pocision
                                            turno = True
                                            ##window.blit(turno_dos,(55,450)) ## pintar texto
                                            
                                            ocupado[i] = 2 # en caso de estar vacio, le asignamos 2  que esta lleno con
                                            
                                            ## en cada turno comprobamos si alguno gano lugo del 5 turno
                                            ## 3 son el minimo numero de movimientos para ganar 
                                            if ocupado.count(2) >=3: ## fi 2 aparese mas de 5 veses, vaya y compruebe si gano
                                                
                                                if Ganador (ocupado,2):
                                                    jugar = False
                                                    
                                                    ##Funcion_Juego (True,[0,0,0,0,0,0,0,0,0])
                         i += 1

                         ## si el tablero esta lleno, Termine
                         if ocupado.count(0) == 0 and  ( (not (Ganador (ocupado,2)) and (not (Ganador (ocupado,1))))):
                             window.blit(empate,(55,450))
                             juego=False
                             
            pygame.display.update()


Funcion_Juego (True,[0,0,0,0,0,0,0,0,0])





    
