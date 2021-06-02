import turtle
import time
import random

posponer = 0.1

#marcador
score=0
hscore=0

#cabecera. pantalla principal
ventana = turtle.Screen()
ventana.title("SNAKE")
ventana.bgcolor("black")
ventana.setup(width = 600, height = 600)
ventana.tracer(0)

#Cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup() #para que no deje rastro
head.goto(0,0) #empieza en el centro. la esquina inferior izquierda es (-300,-300), 
#y la superior derecha al contrario. mismas coordenadas que el plano cartesiano. 300 por ser la mitad de lo que dijimos que medía la pantalla
head.direction = "stop" #definimos una direcion de movimiento. con stop indicamos que espere nuestra señal

#Comida de la serpiente
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,0)

#Cuerpo de la serpiente
cuerpo = []

#texto
tex = turtle.Turtle()
tex.speed(0) #para que no se desplace. que aparezca ya pintado
tex.color("white")
tex.penup() #sin rastro
tex.hideturtle() #aparece oculto en un principio
tex.goto(0,260)
tex.write("Score: 00      High Score: 200", align = "center", font = ("Courier", 24, "normal"))

gameover = turtle.Turtle()
gameover.speed(0) #para que no se desplace. que aparezca ya pintado
gameover.color("red")
gameover.penup() #sin rastro
gameover.hideturtle() #aparece oculto en un principio
gameover.goto(0,0)

#asociamos texto con el teclado
def arriba():
    if head.direction != "down" :
        head.direction = "up"
def abajo():
    if head.direction != "up" :
        head.direction = "down"
def izquierda():
    if head.direction != "right" :
        head.direction = "left"
def derecha():
    if head.direction != "left" :
        head.direction = "right" 
def parar():
    head.direction = "stop"

#funciones de movimiento
def mov():
    if head.direction == "up":
        y = head.ycor() #pedimos a la pantalla que nos diga la coordenada Y
        head.sety(y + (20)) #aumentamos (20) pixeles a la coordenada actual de la head

    if head.direction == "down":
        y = head.ycor() 
        head.sety(y - (20))

    if head.direction == "left":
        x = head.xcor() 
        head.setx(x - (20))

    if head.direction == "right":
        x = head.xcor() 
        head.setx(x + (20))

#asociamos ahora el teclado con el movimiento de la pantalla
ventana.listen() #la ventana esté atenta a lo que apretemos en el teclado
ventana.onkeypress(arriba, "Up") #Cuando apretemos tecla Up corresponderá a nuestra funcion de movimiento "arriba"
ventana.onkeypress(abajo, "Down")#importante la mayúscula, para hacer referencia al teclado
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")
ventana.onkeypress(parar, "space")

#Comenzamos la definición del juego. While implica el desarrollo del juego
while True:
    ventana.update()

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280 :
        head.sety(- head.ycor())
        head.setx(- head.xcor())


    #colision con el borde
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280 :
        gameover.write("Game over", align = "center", font = ("Consolas", 80, "normal"))
        time.sleep(2)
        gameover.clear()
        head.direction = "stop"
        head.goto(0,0)
        posponer = 0.1
        
        longitud = len(cuerpo)
        for i in cuerpo:
            i.goto(1000,1000)

        head.direction = "stop"
        cuerpo.clear()
        score = 0
        tex.clear()
        tex.write("Score: {}      High Score: {}".format(score,hscore), align = "center", font = ("Courier", 24, "normal"))


    if head.distance(food) < 20: #se pone 20 por ser el tamaño del cuadrado
        x = random.randint(-14,14) #no se pone 300 por la misma razón
        y = random.randint(-14,14)    #randint significa que el valor es un entero
        food.goto(20*x,20*y)

        nuevo_segmento = turtle.Turtle() #creamos un nuevo segmento en la pantalla, pero ahora falta ponerle las coordenadas para que siga la serpiente
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        cuerpo.append(nuevo_segmento) #añadimos al cuerpo el nuevo segmento que hemos conseguido

        score+=10
        #posponer *=0.8

        if score > hscore:
            hscore = score

        tex.clear()
        tex.write("Score: {}      High Score: {}".format(score,hscore), align = "center", font = ("Courier", 24, "normal"))

    #ahora vamos a hacer que los segmentos nuevos sigan a la cabeza
    longitud = len(cuerpo) #metemos en esta variable la longitud total del cuerpo
    for i in range(longitud -1, 0, -1): #range, introduces el primer termino, el ultimo, y el incremento
        x=cuerpo[i-1].xcor()
        y=cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y) #hacemos que cada segmento siga al que tiene delante

    #el primer segmento sigue a la cabeza
    if longitud > 0:
        x = head.xcor()
        y = head.ycor()
        cuerpo[0].goto(x,y)

    mov()

    #colisiones con el cuerpo
    for segmento in cuerpo:
        if segmento.distance(head) <20:
            gameover.write("Game over", align = "center", font = ("Consolas", 80, "normal"))
            time.sleep(2)
            gameover.clear()
            
            head.direction = "stop"
            head.goto(0,0)
            
            longitud = len(cuerpo)
            for i in cuerpo:
                i.goto(1000,1000)

            head.direction = "stop"
            cuerpo.clear()   
            score = 0
            tex.clear()
            tex.write("Score: {}      High Score: {}".format(score,hscore), align = "center", font = ("Courier", 24, "normal"))
      

    time.sleep(posponer)
    