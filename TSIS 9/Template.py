import pygame as pg
import datetime
pg.init()
size = [500, 500]
center = [250, 250]
screen = pg.display.set_mode(size)
clock = pg.time.Clock()



running = True
while running:





    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    clock.tick(30)

pg.quit()