import pygame, os

pygame.init()

screenWidth = 475
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))
image = pygame.image.load('bg.jpg')
image = pygame.transform.scale(image, (screenWidth, screenHeight))
music = 'music'

musicFiles = [f for f in os.listdir(music) if f.endswith('.mp3')]

currentMusic = 0
paused = False

pygame.mixer.music.load(os.path.join(music, musicFiles[currentMusic]))
pygame.mixer.music.play()
font = pygame.font.SysFont(None, 40) 

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                currentMusic = (currentMusic + 1) % len(musicFiles)
                pygame.mixer.music.load(os.path.join(music, musicFiles[currentMusic]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                currentMusic = (currentMusic - 1) % len(musicFiles)
                pygame.mixer.music.load(os.path.join(music, musicFiles[currentMusic]))
                pygame.mixer.music.play()

    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    musicName = musicFiles[currentMusic].split('.')[0]
    text = font.render(musicName, True, (255, 255, 255))
    textRect = text.get_rect(center=(screenWidth // 2 - 30, 560))  # сместили
    screen.blit(text, textRect)
    pygame.display.flip()

pygame.quit()