import pygame as pg
from noise_maker import Noise_maker

pg.init()

pixels = 40
box_size = 1
grid_size = 10
screen = pg.display.set_mode((pixels * box_size * grid_size, pixels*box_size *grid_size))

running = True

noise_maker = Noise_maker(grid_size, pixels)
map = noise_maker.make_map()
# noise_maker.check_grid()
def draw_arrow(direction, position, size =1):
    pg.draw.rect(screen, "red", ())

while running:
    for event in pg.event.get():    
        if event.type == pg.QUIT:
            running = False
    position = [0, 0, 0, 0]


    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            for i, pixel_row in enumerate(tile):
                for j, pixel in enumerate(pixel_row):
                    pixel += 1
                    if pixel > 2:
                        pixel = 2
                    elif pixel < 0:
                        pixel = 0 
                    color_value = round(255 / 2 * pixel)

                    screen.set_at((x * pixels + j, y * pixels + i), (color_value, color_value, color_value))

            



    pg.display.update()    
pg.quit()