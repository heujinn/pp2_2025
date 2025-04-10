import pygame as pg
import random, time

pg.init()
# вводим переменные
w, h, fps = 400, 600, 60
isRunning, lose = True, False
screen = pg.display.set_mode((w, h))
clock = pg.time.Clock()
y = 0
ry = 2
step, enemyStep, score, scoreCoin = 5, 5, 0, 0
gameOver = pg.image.load("gameover.jpg")
bg = pg.image.load("track.png")
gameOver = pg.transform.scale(gameOver, (w, h))

# задаем фонт для текста
scoreFont = pg.font.SysFont("Verdana", 20)
scoreCoins = pg.font.SysFont("Verdana", 20)
class Enemy(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load("anotherc12.png") # загружаем картинку
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w - 40), 0) # задаем рандомные координаты
    def update(self):
        global score
        self.rect.move_ip(0, enemyStep) # движение этой машинs по оси у сверху вниз
        if(self.rect.bottom > h + 90): 
            score += 1 
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
    def draw(self, surface): # рисуем машину
        surface.blit(self.image, self.rect)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("playerc12.png") # загружаем картинку
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self): # движение  машины по осям х и у с помощью 
        pressedKeys = pg.key.get_pressed()
        if self.rect.left > 0:
            if pressedKeys[pg.K_LEFT]:
                self.rect.move_ip(-step, 0)
        if self.rect.right < w:
            if pressedKeys[pg.K_RIGHT]:
                self.rect.move_ip(step, 0)
        if self.rect.top > 0:
            if pressedKeys[pg.K_UP]:
                self.rect.move_ip(0, -step)
        if self.rect.bottom < h:
            if pressedKeys[pg.K_DOWN]:
                self.rect.move_ip(0, step)        
    def draw(self, surface): # отрисовываем машину
        surface.blit(self.image, self.rect)

class Coin(pg.sprite.Sprite):
    def __init__(self, value):
        super().__init__()
        self.images = [pg.image.load("coin.png"), pg.image.load("banana12.png"), pg.image.load("cherry12.png")] # загружаем изображения монет
        self.image_index = value - 1
        self.image = self.images[self.image_index] # начальное изображение
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130)) #  координаты для монеты
        self.value = value

    def draw(self): # отрисовываем монетку
        screen.blit(self.image, self.rect)

# создаем объекты
p = Player()
e = Enemy()
c1 = Coin(1)
c2 = Coin(2)
c3 = Coin(3)

# создаем группы и добавляем туда объекты
enemies = pg.sprite.Group()
enemies.add(e)
coins = pg.sprite.Group()
coins.add(c1, c2, c3)

# запускаем основной цикл
while isRunning:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isRunning = False
    # анимируем движущийся фон
    screen.blit(pg.transform.scale(bg, (w, h)), (0, y % h))
    screen.blit(pg.transform.scale(bg, (w, h)), (0, -h + (y % h)))
    y += ry
    p.update()
    e.update()
    # условие для столкновения игровой машинки с другой машинкой
    if pg.sprite.spritecollideany(p, enemies):
        lose = True # запускаем цикл "game over"
    for coin in coins:
        coin.draw()
        if pg.sprite.collide_rect(p, coin): # если  машина получит монетку
            scoreCoin += coin.value # увеличиваем счетчик монет на значение монетки
            coin.rect.center = (random.randint(30, w - 30), random.randint(30, h - 130)) # задаем новые координаты
           
            if scoreCoin % 3 == 0: # если количество монеток кратно трем
                step += 1 # увеличиваем скорость нашей машины на 1
                enemyStep += 1 # увеличиваем скорость вражеской машины на 1
    e.draw(screen)
    p.draw(screen)
    # цикл "game over"
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        screen.blit(gameOver, (0, 0))
        pg.display.flip()

    # статус в правом верхнем углу
    counter = scoreCoins.render(f'Coins: {scoreCoin}', True, 'white')
    screen.blit(counter, (300, 10))
    pg.display.flip()
pg.quit()