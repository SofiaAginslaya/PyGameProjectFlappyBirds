import pygame
import sys
import random
import pygame as pg


FPS = 60
# random.randint()
window_size = (600, 700)
screen = pg.display.set_mode(window_size)

game_speed = 5

coins = -1

pygame.init()
pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

filename = "bird.png"
filename_tube = "tube.png"
filename_tube_up = "tube_up.png"

pygame.display.update()

tube_y = 6000
len_y = 100


class TubeDown(pg.sprite.Sprite):
    def __init__(self, y, len_y):
        pg.sprite.Sprite.__init__(self)
        self.x = window_size[0]
        self.image = pg.image.load(filename_tube).convert_alpha()
        self.positiony = y + len_y
        self.rect = self.image.get_rect(
            center=(self.x, self.positiony))

    def update(self):
        if self.rect.x <= -110:
            self.rect.x = window_size[0]
        else:
            self.rect.x = self.rect.x - game_speed


class TubeUp(pg.sprite.Sprite):
    def __init__(self, y, len_y):
        pg.sprite.Sprite.__init__(self)
        self.x = window_size[0]
        self.image = pg.image.load(filename_tube_up).convert_alpha()
        self.positiony = y - len_y
        self.rect = self.image.get_rect(
            center=(self.x, self.positiony - 1189))

    def update(self):
        if self.rect.x <= -110:
            self.rect.x = window_size[0]
            self.rect.y = random.randint(250, 650) - len_y
            tube_down.rect.y = self.rect.y + len_y
            self.rect.y = self.rect.y - 1189  # труба очень большая, и я не знаю, как определить не центр трубы,
            # а ее верхушки
            # print(f"РАЗНИЦА: {abs(self.rect.y)} - {tube_down.rect.y}", self.rect.y - tube_down.rect.y)
        else:
            self.rect.x = self.rect.x - game_speed


class Bird(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=(window_size[0] // 2, window_size[1] // 2))


bird = Bird()
tube_down = TubeDown(tube_y, len_y)
tube_up = TubeUp(tube_y, len_y)

jump_cold = -1

# текст / шрифты

coins_font = pygame.font.Font(None, 72)
text_coins = coins_font.render("0", True, (255, 255, 51))

title_font = pygame.font.Font(None, 144)
text_title = title_font.render("Flappy Bird", True, (100, 100, 200))

lost_font = pygame.font.Font(None, 72)
text_lost = lost_font.render("Проиграл!", True, (50, 150, 200))

score_font = pygame.font.Font(None, 72)
text_score = score_font.render("Монет: " + str(coins), True, (50, 150, 200))

while_change = 0

# Начальное меню
while while_change == 0:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                while_change = 1

    screen.blit(bird.image, bird.rect)

    screen.blit(text_title, (15, 50))

    pygame.display.update()
while_change = 0
while True:
    # игра
    while while_change == 0:

        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump_cold = 15

        if bird.rect.y > window_size[1] - 60:
            while_change = 1
        elif bird.rect.colliderect(tube_up.rect) or bird.rect.colliderect(tube_down):
            while_change = 1
        elif tube_up.rect.x + 4 == bird.rect.x:
            coins += 1
            text_coins = coins_font.render(str(coins), True, (255, 255, 51))

        if jump_cold >= 0:
            jump_cold = jump_cold - 1
            bird.rect.y -= 5
        elif jump_cold <= -10:
            jump_cold = jump_cold - 1
            bird.rect.y = bird.rect.y + 10
        elif jump_cold < 0 and jump_cold > -10:
            jump_cold = jump_cold - 1
            bird.rect.y = bird.rect.y + 6

        tube_down.update()
        tube_up.update()

        # отображение всех объектов

        screen.blit(tube_down.image, tube_down.rect)
        screen.blit(tube_up.image, tube_up.rect)
        screen.blit(bird.image, bird.rect)
        screen.blit(text_coins, (10, 50))
        pygame.display.update()

    while_change = 0
    jump_cold = 250
    text_score = score_font.render("Монет: "+str(coins), True, (150, 150, 255))

    # экран после смерти
    while while_change == 0:
        clock.tick(FPS)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jump_cold < 220:
                    while_change = 1

        if jump_cold > 0:
            bird.rect.y = bird.rect.y + 10

        jump_cold = jump_cold - 1

        screen.blit(tube_down.image, tube_down.rect)
        screen.blit(tube_up.image, tube_up.rect)
        screen.blit(bird.image, bird.rect)
        screen.blit(text_lost, (10, 50))
        screen.blit(text_score, (10, 200))

        pygame.display.update()
    while_change = 0
    coins = -1
    tube_up.__init__(tube_y, len_y)
    tube_down.__init__(tube_y, len_y)
    bird.__init__()
    text_coins = coins_font.render("0", True, (255, 255, 51))
    jump_cold = 0
