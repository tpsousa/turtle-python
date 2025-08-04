

from turtle import *

#nome da tartagura bob

bob = Turtle()

bob.color('blue')
#move 100 passos para direita
bob.forward(100)

#gira a tartaruga -- muda o angulo para 120 graus
bob.left(120)

#andar 100 passos pra essa direcao
bob.forward(100)

bob.forward(120)

#girou novamente a 120 graus
bob.left(120)

#depois de termos mudado a direcao da tartaruga,basta fazer caminha-la novamente 100 passos

bob.forward(100)
bob.forward(121)
bob.left(120)

bob.forward(100)

#envia a tartaruga para o ponto de partida
home()
clearscreen()

#usando for loops e possivel definir padroes geometricos: 
#ta dizendo que ira percorrer 100 vezes,ou seja que o steps serve para
#dar 100 passos

''''
for steps in range(100):
   
   #ele vai percorrer cada cor e definir como a cor do passo
   for c in ('blue','red', 'green'):
     #o primeiro passo vai ser azul,o segundo vai ser vermelho,e o terceiro vai ser verde e assim por diante
     color(c)
     #a tartaruga vai dar 100 passos
     #vai percorrer de acordo com a quantidade dos steps
     forward(steps)
     #e a tartaruga vai virar 30 graus para a direita
     right(30)
'''''''''
     #obs : para cada passo que ele der ele vai dar uma cor diferente para a linha


ana = Turtle()
ana.forward(100)

#define a direcao para a esquerda
ana.left(90)
#define a direcao para a direita
ana.forward(100)

#define a direcao para a esquerda
ana.left(90)
#e assim por diante
ana.forward(100)

ana.left(90)
ana.forward(100)