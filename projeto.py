import turtle
import random

# Configuração da tela
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Show de Fogos com Turtle")

# Configurações da tartaruga
fogo = turtle.Turtle()
fogo.speed(0)
fogo.hideturtle()

# Lista de cores
cores = ["red", "yellow", "blue", "green", "orange", "purple", "cyan", "magenta", "white"]

# Função para desenhar uma explosão
def explosao(x, y, tamanho, quantidade_linhas):
    fogo.penup()
    fogo.goto(x, y)
    fogo.pendown()
    
    cor = random.choice(cores)
    fogo.color(cor)
    
    for _ in range(quantidade_linhas):
        angulo = random.randint(0, 360)
        comprimento = random.randint(tamanho//2, tamanho)
        fogo.setheading(angulo)
        fogo.forward(comprimento)
        fogo.penup()
        fogo.goto(x, y)
        fogo.pendown()

# Função para disparar vários fogos em lugares aleatórios
def show_fogos(qtd_fogos):
    for _ in range(qtd_fogos):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        tamanho = random.randint(50, 150)
        quantidade_linhas = random.randint(10, 25)
        explosao(x, y, tamanho, quantidade_linhas)

# Execução do show
show_fogos(20)

# Manter a tela aberta
tela.mainloop()
