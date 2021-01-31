import pygame
import sys
import random
import pygame as pg

# здесь определяются константы,
# классы и функции
FPS = 60
# random.randint()
window_size = (400, 600)

# здесь происходит инициация,
# создание объектов
pygame.init()
pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()


class TubeDown(pg.sprite.Sprite):
    def __init__(self, y, len_y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.position = y - len_y


tube_down = TubeDown(tube_y, len_y)


class TubeUp(pg.sprite.Sprite):
    def __init__(self, y, len_y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.position = y + len_y


tube_up = TubeUp(tube_y, len_y)


class Bird(pg.sprite.Sprite):
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("bird.png").convert_alpha()
        self.position = x


bird = Bird(window_size[0]//2)


# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # --------
    # изменение объектов
    # --------

    # обновление экрана
    pygame.display.update()
