
import turtle
import random


#primeiro passo temos que definir nossa tartaruga


t = turtle.Turtle()


turtle.Screen().bgcolor("black")
#tambem e bom definirmos as cores dos fogos de artificio


#temos que definir uma funcao que ira desenhar as cores das linhas da nossa tartaruga
def pen_colours(colours):
  cor = random.choice(colors) 
  t.color(cor)
#temos que definir uma funcao que ira definir que ira causar a explosao


def explosao(distance):
 for _ in range(20): 
    #criar uma petala
    t.forward(180 - (360 / 20))
    t.left(distance)

#tambem temos que definir uma funcao que ira mover a tartaruga
#que ira definir de forma aleatoria onde irao aparecer
def mover():
  #oque diabos e esse penup
  #fazer a tartaruga se mover pra aquela posicao sem deixar linha/rastro pelo caminho
  t.penup()
  #definir posicoes aleatorias
  x = random.randint(-300,300)
  y =  random.randint(-300, 300)

  #definindo a posicao da tartaruga no eixo x e no eixo y
  #a tartaruga vai se mover para aquela posicao 
  t.goto(x,y)
  #oque diabos e esse pendown

  # o pendown serve para a tartaruga voltar a desenhar naquela nova posicao
  t.pendown()

#iremos repetir esse processo 30 vezes

colors = ["red", "blue" , "green"]

for _ in range(30):
  pen_colours(colors)
  mover()
  explosao(random.randint(50,150))
  #ele tem que fazer esse processo para cada petala diferente


turtle.done()

