import pygame
import random




pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
levels = range(32,256,32)
dt = 0
lmao = False
psize = 40
increse = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(tuple(random.choice(levels) for _ in range(3)))
    pygame.draw.circle(screen, (tuple(random.choice(levels) for _ in range(3))), random.randint(0, 500), psize)
    if psize <= 99 and lmao == False:
        psize += increse
    elif psize >= 100:
        increse =1
        lmao = True
    if psize >= 1 and lmao == True:
        psize -= increse
    elif psize <= 0:
        increse = 1
        lmao = False
    print(psize)
    print(lmao)



    player_pos = pygame.mouse.get_pos()
    
#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_w]:
#        player_pos.y -= 300 * dt
#    if keys[pygame.K_s]:
#        player_pos.y += 300 * dt
#    if keys[pygame.K_a]:
#        player_pos.x -= 300 * dt
#    if keys[pygame.K_d]:
#        player_pos.x += 300 * dt

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60
    

pygame.quit()