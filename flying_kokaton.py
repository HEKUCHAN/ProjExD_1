import os
import sys

import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    screen_rect = screen.get_rect()

    clock = pg.time.Clock()

    bg_img = pg.image.load("fig/pg_bg.jpg")
    fliped_bg_img = pg.transform.flip(bg_img, True, False)

    kokaton_img = pg.transform.scale(
        pg.transform.flip(pg.image.load("fig/3.png"), True, False), (60, 60)
    )
    koukaton_rect = kokaton_img.get_rect()

    # 中央にこうかとんを配置
    koukaton_rect.center = screen_rect.center

    # 背景の流れるスピード
    bg_speed = 1

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
        up, down = key_lst[pg.K_UP], key_lst[pg.K_DOWN]
        right, left = key_lst[pg.K_RIGHT], key_lst[pg.K_LEFT]
        dx = right - left
        dy = down - up

        if key_lst[pg.K_RIGHT]:
            dx += 1
            bg_speed = 2
        elif key_lst[pg.K_LEFT]:
            dx -= 1
            bg_speed = 2
        else:
            dx -= 1
            bg_speed = 1

        # こうかとんを計算した位置に移動
        koukaton_rect.move_ip(dx, dy)

        # こうかとんが画面からはみ出ないように制限
        koukaton_rect.clamp_ip(screen_rect)

        pg.display.update()
        tmr += bg_speed
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
