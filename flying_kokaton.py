import os
import sys

import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    fliped_bg_img = pg.transform.flip(bg_img, True, False)
    kokaton_img = pg.transform.flip(pg.image.load("fig/3.png"), True, False)

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        x_offset = -(tmr % bg_img.get_width() * 2)

        screen.blit(bg_img, [x_offset, 0])
        screen.blit(fliped_bg_img, [x_offset + bg_img.get_width(), 0])
        screen.blit(bg_img, [x_offset + bg_img.get_width() * 2, 0])

        screen.blit(kokaton_img, [300, 200])

        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    sys.exit()
