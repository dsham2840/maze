# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1280
HEIGHT = 980
SIZE = (WIDTH, HEIGHT)
TITLE = "W A R Z O N E"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

#stages
START = 0
PLAYING = 1
END = 2


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (100, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (200, 200, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 150)
PURPLE = (255, 0, 255)
GRAY = (10, 10, 10)
ALSOGRAY =(20, 20, 20)
ORANGE = (255,150, 0 )
GROUND = (76, 38, 0)

def setup():
    global coins, score, stage, player, player_vx, player_vy, enemy, enemy_vx, enemy_vy, enemy_speed, player_speed, time_remaining, ticks
    # Make coins
    coin1 = [525, 50, 25, 25]
    coin2 = [37, 750, 25, 25]
    coin3 = [750, 175, 25, 25]
    coin4 = [387, 251, 25, 25]
    coin5 = [260, 675, 25, 25]
    coin6 = [450, 540, 25, 25]
    coin7 = [660, 560, 25, 25]
    coin8 = [525, 475, 25, 25]
    coin9 = [190, 200, 25, 25]
    coin10 = [360, 150, 25, 25]
    coin11 = [940, 400, 25, 25]
    coin12 = [960, 450, 25, 25]
    coin13 = [940, 500, 25, 25]
    coin14 = [767, 410, 25, 25]
    coin15 = [1130, 410, 25, 25]
    coin16 = [767, 485, 25, 25]
    coin17 = [1130, 485, 25, 25]
    coin18 = [40, 375, 25, 25]
    coin19 = [40, 475, 25, 25]
    coin20 = [650, 665, 25, 25]
    coin21 = [225, 825, 25, 25]
    coin22 = [500, 825, 25, 25]
    coin23 = [1100, 150, 25, 25]
    coin24 = [1216, 40, 25, 25]
    coin25 = [732, 740, 25, 25]
    coin26 = [822, 711, 25, 25]
    coin27 = [1200, 736, 25, 25]
    coin28 = [911, 111, 25, 25]
    coin29 = [275, 382, 25, 25]

    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9,
             coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17,
             coin18, coin19, coin20, coin21, coin22, coin23, coin24, coin25,
             coin26, coin27, coin28, coin29]

    # Make a player
    player =  [40, 40, 25, 25]
    player_vx = 0
    player_vy = 0
    player_speed = 5

    enemy =  [1200, 910, 25, 25]
    enemy_vx = 0
    enemy_vy = 0
    enemy_speed = 5

    stage = START
    time_remaining = 120
    ticks = 0
    score = 0

#Stages
START = 0
PLAYING = 1
END = 2


# make walls

''' border walls '''
wall1 =  [0, -25, 600, 50]
wall2 =  [ 680, -25, 600, 50 ]
wall3 =  [-25, 0, 50, 450]
wall4 =  [-25, 530, 50, 450]
wall5 =  [0, 955, 600, 50]
wall6 =  [680, 955, 600, 50]
wall7 =  [1255, 0, 40, 450]
wall8 =  [1255, 530, 50, 450]

''' Maze Walls '''
wall9 =  [75, 0, 25, 200]
wall10 = [75, 250, 25, 125]
wall11 = [0, 425, 250, 25]
wall12 = [75, 350, 175, 25]
wall13 = [225, 450, 25, 175]
wall14 = [325, 350, 175, 25]
wall15 = [75, 175, 100, 25]
wall16 = [150, 175, 25, 125]
wall17 = [225, 125, 25, 250]
wall18 = [150, 100, 375, 25]
wall19 = [575, 0, 25, 125]
wall20 = [325, 425, 25, 300]
wall21 = [150, 525, 25, 200]
wall22 = [150, 725, 200, 25]
wall23 = [75, 450, 25, 200]
wall24 = [75, 700, 25, 200]
wall25 = [0, 700, 75, 25]
wall26 = [100, 875, 200, 25]
wall27 = [150, 750, 25, 100]
wall28 = [200, 775, 25, 100]
wall29 = [250, 725, 25, 125]
wall30 = [300, 775, 25, 125]
wall31 = [350, 750, 25, 175]
wall32 = [300, 175, 25, 200]
wall33 = [300, 175, 400, 25]
wall34 = [300, 150, 25, 25]
wall35 = [350, 125, 25 , 25]
wall36 = [400, 150, 25, 25]
wall37 = [450, 125, 25, 25]
wall38 = [500, 150, 25, 25]
wall39 = [550, 125, 25, 25]
wall40 = [700, 50, 25, 150]
wall41 = [700, 50, 300, 25]
wall42 = [1025, 0, 25, 300]
wall43 = [975, 50, 25, 150]
wall44 = [700, 100, 25, 200]
wall45 = [700, 300, 350, 25]
wall46 = [800, 125, 25, 50]
wall47 = [800, 225, 25, 50]
wall48 = [400, 425, 150, 25]
wall49 = [525, 225, 25, 200]
wall50 = [350, 225, 25, 100]
wall51 = [425, 225, 25, 100]
wall52 = [350, 300, 100, 25]
wall53 = [525, 250, 100, 25]
wall54 = [400, 425, 25, 200]
wall55 = [400, 625, 300, 25]
wall56 = [700, 375, 25, 275]
wall57 = [600, 350, 25, 25]
wall58 = [550, 400, 25, 25]
wall59 = [534, 502, 25, 25]
wall60 = [571, 526, 25, 25]
wall61 = [1560, 666, 25, 25]
wall62 = [502, 567, 25, 25]
wall63 = [572, 466, 25, 25]
wall64 = [617, 432, 25, 25]
wall65 = [632, 522, 25, 25]
wall66 = [470, 510, 25, 25]
wall67 = [700, 350, 100, 25]
wall68 = [850, 350, 250, 25]
wall69 = [1075, 50, 25, 325]
wall70 = [1175, 0, 25, 325]
wall71 = [1075, 75, 75, 25]
wall72 = [1125, 125, 75, 25]
wall73 = [1075, 175, 75, 25]
wall74 = [1125, 225, 75, 25]
wall75 = [1075, 275, 75, 25]
wall76 = [1075, 350, 125, 25]
wall77 = [1200, 300, 25, 25]
wall78 = [1230, 250, 25, 25]
wall79 = [1200, 200, 25, 25]
wall80 = [1230, 150, 25, 25]
wall81 = [1200, 100, 25, 25]
wall82 = [1175, 400, 25, 150]
wall83 = [1175, 525, 200, 25]
wall84 = [950, 375, 25, 25]
wall85 = [950, 425, 25, 25]
wall86 = [950, 475, 25, 25]
wall87 = [950, 525, 25, 25]
wall88 = [750, 550, 350, 25]
wall89 = [750, 450, 25, 25]
wall90 = [800, 450, 25, 25]
wall91 = [850, 450, 25, 25]
wall92 = [900, 450, 25, 25]
wall93 = [1000, 450, 25, 25]
wall94 = [1050, 450, 25, 25]
wall95 = [1100, 450, 25, 25]
wall96 = [1150, 450, 25, 25]
wall97 = [400, 700, 375, 25]
wall98 = [775, 600, 25, 125]
wall99 = [775, 625, 200, 25]
wall100 = [1025, 575, 25, 325]
wall101 = [775, 700, 25, 75]
wall102 = [775, 750, 100, 25]
wall103 = [950, 625, 25, 150]
wall104 = [700, 725, 25, 100]
wall105 = [700, 825, 300, 25]
wall106 = [875, 675, 25, 100]
wall107 = [825, 675, 50, 25]
wall108 = [600, 875, 450, 25]
wall109 = [1050, 850, 150, 25] 
wall110 = [1100, 775, 300, 25]
wall111 = [1050, 700, 150, 25]
wall112 = [1100, 625, 300, 25]
wall113 = [575, 875, 25, 200]



walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8,
         wall9, wall10, wall11, wall12, wall13, wall14, wall15,
         wall16, wall17, wall18, wall19, wall20, wall21, wall22,
         wall23, wall24, wall25, wall26, wall27, wall28, wall29,
         wall30, wall31, wall32, wall33, wall34, wall35, wall36,
         wall37, wall38, wall39, wall40, wall41, wall42, wall43,
         wall44, wall45, wall46, wall47, wall48, wall49, wall50,
         wall51, wall52, wall53, wall54, wall55, wall56, wall57,
         wall58, wall59, wall60, wall61, wall62, wall63, wall64,
         wall65, wall66, wall67, wall68, wall69, wall70, wall71,
         wall72, wall73, wall74, wall75, wall76, wall77, wall78,
         wall79, wall80, wall81, wall82, wall83, wall84, wall85,
         wall86, wall87, wall88, wall89, wall90, wall91, wall92,
         wall93, wall94, wall95, wall96, wall97, wall98, wall99,
         wall100, wall101, wall102, wall103, wall104, wall105, wall106,
         wall107, wall108, wall109, wall110, wall111, wall112, wall113]

# teleporters

tp1 = [620, 590, 25, 25]
tp2 = [1200, 75, 25, 25]
tp3 = [874, 749, 25, 25]

teleporters = [tp1, tp2, tp3]

tp4 = [500, 885, 25, 25]
tp5 = [600, 830, 25, 25]

evilteleporters = [tp4, tp5]

# sounds/ pictures/ fonts
start_sound = pygame.mixer.Sound("entering_warzone.wav")
coin_sound = pygame.mixer.Sound("goodmemev2.wav")
img = pygame.image.load('splashcreen.jpg')
MY_FONT = pygame.font.Font(None, 50)
player_icon = pygame.image.load('player_icon.png')
coin_icon = pygame.image.load('coin_icon.png')
enemy_icon = pygame.image.load('enemy_icon.png')

# Game loop
win = False
done = False
lose = False
setup()

stage = START
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    start_sound.play(0)
                    stage = PLAYING

            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()
                    stage == START

    if stage == PLAYING:

        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
            
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
            player_vx = 0

        upe = pressed[pygame.K_w]
        downe = pressed[pygame.K_s]
        lefte = pressed[pygame.K_a]
        righte = pressed[pygame.K_d]

        if upe:
            enemy_vy = -enemy_speed
        elif downe:
            enemy_vy = enemy_speed
        else:
            enemy_vy = 0
            
        if lefte:
            enemy_vx = -enemy_speed
        elif righte:
            enemy_vx = enemy_speed
        else:
            enemy_vx = 0

        

        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    player[0] += player_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    player[1] += player_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]

    # enemy
    ''' move the player in horizontal direction '''
    enemy[0] += enemy_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(enemy, w):        
            if enemy_vx > 0:
                enemy[0] = w[0] - enemy[2]
            elif enemy_vx < 0:
                enemy[0] = w[0] + w[2]

    ''' move the player in vertical direction '''
    enemy[1] += enemy_vy
    
    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(enemy, w):                    
            if enemy_vy > 0:
                enemy[1] = w[1] - enemy[3]
            if enemy_vy < 0:
                enemy[1] = w[1] + w[3]

    ''' timer stuff '''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            lose = True

                


    ''' here is where you should resolve player collisions with screen edges '''

    left = player[0]
    right = player[0] + player[2]
    top = player[1]
    bottom = player[1] + player[3]

    if bottom < 0:
        player[1] = HEIGHT
    elif top > HEIGHT:
        player[1] = 0 - player[3]

    if left > WIDTH:
        player[0] = 0 - player[2]
    elif right < 0:
        player[0] = WIDTH

    #enemy

    lefte = enemy[0]
    righte = enemy[0] + enemy[2]
    tope = enemy[1]
    bottome = enemy[1] + enemy[3]

    if bottome < 0:
        enemy[1] = HEIGHT
    elif tope > HEIGHT:
        enemy[1] = 0 - enemy[3]

    if lefte > WIDTH:
        enemy[0] = 0 - enemy[2]
    elif righte < 0:
        enemy[0] = WIDTH



    ''' get the coins '''
    hit_list = [c for c in coins if intersects.rect_rect(player, c)]

    for hit in hit_list:
        coins.remove(hit)
        score += 1
        coin_sound.play(0)

    font3 = pygame.font.Font(None, 50)
    scoretext = font3.render("SCORE: " + str(score), 1, WHITE)
    screen.blit(scoretext, [175, 50])

    if len(coins) == 0:
        win = True

    if intersects.rect_rect(player, enemy):
        player = [40, 40, 25, 25]

    # teleporter teleportation
    if intersects.rect_rect(player, tp1):
        player = [1200, 800, 25, 25]

    if intersects.rect_rect(player, tp2):
        player = [600, 420, 25, 25]

    if intersects.rect_rect(player, tp3):
        player = [250, 382, 25, 25]

    if intersects.rect_rect(player, tp4):
        player = [100, 920, 25, 25]

    if intersects.rect_rect(player, tp5):
        player = [1200, 920, 25, 25]

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(GROUND)

    screen.blit(player_icon, (player[0], player[1]))
    screen.blit(enemy_icon, (enemy[0], enemy[1]))

    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [125, 50])
    
    
    
    for w in walls:
        pygame.draw.rect(screen, ALSOGRAY, w)

    for c in coins:
        screen.blit(coin_icon, (c[0], c[1]))

    for t in teleporters:
        pygame.draw.rect(screen, ALSOGRAY, t)

    for x in evilteleporters:
        pygame.draw.rect(screen, GROUND, x)
        
    if win:
        stage = END
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        pygame.draw.rect(screen, WHITE, [495, 320, 290, 290])
        pygame.draw.rect(screen, BLACK, [500, 325, 280, 280])
        screen.blit(text, [567, 450])
        

    if lose:
        stage = END
        font = pygame.font.Font(None, 48)
        text = font.render("You Lose!", 1, RED)
        pygame.draw.rect(screen, WHITE, [495, 320, 290, 290])
        pygame.draw.rect(screen, BLACK, [500, 325, 280, 280])
        screen.blit(text, [567, 450])

    if stage == END:
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over!", 1, WHITE)
        player_vx = 0
        player_vy = 0
        enemy_vx = 0
        enemy_vy = 0
        
    if stage == START:
        screen.blit(img, (0, 0))

    
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
