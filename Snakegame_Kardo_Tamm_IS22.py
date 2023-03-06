import pygame
import random

# initsialiseerib pygame
pygame.init()

# seadistab mängu aken
width = 600
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game-Kardo_Tamm")

# määratleb värvid
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# määrab ploki suuruse ja mao kiiruse
block_size = 10
snake_speed = 15

# määrab fonti
font = pygame.font.Font(None, 30)

# Seadistab kella
clock = pygame.time.Clock()

# seab mao esialgse asukoha ja suuruse
snake_x = width/2
snake_y = height/2
snake_size = 1
snake_body = []

# seadistab õuna algse asendi
apple_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
apple_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

# Määrab mangu timeri/aja
start_time = pygame.time.get_ticks()

# määrab mängutsükkli
game_over = False
while not game_over:
    #  tegeleb sündmustega
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # käepideme klahvivajutused (liikmymine)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= block_size
    if keys[pygame.K_RIGHT]:
        snake_x += block_size
    if keys[pygame.K_UP]:
        snake_y -= block_size
    if keys[pygame.K_DOWN]:
        snake_y += block_size


    # kontrollige õuna kokkupõrget ja värskendage mao suurust ja õuna asukohta
    if snake_x == apple_x and snake_y == apple_y:
        snake_size += 1
        apple_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        apple_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    # uuendab mao suurust
    snake_body.append([snake_x, snake_y])
    if len(snake_body) > snake_size:
        del snake_body[0]

    # kontrollib kokkupõrkeid seinte või mao kehaga
    if snake_x < 0 or snake_x > width - block_size or snake_y < 0 or snake_y > height - block_size:
        game_over = True
    for block in snake_body[:-1]:
        if block == [snake_x, snake_y]:
            game_over = True

    # Joonistab mängu objektid
    window.fill(black)
    for block in snake_body:
        pygame.draw.rect(window, green, [block[0], block[1], block_size, block_size])
    pygame.draw.rect(window, red, [apple_x, apple_y, block_size, block_size])

    # Uuendab mängu timerit/aega
    timer = pygame.time.get_ticks() - start_time
    timer_text = font.render("Time: " + str(round(timer/1000, 1)), True, white)
    window.blit(timer_text, [10, 10])

    # Uuendab displayd ehk akent
    pygame.display.update()

    # Määrab mängu/mao kiiruse
    clock.tick(snake_speed)
    # Paneb mängu loopi
    def gameLoop():
        game_over = False
        game_close = False