import pygame

pygame.init()

width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
is_up = True
is_right = True
ball = [width / 2, height / 2]
ball_radius = 20

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    ball[0] -= is_right * 2 - 1
    ball[1] -= is_up * 2 - 1

    if ball[0] - ball_radius <= 0: 
        is_right = False
    
    if ball[0] + ball_radius >= width:
        is_right = True
    
    if ball[1] - ball_radius <= 0:
        is_up = False
    
    if ball[1] + ball_radius >= height:
        is_up = True

    pygame.draw.circle(screen, (255, 0, 0), ball, ball_radius)
    pygame.display.update()
    screen.fill((0, 0, 0))