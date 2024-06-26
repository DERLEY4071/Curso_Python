import pygame
from pygame.locals import *
from sys import exit
from random import *

pygame.init()

altura = 480
largura = 640

# Definindo Posição e tamanho do retangulo
pos_y_retangulo = altura / 2
pos_x_retangulo = largura / 2
largura_retangulo = 30
altura_retangulo = 40

#Definindo Posição e Tamanho do Circulo
pos_y_circulo = circulo = 40
pos_x_circulo = circulo = 40
raio_circulo = 10

#Definindo Fonte
fonte = pygame.font.SysFont("arial", 20, True, False)
pontos = 0

# Criando a Janela
tela = pygame.display.set_mode((largura, altura))
# Definir titulo da Janela
pygame.display.set_caption("Criando Jogos")

#Modificar a taxa de atualização de Pixels/Segundo
relogio = pygame.time.Clock()

while True:
    relogio.tick(25)
    tela.fill((0,0,0))
    mensagem = f'pontos: {pontos}'
    textoFormatado = fonte.render(mensagem, True,(255,255,255))
    
    #Colocando os enventos no Pygame
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit
            
        # if event.type ==  KEYDOWN:
        #     if event.key == K_UP:
        #         pos_y_retangulo -= 10
                
        #     if event.key == K_DOWN:
        #         pos_y_retangulo += 10
                
        #     if event.key == K_LEFT:
        #         pos_x_retangulo -= 10
                
        #     if event.key == K_RIGHT:
        #         pos_x_retangulo += 10
        
    if pygame.key.get_pressed()[K_UP]:
        pos_y_retangulo -= 10
    elif pygame.key.get_pressed()[K_LEFT]:
        pos_x_retangulo -= 10
    elif pygame.key.get_pressed()[K_RIGHT]:
        pos_x_retangulo +=10
    elif pygame.key.get_pressed()[K_DOWN]:
        pos_y_retangulo +=10
            
            
            
    retangulo = pygame.draw.rect(tela, (0,0,255), (pos_x_retangulo,pos_y_retangulo,largura_retangulo, altura_retangulo))
    
    circulo = pygame.draw.circle(tela, (255,0,255), (pos_x_circulo,pos_y_circulo), raio_circulo )
    
    if retangulo.colliderect(circulo):
        pos_x_circulo = randint(40,600)
        pos_y_circulo = randint(50,430)
        pontos += 1
        
    tela.blit(textoFormatado, (400,40))
        
    
    
    # Atualizar o jogo a cada interação
    pygame.display.update()
    
    
    
           



