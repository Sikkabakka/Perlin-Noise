import pygame as pg
from noise_maker import Noise_maker, Pixel

pg.init()

pixels = 40
box_size = 1
grid_size = 10
padding = 40
screen = pg.display.set_mode((pixels * box_size * grid_size + padding, pixels*box_size *grid_size + padding))

running = True

draw_arrows = False

noise_maker = Noise_maker(grid_size, pixels)
map = noise_maker.make_map()
# noise_maker.check_grid()
def draw_arrow(direction, position, size =1):

    pg.draw.line(screen, (255, 0, 0), (position[0]* pixels + padding/2, position[1]*pixels + padding/2), (position[0]* pixels + padding/2 + direction[0]*10, position[1]*pixels + padding/2+direction[1]*10), 3)


while running:
    for event in pg.event.get():    
        if event.type == pg.QUIT:
            running = False
    position = [0, 0, 0, 0]


    for y, row in enumerate(map):
        for x, tile in enumerate(row):

            for i, pixel_row in enumerate(tile):
                for j, pixel in enumerate(pixel_row):

                    pixel_value = pixel.value
                    pixel_value += 1
                    if pixel_value > 2:
                        pixel_value = 2
                    elif pixel_value < 0:
                        pixel_value = 0
                    

                    # if pixel.pixel_count[0] == 39 and pixel.pixel_count[1] == 1:
                    #     print(pixel.value, "top_right", x, y)
                    #     print(pixel.corners, "Parents")
                    # if pixel.pixel_count[0] == 1 and pixel.pixel_count[1] == 1:
                    #     print(pixel.value, "top_left", x, y)
                    #     print(pixel.corners, "Parents")



                    color_value = round(255 / 2 * pixel_value)
                    screen.set_at((x * pixels+ padding//2 + j , y * pixels + padding//2 + i), (color_value, color_value, color_value))
    if draw_arrows:
            
        for y, row in enumerate(noise_maker.grid_vectors):
            for x, direction in enumerate(row):
                draw_arrow(direction, (x, y))


    pg.display.update()    
pg.quit()