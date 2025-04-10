import pygame, sys
pygame.init()

#түстер
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

#default color of pen 
color = RED

#clock 
clock = pygame.time.Clock()
FPS = 60

#screen 
wl, wh = 1001, 601
screen = pygame.display.set_mode((wl, wh))
screen.fill(WHITE)#whole screen white

#pen
pen="mouse" #default is mouse
last_event=None

pre, cur = None, None
pre_e, cur_e = None, None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
        #pen
        if event.type == pygame.KEYDOWN:#если что то нажимается на кейборде
            if event.key == pygame.K_q:
                pen="mouse"#если q, то пен меняется на мышь
            if event.key == pygame.K_w:
                pen="rectangle"#если w, то пен меняется на ректангл
            if event.key == pygame.K_e:
                pen="circle"#если е, то круг
            if event.key == pygame.K_r:
                pen="Eraser"#если r, то эрейзер

            #color
            if event.key == pygame.K_a:
                color=RED
            if event.key == pygame.K_s:
                color=GREEN
            if event.key == pygame.K_d:
                color=BLUE
            if event.key == pygame.K_f:
                color=BLACK
        
        #draw by mouse
        if pen == "mouse":
            if event.type == pygame.MOUSEBUTTONDOWN:#проверка нажатия мыши
                pre = pygame.mouse.get_pos()#начальная позиция мыши
            if event.type == pygame.MOUSEMOTION:#проверка на движение мыши
                cur = pygame.mouse.get_pos()#координаты после движения мыши
            if pre:#если нажалась мышка(если определяется начальная координата мышки)
                pygame.draw.line(screen, color, pre, cur, 1)#проводит линию между начальльной и последней точкой
                pre = cur#после первой линии, чтобы нарисовать следующую линию, начальная точка меняется на следующую после движения мыши
            if event.type==pygame.MOUSEBUTTONUP:#когда разжали мышку
                pre=None#заново определяется начальная координата
        
        #draw rectangle
        if pen == "rectangle":
            if event.type==pygame.MOUSEBUTTONDOWN:#проверка нажатия мыши
                x, y = pygame.mouse.get_pos()#начальная позиция мыши
                last_event="press"#мышь нажата
            if event.type==pygame.MOUSEBUTTONUP:#мышь разжата
                x1, y1 = pygame.mouse.get_pos()#координата места, где разжали
                last_event="not press"#мышь разжата
            if last_event=="not press":#если нажатие на мышь прекратилось
                #pygame.draw.rect(screen, color, (int(x), int(y), int(x1)-int(x), int(y1)-int(y) ))#это для закрашенного прямоугольника
                pygame.draw.line(screen, color, (x, y), (x1, y), 1)
                pygame.draw.line(screen, color, (x,y), (x, y1), 1)
                pygame.draw.line(screen, color, (x, y1), (x1, y1), 1)
                pygame.draw.line(screen, color, (x1, y), (x1, y1), 1)
                last_event=None
                
        #draw circle
        if pen == "circle":
            if event.type==pygame.MOUSEBUTTONDOWN:#если мышь зажата
                x, y = pygame.mouse.get_pos()#начальная координата
                last_event="press"#мышь зажата
            if event.type==pygame.MOUSEBUTTONUP:#мышь разжата
                x1, y1 = pygame.mouse.get_pos()#координата места, где разжали
                last_event="not press"#мышь разжата
            if last_event=="not press":#если нажатие на мышь прекращается
                pygame.draw.circle(screen, color, (((x+x1)//2), ((y+y1)//2)), abs((x1-x)/2))#рисует круг
                pygame.draw.circle(screen, WHITE, (((x+x1)//2), ((y+y1)//2)), abs((x1-x)/2)-0.5)#белый цвет чистит окрашенный круг
                last_event=None
                
        #Eraser
        if pen == "Eraser":
            if event.type == pygame.MOUSEBUTTONDOWN:#проверка на нажатие мыши
                pre_e = pygame.mouse.get_pos()#начальная координата мыши
            if event.type == pygame.MOUSEMOTION:#проверка на движение мыши
                cur_e = pygame.mouse.get_pos()#координата после движения мыши
            if pre_e:
                pygame.draw.line(screen, WHITE, pre_e, cur_e, 10)#рисуем линию толщиной 10
                pre_e=cur_e
            if event.type == pygame.MOUSEBUTTONUP:
                prev1 = None


    clock.tick(FPS)       
    pygame.display.flip()