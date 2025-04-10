import pygame, time, sys

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
frame = pygame.image.load("clock.png")
seconds = pygame.image.load("sec_hand.png")
minutes = pygame.image.load("min_hand.png")

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.blit(frame, (0,0))
    now = time.localtime()
    minuteAngle = 360 - (now.tm_min * 6)
    minRotate = pygame.transform.rotate(minutes, minuteAngle)
    minPos = ((size[0] - minRotate.get_width())/2, (size[1] - minRotate.get_width())/2)
    screen.blit(minRotate, minPos)

    secondAngle = 360 - (now.tm_sec * 6)
    secRotate = pygame.transform.rotate(seconds, secondAngle)
    secPos = ((size[0] - secRotate.get_width())/2, (size[1] - secRotate.get_width())/2)
    screen.blit(secRotate, secPos)
    pygame.display.flip()

pygame.quit()

sys.exit()