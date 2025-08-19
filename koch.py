import turtle

# Função recursiva para desenhar a curva de Koch
def curva_koch(t, comprimento, nivel):
    if nivel == 0:
        t.forward(comprimento)
    else:
        comprimento /= 3.0
        curva_koch(t, comprimento, nivel - 1)
        t.left(60)
        curva_koch(t, comprimento, nivel - 1)
        t.right(120)
        curva_koch(t, comprimento, nivel - 1)
        t.left(60)
        curva_koch(t, comprimento, nivel - 1)

# Função para desenhar o floco de neve de Koch (3 lados)
def floco_de_neve(t, comprimento, nivel):
    for _ in range(3):
        curva_koch(t, comprimento, nivel)
        t.right(120)

# Configuração da tela e tartaruga
tela = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Velocidade máxima

# Posição inicial
t.penup()
t.goto(-150, 90)
t.pendown()

# Desenhar o floco de neve
floco_de_neve(t, 300, 4)  # 300 pixels de lado, nível de recursão 4

t.hideturtle()
tela.mainloop()
