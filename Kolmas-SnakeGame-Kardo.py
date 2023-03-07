# importib packaged
import pygame
import time
import random
# Ussi kiirus
snake_speed = 15

# Ekraani suurus
window_x = 720
window_y = 480

# Määrab värvid
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialiseerib pygame
pygame.init()

# Initialiseerib mängu ekraani
pygame.display.set_caption('Ussimäng')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second)
fps = pygame.time.Clock()

# Määrab ussi asukoha
snake_position = [100, 50]

# mao keha esimese 4 plokki määratlemine
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# Õuna asukoht
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# mao vaikesuuna määramine
# #õige
direction = 'RIGHT'
change_to = direction

# esialgne punktisumma
score = 0


# skoori funktsiooni kuvamine
def show_score(choice, color, font, size):
    # fondiobjekti loomine score_font
    score_font = pygame.font.SysFont(font, size)

    # luua kuvapinna objekt
    # skoori_pind
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # luua teksti jaoks ristkülikukujuline objekt
    # pinnaobjekt
    score_rect = score_surface.get_rect()

    # teksti kuvamine
    game_window.blit(score_surface, score_rect)


# mäng üle funktsiooni
def game_over():
    # fondiobjekti loomine minu_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # tekstipinna loomine, millel tekst
    # Joonistatakse
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)

    # luua teksti jaoks ristkülikukujuline objekt
    # pinnaobjekt
    game_over_rect = game_over_surface.get_rect()

    # teksti asukoha määramine
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit joonistab teksti ekraanile
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # 2 sekundi pärast sulgeme programmi
    time.sleep(2)

    # pygame'i raamatukogu desaktiveerimine
    pygame.quit()

    # programmist väljuda
    quit()


# Peamine funktsioon
while True:

    # võtmesündmuste käsitlemine
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Kui kaks klahvi korraga vajutatakse
    # me ei taha, et madu kaheks koliks

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Ussi liikumine eri suundades
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Madu keha kasvatamise mehhanism
    # kui puuviljad ja maod põrkuvad, siis hinded
    # suurendatakse 10 võrra
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Mängu tingimused
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # Mao keha puudutamine
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # skoori pidev kuvamine
    show_score(1, white, 'times new roman', 20)

    # Uuendab mängu ekraani
    pygame.display.update()

    # Mitu pikslit sekundis
    fps.tick(snake_speed)
