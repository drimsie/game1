import pygame_textinput
import pygame as pg
class Window:
    width =640
    height = 480
    centr_x = width/2
    centr_y = height/2

FPS=30

pg.init()
textinput=pg.textinput.TextInput()
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

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    list_events = pg.event.get()
    for event in list_events:
        if event.type == pg.QUIT:
            running = False
    textinput.update(list_events)
    pg.draw.rect(screen, BLUE, (50, 50, 5, 250))
    pg.draw.rect(screen, BLUE, (50, 300, 50, 5))
    screen.blit(text1, (Window.centr_x, 10))
    screen.blit(textinput.get_surface() (Window.centr_x, 400))
    pg.display.update()
    
pg.quit()