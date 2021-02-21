import pygame as pg
import random
class Window:
    width = 640
    height = 480
    centr_x = width/2
    centr_y = height/2

FPS=30

pg.init()
screen=pg.display.set_mode ((Window.width, Window.height))
clock=pg.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 200)
screen.fill(WHITE)

font1 = pg.font.SysFont("serif", 36)
text1 = font1.render("текст", True, BLACK)
screen.blit(text1, (10, Window.centr_x))

keys = {102:'а', 44:'б', 100:'в', 117:'г', 108:'д', 116:'е', 59:'ж', \
        112:'з', 98:'и', 114:'к', 107:'л', 118:'м', 121:'н', 106:'о',\
        104:'р', 99:'с', 110:'т', 101:'у', 97:'ф',  91:'х',  105:'ш', \
        39:'э',  46:'ю', 112:'я', 103:'п'}

Word3 = ['кот','ток','бок','зуб','дом','сыр']
a = 'мама'#random.choice(Word3)
print (a)

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    list_events = pg.event.get()
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            l=keys[event.key]
            print (l)
            spots = []
            for i, s in enumerate(a):
                if l==s:
                    print (1)
                    spots.append(i)
                else: print (0)
            print(spots)

    pg.draw.rect(screen, BLUE, (50, 50, 5, 250))
    pg.draw.rect(screen, BLUE, (50, 300, 50, 5))
#     pg.draw.rect(screen, BLACK, (70, 350, 50, 5))
#     pg.draw.rect(screen, BLACK, (170, 350, 50, 5))
#     pg.draw.rect(screen, BLACK, (270, 350, 50, 5))
    screen.blit(text1, (Window.centr_x, 10))
    pg.display.update()
    if i ==1: pg.draw.rect(screen, BLACK, (70, 350, 50, 5)) 
pg.quit()