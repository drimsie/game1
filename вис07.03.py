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
text1 = font1.render("текст", True, BLACK)
screen.blit(text1, (10, Window.centr_x))
text2 = font1.render("этой буквы нет", True, BLACK)
text3 = font1.render("да", True, BLACK)


choose = NULL
user_symbols = []
quantity = [] #сделать так, чтоб считалось кол-во букв. типа если на этом месте что-то есть,  то есть
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
            print (event.key)
            
            for i, s in enumerate(a):
                if l == s:
                    spots.append(i)
                    user_symbols.append(i)
                    
            if len(spots) > 0: choose = RIGHT
            else: choose = WRONG
            
            print(spots)

    if choose == WRONG:
        screen.blit(text2, (Window.centr_x-60, 300))
    
    for j in user_symbols:
            text_ = font1.render(a[j], True, BLACK)
            screen.blit(text_, (400+j*30, 350))
            
            
            
    q = len(quantity)
    n = 0
    
    while n < q:
        pg.draw.rect(screen, BLACK, (70, 350, 50, 5))
        n = n+1 #создать перемеенную, которая будет изменять полжение 
            
            
    
    pg.draw.rect(screen, BLUE, (50, 50, 5, 250))
    pg.draw.rect(screen, BLUE, (50, 300, 50, 5))
#     pg.draw.rect(screen, BLACK, (70, 350, 50, 5))
#     pg.draw.rect(screen, BLACK, (170, 350, 50, 5))
#     pg.draw.rect(screen, BLACK, (270, 350, 50, 5))
    screen.blit(text1, (Window.centr_x, 10))
    pg.display.update()
#     pg.draw.rect(screen, BLACK, (70, 350, 50, 5)) 
pg.quit()