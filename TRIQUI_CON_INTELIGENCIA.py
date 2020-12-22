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

gano_uno = fuente.render ("-- JUGADOR  GANO LA PARTIDA --", 4 ,(0,100,100))
gano_dos = fuente.render ( "-- MAQUINA GANO LA PARTIDA --", 4 ,(255,255,255))
empate =    fuente.render ( "--                EMPATADOS                --", 5 ,(0,0,0))

#para disminuir la velocidad de ejecucion cuando alguien gane
reloj = pygame.time.Clock()

## estas son las posiciones de las imagenes en el plano coordenado de pixeles
### los indices indicaran la posicion en el tablero del triqui
posiciones_imagenes = [  (40,40),(185,40),(325,40),(40,170),(185,170), (325,170),(40,300),(185,300),(325,300)]
area_imagenes = [ (165,165),(310,165),(450,165),(165,280),(310,280),(450,280),(165,410),(310,410),(450,410)]
##------------------------------------------------------------------------------------------

def primero_IA():
   return randint (0,8)

def segundo_IA(ocupado):
   
   ceros =[]
   copia_ocupado = ocupado.copy()
   
   i=0
   while i < 9 : ##recorra la lista ocupado------------------------------------------------------------------------------------------------

      if copia_ocupado[i]== 0:
         ceros.append(i)
      i+=1
      
   i=0
   
   while i < 6 : ## recorrer matriz de ceros para mirar si pierde en alguna posicion ----------------------------------------------------
      movimiento = ceros[i]
     
      copia_ocupado[movimiento] = 1
      
      if  Ganador (copia_ocupado,1,False): ## si donde va a poner va a ganar, retorne la posicion        
         
        
         return movimiento
      else: copia_ocupado[movimiento] = 0
      i += 1

   ## si el rival no gana en ninguna posicion, hacemos un movimiento aleatorio   
   movimiento_maquina =  randint (0,5)
   while copia_ocupado[ceros[movimiento_maquina]] == 0 :
           if ocupado[movimiento_maquina] == 0:
              return movimiento_maquina                                                      
           else:
             movimiento_maquina =   randint (0,5)
   

def tercero_IA(ocupado): #tercer movimiento de la IA --------------------------------------------------------------------------------------------------------------------------------------------------

   ceros =[]
   copia_ocupado = ocupado.copy()

   i=0
   while i < 9 : ##recorra la lista ocupado------------------------------------------------------------------------------------------------

      if copia_ocupado[i]== 0:
         ceros.append(i)
      i+=1
   i=0
   while i < 4 : ## recorrer matriz de ceros para mirar si gana en alguna posicion ----------------------------------------------------
      movimiento = ceros[i]
      copia_ocupado[movimiento] = 2
      
      if  Ganador (copia_ocupado,2,True): ## si donde va a poner va a ganar, retorne la posicion
         
         
         return movimiento
      else: copia_ocupado[movimiento] = 0
      i += 1
   
   i=0
   while i < 4 : ## recorrer matriz de ceros para mirar si gana en alguna posicion el rival ----------------------------------------------------
      movimiento = ceros[i]
      copia_ocupado[movimiento] = 1      
      if  Ganador (copia_ocupado,1,False): ## si donde va a poner va a ganar, retorne la posicion         
          return movimiento
      else: copia_ocupado[movimiento] = 0
      i += 1
      
   ## si el rival no gana en ninguna posicion, hacemos un movimiento aleatorio   
   movimiento_maquina =  randint (0,3)
   while copia_ocupado[ceros[movimiento_maquina]] == 0 :
           if ocupado[movimiento_maquina] == 0:
              return movimiento_maquina                                                      
           else:
             movimiento_maquina =   randint (0,3)

def ultimo_IA (ocupado):
   
   copia_ocupado = ocupado.copy()
   movimiento = randint (0,8)
   if copia_ocupado[movimiento] ==0:

      copia_ocupado[movimiento]= 2
      if  Ganador (copia_ocupado,2,False): ## si donde va a poner va a ganar, retorne la posicion        
        
         return movimiento
      else: ## de lo contrario, retorne la otra posicion disponible
         
         copia_ocupado[movimiento]= 1
         if  Ganador (copia_ocupado,1,False): ## si donde va a poner va a ganar el contrario, pues ponga ahi para no dejarlo ganar
         
            return movimiento
         
         else: ## de lo contrario, retorne la otra posicion disponible        
                 return copia_ocupado.index(0) 
         
   return  ultimo_IA (ocupado) ##llamado recursivo para que vuelva a generar aleatorio y todo

   ## No dejar ganar al Rival--------------------------------------------------------------------------------------------------------------
   i=0
   while i < 4 : ## recorrer matriz de ceros para mirar si gana el rival en alguna posicion
      movimiento = ceros[i]
      copia_ocupado[movimiento] = 1
      
      if  Ganador (copia_ocupado,1,False): ## si donde va a poner va a ganar, retorne la posicion
         
         window.blit(o,posiciones_imagenes[movimiento]) # pinta la imagen O en la pocision
         return movimiento
      else: copia_ocupado[movimiento] = 0
      i += 1
   
   ## si no gana en ninguna casilla disponible, le da en cualquiera aleatoriamente  -----------------------------------------------------  
   movimiento = ceros[randint (0,3)]
   window.blit(o,posiciones_imagenes[movimiento]) # pinta la imagen O en la pocision
   return movimiento






def Ganador (ocupado,jugador,imprimir):
       
    i = 0
    #para disminuir la velocidad de ejecucion
    
   
    while i < 9 : ## validamos las 3 horizontales
        if ocupado[i] == jugador and ocupado[i+1] == jugador and ocupado[i+2] == jugador:

            if jugador==1:  ## sumele al jugador que gano en el puntaje
                   if imprimir:
                      window.blit(gano_uno,(55,450))
                   return True                  
            else:
                    if imprimir:
                       window.blit(gano_dos,(55,450))
                    return True                     
        i+=3

    i=0
    ## validar verticales 
    while i < 3 : ## validamos las 3 horizontales
        if ocupado[i] == jugador and ocupado[i+3] == jugador and ocupado[i+6] == jugador:

            if jugador==1:  ## sumele al jugador que gano en el puntaje
                   if imprimir:
                      window.blit(gano_uno,(55,450))
                   return True                   
            else:                    
                    if imprimir:
                      window.blit(gano_dos,(55,450))
                    return True                     
        i+=1

    ## Validamos las 2 diagonales
    if ocupado[0] == jugador and ocupado[4] == jugador and ocupado[8] == jugador:

            if jugador==1:  ## sumele al jugador que gano en el puntaje
                   if imprimir:
                      window.blit(gano_uno,(55,450))
                   return True                   
            else:                    
                    if imprimir:
                      window.blit(gano_dos,(55,450))
                    return True
    if ocupado[2] == jugador and ocupado[4] == jugador and ocupado[6] == jugador:

            if jugador==1:  ## sumele al jugador que gano en el puntaje
                   if imprimir:
                      window.blit(gano_uno,(55,450))
                   return True                   
            else:                    
                    if imprimir:
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
                                     
                                     if True : ## condicion que cambia el turno     ## Empieza el tuno del Jugador
                                         
                                            window.blit(x,posiciones_imagenes[i]) # pinta la imagen X en la pocision
                                            
                                            ocupado[i] = 1 # en caso de estar vacio, le asignamos 1 que esta lleno con X

                                            ## en cada turno comprobamos si alguno gano lugo del 5 turno                                            
                                            ## 3 son el minimo numero de movimientos para ganar 
                                            if ocupado.count(1)>=3: ## fi 1 aparese mas o igual de 5 veses, vaya y compruebe si gano
                                                
                                                if Ganador (ocupado,1,True) :
                                                    jugar = False ##si gano el jugador, salgase del juego
                                                    break;                                              

                                                    
                                            ## ---------------------------   MOVIMIENTOS DE LA IA --------------------------------------------------------

                                             # PRIMER MOVIMIENTO
                                             
                                            if ocupado.count(0) == 8 :## condicion para que la maquina de el primer movimiento aleatorio
                                               
                                               movimiento_maquina =  primero_IA()
                                               while ocupado[movimiento_maquina] != 0 :
                                                  
                                                   
                                                   
                                                   if ocupado[movimiento_maquina] == 0:
                                                      ocupado[movimiento_maquina] = 2    # en caso de estar vacio, le asignamos 2  que esta lleno con
                                                   
                                                   else: movimiento_maquina =  primero_IA()
                                                   
                                               ocupado[movimiento_maquina] = 2 
                                               window.blit(o,posiciones_imagenes[movimiento_maquina]) # pinta la imagen O en la pocision

                                           # SEGUNDO MOVIMIENTO                                           
                                                                                     
                                            if ocupado.count(0) == 6 :## 
                                               
                                               movimiento_maquina =  segundo_IA(ocupado)
                                             
                                               ocupado[movimiento_maquina] = 2
                                               
                                               window.blit(o,posiciones_imagenes[movimiento_maquina]) # pinta la imagen O en la pocision
                                               
                                          # TERCERO MOVIMIENTO
                                             
                                            if ocupado.count(0) == 4 :## io
                                               asigne = tercero_IA(ocupado)
                                               ocupado [asigne] = 2
                                               window.blit(o,posiciones_imagenes[asigne]) # pinta la imagen O en la pocision                                               

                                          # ULTIMO MOVIMIENTO
                                          
                                            if ocupado.count(0) == 2 :## condicion para que la maquina de eL ULTIMO movimiento en las 2 casillas disponibles
                                               asigne = ultimo_IA(ocupado)
                                               ocupado [asigne] = 2
                                               window.blit(o,posiciones_imagenes[asigne]) # pinta la imagen O en la pocision                                               
                                            
                                            ## en cada turno comprobamos si alguno gano lugo del 5 turno
                                            ## 3 son el minimo numero de movimientos para ganar 
                                            if ocupado.count(2) >=3: ## fi 2 aparese mas de 5 veses, vaya y compruebe si gano
                                                
                                                if Ganador (ocupado,2,True):
                                                    jugar = False
                                                    
                                                    ##Funcion_Juego (True,[0,0,0,0,0,0,0,0,0])
                         i += 1

                         ## si el tablero esta lleno, Termine
                         if ocupado.count(0) == 0 and  ( (not (Ganador (ocupado,2,True)) and (not (Ganador (ocupado,1,True))))):
                             window.blit(empate,(55,450))
                             juego=False
                             
            pygame.display.update()


Funcion_Juego (True,[0,0,0,0,0,0,0,0,0])





    
