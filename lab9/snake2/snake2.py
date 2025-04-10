import pygame as pg 
from random import randrange, choice
pg.init()

# переменные
w, h, fps, level, step = 800, 800, 10, 0, 40 
screen = pg.display.set_mode((w, h))
isRunning, lose = True, False
clock = pg.time.Clock()
score = pg.font.SysFont("Verdana", 20)
surf = pg.Surface((390, 390), pg.SRCALPHA)
background = pg.image.load("background.jpg")
background = pg.transform.scale(background, (w, h))
gameover = pg.image.load("gameover.jpg")
gameover = pg.transform.scale(gameover, (390, 390))

class Food:
    def __init__(self, pic):
        self.pic = pic
        self.value = 0
        self.time_to_appear = fps * 5  # каждая монетка появляется каждые 5 секунд
        self.timer = self.time_to_appear

        # Задаем рандомные координаты для еды в диапазоне игрового поля 
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.randomize_value()

    def draw(self):
        screen.blit(self.pic, (self.x, self.y))
    
    def draw2(self):
        self.x = randrange(0, w, step)
        self.y = randrange(0, h, step)
        self.randomize_value()

    def randomize_value(self):
        self.value = choice([1, 2, 3])

    def update(self):
        if self.timer <= 0:
            self.draw2()
            self.timer = self.time_to_appear
        else:
            self.timer -= 1

class Snake:
    def __init__(self):
        self.speed = step
        self.body = [[360, 360]] # изначальные координаты головы
        self.dx = 0
        self.dy = 0
        self.score = 0
        self.color = 'red'

    def move(self, events):
        for event in events:
            if event.type == pg.KEYDOWN: # движение змейки по нажатию 
                if event.key == pg.K_LEFT and self.dx == 0: 
                    self.dx = -self.speed
                    self.dy = 0
                if event.key == pg.K_RIGHT and self.dx == 0:
                    self.dx = self.speed
                    self.dy = 0
                if event.key == pg.K_UP and self.dy == 0:
                    self.dx = 0
                    self.dy = -self.speed
                if event.key == pg.K_DOWN and self.dy == 0:
                    self.dx = 0
                    self.dy = self.speed

        # передвигаем части тела змейки по oсям х и у на предыдущие координаты
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0] 
            self.body[i][1] = self.body[i - 1][1]

        # передвигаем голову змейки по осям х и у на следующие координаты
        self.body[0][0] += self.dx 
        self.body[0][1] += self.dy 
    
    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], step, step))
    
    # проверяем когда змейка съедает еду
    def collideFood(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y: # если координаты головы змейки совпадают с координатами еды
            self.score += f.value
            self.body.append([1000, 1000]) 
            f.draw2()

    # заканчиваем игру, если голова змейки столкнеться со своим телом
    def selfCollide(self):
        global isRunning
        if self.body[0] in self.body[1:]: # если голова змейки и входит в массив координат тела змейки
            lose = True # запускаем цикл 'game over' 

    # проверяем чтобы еда не оказалась на теле змейки
    def checkFood(self, f:Food): 
        if [f.x, f.y] in self.body: # если координаты еды входят в массив координат тела змейки
            f.draw2() # заново рисуем еду

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pic = pg.image.load("block.png")
    
    def draw(self):
        screen.blit(self.pic, (self.x, self.y))

# создаем объекты змейки и еды
s = Snake()
f1 = Food(pg.image.load("coin.png"))  # первая монетка
f2 = Food(pg.image.load("banana12.png"))  # вторая монетка
f3 = Food(pg.image.load("cherry12.png"))  # третья монетка

# запускаем основной цикл
while isRunning:
    clock.tick(fps)
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            isRunning = False
    screen.blit(background, (0, 0))

    # прорисовываем стенки с помощью заранее написанных паттернов  
    myWalls = open(f'wall{level}.txt', 'r').readlines() # читает каждую линию как отдельный лист
    walls = []
    for i, line in enumerate(myWalls): # проходимся по индексу и строке
        for j, each in enumerate(line): # проходимся по каждому элементу в строке
            if each == "+":
                walls.append(Wall(j * step, i * step)) # добавляем каждый блок стенки в лист

    # вызываем методы классов
    f1.draw()
    f2.draw()
    f3.draw()
    s.draw()
    s.move(events) # нажать любую клавишу чтобы начать игру
    s.collideFood(f1)
    s.collideFood(f2)
    s.collideFood(f3)
    s.selfCollide()
    s.checkFood(f1)
    s.checkFood(f2)
    s.checkFood(f3)

    # Обновляем состояние монеток
    f1.update()
    f2.update()
    f3.update()

    # баллы 
    counter = score.render(f'Score - {s.score}', True, 'white')
    screen.blit(counter, (550, 50))
    
    # стены на экран
    for wall in walls:
        wall.draw()
        if s.body[0][0] == wall.x and s.body[0][1] == wall.y: # останавливаем игру, если голова змейки столкнеться со стенкой
            lose = True
    
    # запускаем цикл 'game over'
    while lose:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False
                lose = False   

        surf.blit(gameover, (0, 0))
        screen.blit(surf, (200, 200))
        cntr = score.render(f'Your score is {s.score}', True, 'black')
        screen.blit(cntr, (320, 480))
        l = score.render(f'Your level is {level}', True, 'black')
        screen.blit(l, (320, 510))
        pg.display.flip()
    pg.display.flip()

pg.quit()