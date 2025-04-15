import pygame
import random
import psycopg2
pygame.init()

#color
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW =(255, 215, 0)

#clock
clock = pygame.time.Clock()
FPS = 10
BlackFood = 10*FPS+1  # my time it is just cnt by FPS  10*FPS=10s

#screen
l, w = 1001, 601
screen = pygame.display.set_mode((l,w))
running = True
x_axis, y_axis = 0, 0
Value = 20
body = [[10, 10]]
snake_len=1
wall = []
wall_len = 0
kill_condition = False
last_key = str("")

#value
level_value = 1
score_value = 0
record = 0

#fonts
font = pygame.font.SysFont("Verdana", 24)
font_Gameover = pygame.font.SysFont("Verdana", 72)
text4 = font.render("Game Over", True, WHITE,)


#cordinate randomiser
def random_c():
    x_value = random.randrange(10, l-10)
    y_value = random.randrange(10, w-10)
    x1, y1 = 10 * round(x_value / 10), 10 * round(y_value /10)
    condition = True
    for i in range(len(body)):
        if body[i][0]==x1 and body[i][1] == y1:
            condition = False
            break
    if level_value == 1:
        for i in range(100,400):
            if x1 == 300 and y1 == i:
                condition = False
                break
    if condition == True:
        return x1, y1
    else:
        x1, y1 = random_c()
        return x1, y1

food_x, food_y = random_c()
BlackFoodx, BlackFoody = random_c()

def kill_by_yourself():
    global kill_condition
    for i in range(1,len(body)):
        if body[0][0] == body[i][0] and body[0][1] == body[i][1]:
            kill_condition = True
            break
    return kill_condition
    

def tall_wall_kill():
    global kill_condition
    for i in range(200,701):
        if body[0][0] == i and body[0][1] == 300:
            kill_condition = True
            break
        if body[0][0] == i and body[0][1] == 500:
            kill_condition = True
            break
        
    return kill_condition

def wall_kill():  
    global kill_condition
    for i in range(len(wall)):
        if body[0][0] == wall[i][0] and body[0][1] == wall[i][1]:
            kill_condition = True
            break

    return kill_condition
   
#SQL
conn = psycopg2.connect(
	database="postgres",
	user='postgres',
	password='2305',
	host='localhost',
)
con = conn.cursor()
conn.autocommit = True

login_name = str(input('Name: '))
sql = f"select * from snakedata where the_user =\'{login_name}\'"
con.execute(sql)
info = con.fetchall()

if len(info) > 0:
    print("Continue")
    score_value = info[0][1]
    level_value = info[0][2]
    FPS = info[0][3]
    snake_len = int(info[0][4])
    wall_len = int(info[0][5])
    body[0][0] = int(info[0][6])
    body[0][1] = int(info[0][7])
    x_axis = -10
    record = info[0][8]
    for i in range(1,snake_len):
        body.append([-i*200,-i*200])
    for j in range(wall_len):
        food_x2, food_y2 = random_c()
        wall.append([food_x2, food_y2])
    print(body)

else:
    print("Create a new account")
    sql_insert = f"INSERT INTO snakedata(the_user, last_score, last_level, last_FPS, snake_len, wall_len, snake_x, snake_y, record) VALUES( \'{login_name}\',\'{score_value}\',\'{level_value}\',\'{FPS}\', \'{snake_len}\', \'{wall_len}\',\'{body[0][0]}\', \'{body[0][1]}\', \'{record}\' )"
    con.execute(sql_insert)


def game_over():
    global running
    global sql_insert1
    global score_value
    global record
    screen.fill(BLACK)
    screen.blit(scoretext, (850,5))
    screen.blit(leveltext, (850,35))
    screen.blit(fpstext, (850,65))
    screen.blit(text4, (425,225))
    sql_insert1 = f"UPDATE snakedata set  last_score = 0, last_level = 1, last_FPS = 10, snake_len = 1, wall_len = 0, snake_x=10, snake_y=10  where the_user = \'{login_name}\' "
    con.execute(sql_insert1)
    if score_value > record:
        sql_insert1 = f"UPDATE snakedata set record = \'{score_value}\'  where the_user = \'{login_name}\' "
        record = score_value
        con.execute(sql_insert1)
  
#main
while running:
    wall_len = len(wall)
    snake_len=len(body)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and last_key!="K_LEFT":
                x_axis = 10
                y_axis = 0
                last_key = "K_RIGHT"
            if event.key == pygame.K_LEFT and last_key!="K_RIGHT":
                x_axis = -10
                y_axis = 0
                last_key = "K_LEFT"
            if event.key == pygame.K_UP and last_key!="K_DOWN":
                x_axis = 0
                y_axis = -10
                last_key = "K_UP"
            if event.key == pygame.K_DOWN and last_key!="K_UP":
                x_axis = 0
                y_axis = 10
                last_key = "K_DOWN"
    #records
    scoretext = font.render("Score: "+str(score_value), True, BLACK)
    leveltext = font.render("Level: "+str(level_value), True, BLACK)
    fpstext = font.render("FPS: "+str(FPS), True, BLACK)
    recordtext = font.render("Record: "+str(record), True, BLACK)

    #eating
    if body[0][0]==food_x and body[0][1]==food_y:
        food_x, food_y = random_c()
        body.append([0, 0])
        score_value += 10
        BlackFood = 10*FPS +1
    #eating Blsck food
    elif body[0][0]==BlackFoodx and body[0][1]== BlackFoody:
        body.append([0, 0])
        score_value += 30
        BlackFood = 10*FPS+1

    #level
    last_level = level_value
    level_value = 1 + score_value //50
    #body change
    for i in range(len(body) - 1, 0, -1):
        body[i][0] = body[i - 1][0]
        body[i][1] = body[i - 1][1]
    #return to screen
    if body[0][0] > l-11:
        body[0][0] = 10
    if body[0][1] > w-11:
        body[0][1] = 10
    if body[0][1] < 10:
        body[0][1] = w-11
    if body[0][0] < 10:
        body[0][0] = l-11
    
    #body coordination
    body[0][0] += x_axis
    body[0][1] += y_axis

    # main screen     
    screen.fill(YELLOW)

    # Draw score level FPS
    screen.blit(scoretext, (850,480))
    screen.blit(leveltext, (850,510))
    screen.blit(fpstext, (850,540))
    screen.blit(recordtext, (850,570))

    # Draw food
    pygame.draw.rect(screen, WHITE, (food_x - 0, food_y - 0, Value, Value))
    if BlackFood == 0:
        BlackFoodx, BlackFoody = random_c()
    if BlackFood <= 10*FPS:
        pygame.draw.rect(screen, BLACK, (BlackFoodx - 0, BlackFoody - 0, Value , Value ))
        BlackFood += 1
    if BlackFood > 10*FPS:
        BlackFoodx, BlackFoody = -100, -100

    # Draw snake body
    for i, (x, y) in enumerate(body):
        if i!=0:
            #pygame.draw.circle(screen, GREEN, (x, y), Value)
            pygame.draw.rect(screen, BLACK, (x, y, Value, Value))

    # Draw snake head

    pygame.draw.rect(screen, BLACK, (body[0][0], body[0][1], Value, Value))
    
    #level 1
    if level_value == 1:
        pygame.draw.line(screen, BLACK, (200,300),(701,300), 20)
        pygame.draw.line(screen, BLACK,(200,500),(701,500),20)
      
        if tall_wall_kill() == True:
            print("You died")
            game_over()

    # add wall circle & add FPS next level
    if last_level != level_value:
        FPS += 3
        food_x2, food_y2 = random_c()
        wall.append([food_x2, food_y2])
        BlackFood = 0

    if level_value > 1:
        for i in range(len(wall)):
            pygame.draw.circle(screen, BLUE, (wall[i][0]-0, wall[i][1]-0), Value-10 )
         
        if wall_kill()== True:
            print("You died")
            game_over()
    
    # Kill yourself
    if kill_by_yourself()==True:
        print("You died.")
        game_over
        
    pygame.display.flip()
    clock.tick(FPS)
conn.commit()
pygame.quit()