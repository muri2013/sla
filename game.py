import pygame
import sys

# Inicialize o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo com Inimigo")

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Configurações do jogador
player_size = 50
player_color = BLUE
player_x, player_y = WIDTH // 2, HEIGHT - player_size
player_speed

