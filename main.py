import pygame as pg
from noise_maker import Noise_maker

pg.init()

pixels = 100
screen = pg.display.set_mode((pixels, pixels))

running = True

noise_maker = Noise_maker(5, pixels)
map = noise_maker.make_map()
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    for i in range(pixels-1):
        for j in range(pixels-1):
            screen.set_at((j, i), (255/2,255/2,255/2))

pg.display.update()    
pg.quit()