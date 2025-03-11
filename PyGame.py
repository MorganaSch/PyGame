import pygame, random
from pygame.locals import *

def matriz_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def colisão(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')


cobra = [(200, 200), (210, 200), (220,200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((0, 255 , 0))
my_direction = LEFT

apple_pos = matriz_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))


clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_UP and my_direction != DOWN:
                my_direction = UP
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
            if event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
            if event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT

    if colisão(cobra[0], apple_pos):
        apple_pos = matriz_random()
        cobra.append((0,0))
        score = score + 1


        
    if cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0:
        game_over = True
        break
    
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True
            break


    for i in range(len(cobra) - 1,0 ,-1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
        
    
    if my_direction == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)

    if my_direction == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)

    if my_direction == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])

    if my_direction == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
    screen.fill((0,50,0))
    screen.blit(apple, apple_pos)
    
    score_font = font.render('Score: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (600 - 120, 10)
    screen.blit(score_font, score_rect)
    
    for pos in cobra:
        screen.blit(cobra_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (600 / 2, 10)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

       






  
