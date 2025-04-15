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
    kokaton_img = pg.transform.scale(
        pg.transform.flip(pg.image.load("fig/3.png"), True, False), (60, 60)
    )
    koukaton_rect = kokaton_img.get_rect()
    koukaton_rect.center = 300, 200

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        x_offset = -(tmr % bg_img.get_width() * 2)

        screen.blit(bg_img, [x_offset, 0])
        screen.blit(fliped_bg_img, [x_offset + bg_img.get_width(), 0])
        screen.blit(bg_img, [x_offset + bg_img.get_width() * 2, 0])

        screen.blit(kokaton_img, koukaton_rect)

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            if koukaton_rect.top > 0:
                koukaton_rect.move_ip(0, -1)
            else:
                koukaton_rect.top = 0
        if key_lst[pg.K_DOWN]:
            if koukaton_rect.bottom < screen.get_height():
                koukaton_rect.move_ip(0, 1)
            else:
                koukaton_rect.bottom = screen.get_height()
        if key_lst[pg.K_LEFT]:
            if koukaton_rect.left > 0:
                koukaton_rect.move_ip(-1, 0)
            else:
                koukaton_rect.left = 0
        if key_lst[pg.K_RIGHT]:
            if koukaton_rect.right < screen.get_width():
                koukaton_rect.move_ip(1, 0)
            else:
                koukaton_rect.right = screen.get_width()

        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
    sys.exit()
