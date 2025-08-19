
import turtle
import math

# Configurações iniciais
turtle.bgcolor("white")
turtle.color("red")
turtle.speed(0)

#r - raio, a- arco
def criar_raio(raio, angulo):
    turtle.circle(raio, angulo)

def desenhar_petala(quantidade_petalas, quantidade_arcos_petala, raio, angulo):
    for i in range(quantidade_petalas):
        for j in range(quantidade_arcos_petala):
            criar_raio(raio, angulo)
            turtle.left(120)
        turtle.left(360 / quantidade_petalas)
t = turtle.Turtle()
desenhar_petala(36,2, 100,60)

#vamos tentar fazer de forma recursiva
def circulo(raio,angulo):
  turtle.circle(raio,angulo)

def criar_flor(quantidade_petalas):
    if quantidade_petalas == 0 : 
        return 
        turtle.done()
    else : 
       raio  = 100
       angulo = 60

       circulo(raio,angulo)
       turtle.left(120)
    turtle.left(360 / quantidade_petalas)

    criar_flor(quantidade_petalas - 1) 
quantidade_petalas = 100
criar_flor(quantidade_petalas)

# Desenha as pétalas
'''for i in range(36):  # 36 pétalas (cada uma com 10 graus de rotação)
    for j in range(2):  # cada pétala tem dois arcos
        turtle.circle(100, 60)  # raio 100, arco de 60 graus
        turtle.speed(5)
        turtle.left(120)  
                      # gira para o próximo arco
    turtle.left(10)  # gira para a próxima pétala'''
turtle.hideturtle()
turtle.done()

# Desenha o miolo
turtle.color("purple")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# Finaliza
turtle.hideturtle()
turtle.done()
