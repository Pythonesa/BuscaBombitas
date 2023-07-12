import pygame

pygame.init()

# Images:
background = pygame.image.load('resources/fondo.jpg')
tile_not_clicked = pygame.image.load('resources/notClicked.jpg')
tile_empty = pygame.image.load('resources/empty.jpg')
tile_1 = pygame.image.load('resources/1.jpg')
tile_2 = pygame.image.load('resources/2.jpg')
tile_3 = pygame.image.load('resources/3.jpg')
tile_4 = pygame.image.load('resources/4.jpg')
tile_5 = pygame.image.load('resources/5.jpg')
tile_6 = pygame.image.load('resources/6.jpg')
tile_7 = pygame.image.load('resources/7.jpg')
tile_8 = pygame.image.load('resources/8.jpg')
tile_flag = pygame.image.load('resources/flag.jpg')
tile_question = pygame.image.load('resources/question.jpg')
tile_clicked_bomb = pygame.image.load('resources/clickedBomb.jpg')
tile_bomb = pygame.image.load('resources/bomb.jpg')
tile_not_bomb = pygame.image.load('resources/notBomb.jpg')

# Config:
pygame.display.set_caption('BuscaBombitas')
bombs_amount = 10
grid_width = 9
grid_heigth = 9
timer = pygame.time.Clock()
grid = [] # main grid
mines = [] # pos of the mines
tile_size = 40
background_width = 850
background_heigth = 553

def drawText(text, x, y):
    pass

# Game loop:
def game_loop():
    pass

game_loop()
pygame.quit()
quit()
