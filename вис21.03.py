import pygame as pg
import random
class Window:
    width = 640
    height = 480
    centr_x = width/2
    centr_y = height/2

FPS=30

NULL = 0
WRONG = 1
RIGHT = 2

pg.init()
screen=pg.display.set_mode ((Window.width, Window.height))
clock=pg.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 200)
screen.fill(WHITE)

keys = {102:'а', 44:'б', 100:'в', 117:'г', 108:'д', 116:'е', 59:'ж', \
        112:'з', 98:'и', 114:'к', 107:'л', 118:'м', 121:'н', 106:'о',\
        104:'р', 99:'с', 110:'т', 101:'у', 97:'ф',  91:'х',  105:'ш', \
        39:'э',  46:'ю', 112:'я', 103:'п'}

Word3 = ['кот','ток','бок','зуб','дом','сыр']
a = 'мама'#random.choice(Word3)
print (a)

font1 = pg.font.SysFont("serif", 36)
font2 = pg.font.SysFont("serif", 45)
text1 = font1.render("Введите букву", True, BLACK)
text2 = font1.render("Этой буквы нет", True, BLACK)

is_game_over = False
choice = NULL
counter = 0
increase = NULL
user_symbols = []
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    list_events = pg.event.get()
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            l = keys[event.key]
            spots = []
            print (event.key, l)
            
            for i, s in enumerate(a):
                if l == s:
                    spots.append(i)
                    user_symbols.append(i)
                    
            if len(spots) > 0: choice = RIGHT
            else: choice = WRONG
            
            if len(spots) == 0:
                counter=counter+1
                print(counter)
            
            print(spots)
            

    if choice == WRONG:
        screen.blit(text2, (Window.centr_x-60, 370))
        if counter >= 1: pg.draw.rect(screen, BLUE, (50, 50, 50, 5))
        if counter >= 2: pg.draw.rect(screen, BLUE, (100, 50, 5, 50))
        if counter >= 3: pg.draw.circle(screen, BLUE, (102, 120), 20, 5)
        if counter >= 4: pg.draw.rect(screen, BLUE, (100, 140, 5, 85))
        if counter >= 5:
            pg.draw.line(screen, BLUE, (102, 160),(80, 190), 5)
            pg.draw.line(screen, BLUE, (102, 160),(120, 190),5)
        if counter >= 6:
            pg.draw.line(screen, BLUE, (102, 225),(80, 275), 5)
            pg.draw.line(screen, BLUE, (102, 225),(120, 275),5)
        if counter >= 7:
            is_game_over = True

    if is_game_over == True:
        text4 = font2.render("Вы проиграли", True, RED)
        screen.blit(text4, (Window.centr_x-100, Window.centr_y-30))
#         for i in enumerate(a):
#             text3 = font1.render(a[i], True, BLACK)
#             screen.blit(text3, (72+i*100, 310))
            

    for j in user_symbols:
        text3 = font1.render(a[j], True, BLACK)
        screen.blit(text3, (72+j*100, 310))
            
    for n, _ in enumerate(a):
        pg.draw.rect(screen, BLACK, (70+n*100, 350, 50, 5))
            
    
    pg.draw.rect(screen, BLUE, (50, 50, 5, 250)) #вертикальная полоска
    pg.draw.rect(screen, BLUE, (50, 300, 50, 5)) #горизонтальная полоска
    screen.blit(text1, (Window.centr_x-50, 10))
    pg.display.update()
    
pg.quit()