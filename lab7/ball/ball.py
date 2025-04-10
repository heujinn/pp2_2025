import pygame
import sys

pygame.init()

screenWidth = 800
screenHeight = 600

white = (255, 255, 255)
red = (255, 0, 0)

ballSize = 50
ballRad = ballSize // 2
ballX = (screenWidth - ballSize) // 2
ballY = (screenHeight - ballSize) // 2
ballSpeed = 20

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ballY -= ballSpeed
    elif keys[pygame.K_DOWN]:
        ballY += ballSpeed
    elif keys[pygame.K_LEFT]:
        ballX -= ballSpeed
    elif keys[pygame.K_RIGHT]:
        ballX += ballSpeed
    
    ballX = max(0, min(screenWidth - ballSize, ballX))
    ballY = max(0, min(screenHeight - ballSize, ballY))
    
    screen.fill(white)
    
    pygame.draw.circle(screen, red, (ballX + ballRad, ballY + ballRad), ballRad)
    
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()

sys.exit()