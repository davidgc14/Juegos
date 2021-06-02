import pygame, sys
import random


#Inicializamos el motor de juego
pygame.init() 
clock = pygame.time.Clock()

#Creamos la ventana principal

ancho = 1200
alto = 600
#definimos escenario. importante no cambiar
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("PONG")

#creamos la esfera, mediante una imagen
ball = pygame.Rect(ancho/2-15,alto/2-15,30,30)
player1 =pygame.Rect(ancho-20, alto/2-70,10,140)
player2 =pygame.Rect(10, alto/2-70,10,140)
player1speed = 0
player2speed = 0
velocidad = [4,3] #vector velocidad

#texto
fuente = pygame.font.Font(None, 80 )#fuente de letra)
text = fuente.render("Game over", True, (255,255,255))

#definimos el movimiento de la esfera
def ball_mov():
    ball.x += velocidad[0]
    ball.y += velocidad[1]

    if ball.top<= 0 or ball.bottom >= alto:
        velocidad[1] *=-1
    if ball.colliderect(player1) or ball.colliderect(player2): #devuelve true si dos rectangulos estan juntos (colisión)
        velocidad[0] *=-1.2
        velocidad[1] *=1.2
    
    if ball.left <= 0 or ball.right >= ancho:
        restart()



#empezamos a pintar
bgcolor = pygame.Color("grey12") #fondo
light_grey = (200,200,200) #barras

def paint():
    #pintamos las figuras. importante el orden en el que los ponemos
    pantalla.fill(bgcolor)
    pygame.draw.rect(pantalla, light_grey, player1)
    pygame.draw.rect(pantalla, light_grey, player2)
    pygame.draw.ellipse(pantalla, light_grey, ball) #dibujamos una elipse dentro del cuadrado de ball, que como es un cuadrado, será un circulo
    pygame.draw.aaline(pantalla, light_grey, (ancho/2,0), (ancho/2,alto)) #linea de medio campo    

def restart():
    ball.center = (ancho/2-15,alto/2-15)
    velocidad[0] = 4
    velocidad[1] =3
    pantalla.blit(text, (100,100))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#si apretamos cerrar ventana, el juego se acaba
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: #KEYDOWN = alguna tecla apretada
            if event.key == pygame.K_DOWN: #la tecla apretada es flecha abajo
                player1speed += 7
            if event.key == pygame.K_UP: #la tecla apretada es flecha arriba
                player1speed -= 7
        if event.type == pygame.KEYUP: #KEYDOWN = alguna tecla levantada
            if event.key == pygame.K_DOWN: #Cuando se levante la flecha se vuelve a velocidad cero
                player1speed -= 7
            if event.key == pygame.K_UP:
                player1speed += 7

        if event.type == pygame.KEYDOWN: #KEYDOWN = alguna tecla apretada
            if event.key == pygame.K_z: #la tecla apretada es flecha abajo
                player2speed += 7
            if event.key == pygame.K_a: #la tecla apretada es flecha arriba
                player2speed -= 7
        if event.type == pygame.KEYUP: #KEYDOWN = alguna tecla levantada
            if event.key == pygame.K_z: #Cuando se levante la flecha se vuelve a velocidad cero
                player2speed -= 7
            if event.key == pygame.K_a:
                player2speed += 7  
        

                
    player1.y += player1speed
    player2.y += player2speed

    if player1.top <= 0:
        player1.top = 0
    if player1.bottom <= 0:
        player1.bottom = 0

    if player2.top <= 0:
        player2.top = 0
    if player2.bottom <= 0:
        player2.bottom = 0


        
    ball_mov()

    

    paint()


    #Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60) #60fps. Si no controlamos esto, el ordenador intentará procesarlo al máximo. Puede petar