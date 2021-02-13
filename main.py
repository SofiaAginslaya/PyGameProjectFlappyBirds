import pygame
import sys
import random
import pygame as pg


FPS = 60
# random.randint()
window_size = (600, 700)
sc = pg.display.set_mode(window_size)

game_speed = 5

coins = -1
file_coins = open('coins.txt', 'r')
all_coins = int(file_coins.read())
file_coins.close()

pygame.init()
pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

filename = "bird.png"
filename_tube = "tube.png"
filename_tube_up = "tube_up.png"
filename_plate = "pol.png"
filename_ttf = "font.ttf"

skins = ["bird.png", "bird1.png", "bird2.png", "bird3.png"]
prices = [0, 10, 15, 20]

pygame.display.update()

tube_y = 6000
len_y = 100


def show_intro():
    fon_image = pygame.transform.scale(pygame.image.load("ground.png"), window_size)
    sc.blit(fon_image, (0, 0))


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
            self.rect.y = self.rect.y - 1189    # Труба очень большая, и я не знаю как поределить не центр трубы, а её
            # верхушку
            # print(f"РАЗНИЦА: {abs(self.rect.y)} - {tube_down.rect.y}", self.rect.y - tube_down.rect.y)
        else:
            self.rect.x = self.rect.x - game_speed


class Bird(pg.sprite.Sprite):
    def __init__(self, filename=filename):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(
            center=(window_size[0] // 2, window_size[1] // 2))


class Plate(pg.sprite.Sprite):
    def __init__(self, x):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename_plate).convert_alpha()
        self.rect = self.image.get_rect(
            center=(x, window_size[1] + 200))


plate1 = Plate(0)
plate2 = Plate(window_size[0] + 680)
bird = Bird()
bird_example = Bird()
tube_down = TubeDown(tube_y, len_y)
tube_up = TubeUp(tube_y, len_y)

jump_cold = -1

# текст / шрифты

coins_font = pygame.font.Font(filename_ttf, 72)
text_coins = coins_font.render("0", True, (255, 255, 51))

title_font = pygame.font.Font(filename_ttf, 70)
text_title = title_font.render("Flappy Bird", True, (50, 200, 50))

lost_font = pygame.font.Font(filename_ttf, 60)
text_lost = lost_font.render("Проиграл!", True, (50, 150, 200))

score_font = pygame.font.Font(filename_ttf, 60)
text_score = score_font.render("Монет: " + str(coins), True, (50, 150, 200))

shop_font = pygame.font.Font(filename_ttf, 25)
text_shop = shop_font.render("Магазин (кнопка 'S')", True, (50, 150, 200))

buy_font = pygame.font.Font(filename_ttf, 25)
text_buy = buy_font.render("Купить скин  (кнопка 'B')", True, (50, 200, 20))

price_font = pygame.font.Font(filename_ttf, 35)
text_price = price_font.render("Цена: " + "0", True, (50, 200, 20))

menu_font = pygame.font.Font(filename_ttf, 35)
text_menu = menu_font.render("Меню  (кнопка 'M')", True, (50, 200, 20))

while_change = 0

while True:
    # Начальное меню
    while_change_game = 0
    while while_change == 0:
        clock.tick(FPS)
        sc.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    while_change = 1
                elif event.key == pygame.K_s:
                    coins_font = pygame.font.Font(filename_ttf, 25)
                    text_coins = coins_font.render(str(all_coins), True, (255, 255, 51))
                    text_title = title_font.render("Магазин", True, (50, 200, 50))
                    text_shop = shop_font.render("Выйти (кнопка 'E')", True, (50, 150, 200))
                    skin = 0
                    price = 0

                    while while_change == 0:
                        clock.tick(FPS)
                        sc.fill((0, 0, 0))

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                sys.exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_e:
                                    while_change = 1
                                elif event.key == pygame.K_b:
                                    if price > all_coins:
                                        pass
                                    else:
                                        all_coins = all_coins - price
                                        file_coins = open("coins.txt", "w")
                                        file_coins.write(str(all_coins))
                                        file_coins.close()
                                        filename = skins[skin]
                                        bird = Bird(filename)
                                        text_coins = coins_font.render(str(all_coins), True, (255, 255, 51))
                                        prices[skin] = 0

                                elif event.key == pygame.K_RIGHT:
                                    skin += 1
                                elif event.key == pygame.K_LEFT:
                                    skin -= 1

                                if skin < 0:
                                    skin = len(skins) - 1
                                elif skin == len(skins):
                                    skin = 0

                                price = prices[skin]
                                bird_example = Bird(skins[skin])
                        if price > all_coins:
                            text_buy = buy_font.render("Недостаточно денег", True, (200, 50, 20))
                            buy_koor = (window_size[0] // 2 - 150, window_size[1] // 2 + 200)
                        else:
                            text_buy = buy_font.render("Купить скин  (кнопка 'B')", True, (50, 200, 20))
                            buy_koor = (window_size[0] // 2 - 190, window_size[1] // 2 + 200)

                        text_price = price_font.render("Цена: " + str(price), True, (50, 200, 20))

                        sc.blit(bird_example.image, bird_example.rect)
                        sc.blit(text_title, (120, 50))
                        sc.blit(text_shop, (window_size[0] - 300, window_size[1] - 60))
                        sc.blit(text_buy, buy_koor)
                        sc.blit(text_coins, (window_size[0] // 2 - 280, window_size[1] // 2 + 285))
                        sc.blit(text_price, (window_size[0] // 2 - 70, window_size[1] // 2 + 130))

                        pygame.display.update()

                    while_change = 0
                    text_shop = shop_font.render("Магазин (кнопка 'S')", True, (50, 150, 200))
                    text_title = title_font.render("Flappy Bird", True, (50, 200, 50))
                    coins_font = pygame.font.Font(filename_ttf, 72)
                    text_coins = coins_font.render("0", True, (255, 255, 51))

        sc.blit(bird.image, bird.rect)
        sc.blit(text_title, (60, 50))
        sc.blit(text_shop, (window_size[0] - 330, window_size[1] - 60))

        pygame.display.update()
    while_change = 0
    while_change_game = 0

    while while_change_game == 0:
        # игра
        while while_change == 0:

            clock.tick(FPS)
            sc.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jump_cold = 15

            if bird.rect.colliderect(plate1.rect) or bird.rect.colliderect(plate2.rect):
                while_change = 1
            elif bird.rect.colliderect(tube_up.rect) or bird.rect.colliderect(tube_down.rect):
                while_change = 1
            elif tube_up.rect.x + 4 == bird.rect.x:
                coins = coins + 1
                text_coins = coins_font.render(str(coins), True, (255, 255, 51))

            if jump_cold >= 0:
                jump_cold = jump_cold - 1
                bird.rect.y = bird.rect.y - 5
            elif jump_cold <= -10:
                jump_cold = jump_cold - 1
                bird.rect.y = bird.rect.y + 10
            elif jump_cold < 0 and jump_cold > -10:
                jump_cold = jump_cold - 1
                bird.rect.y = bird.rect.y + 6

            if plate2.rect.x < 0:
                plate1.rect.x = 0
                plate2.rect.x = window_size[0] + 680

            tube_down.update()
            tube_up.update()
            plate1.update()
            plate2.update()

            plate1.rect.x -= game_speed
            plate2.rect.x -= game_speed

            # отображение всех объектов
            sc.blit(tube_down.image, tube_down.rect)
            sc.blit(tube_up.image, tube_up.rect)
            sc.blit(plate1.image, plate1.rect)
            sc.blit(plate2.image, plate2.rect)
            sc.blit(bird.image, bird.rect)
            sc.blit(text_coins, (window_size[0]//2-15, 40))

            pygame.display.update()

        if coins == -1:
            coins = 0
        while_change = 0
        jump_cold = 250
        text_score = score_font.render("Монет: " + str(coins), True, (150, 150, 255))
        all_coins += coins
        file_coins = open("coins.txt", "w")
        file_coins.write(str(all_coins))
        file_coins.close()

        # экран после смерти
        while while_change == 0:
            clock.tick(FPS)
            sc.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and jump_cold < 220:
                        while_change = 1
                    elif event.key == pygame.K_m:
                        while_change_game = 1
                        while_change = 1

            if jump_cold > 0:
                bird.rect.y = bird.rect.y + 10

            jump_cold = jump_cold - 1

            sc.blit(tube_down.image, tube_down.rect)
            sc.blit(tube_up.image, tube_up.rect)
            sc.blit(plate1.image, plate1.rect)
            sc.blit(plate2.image, plate2.rect)
            sc.blit(bird.image, bird.rect)
            sc.blit(text_lost, (10, 50))
            sc.blit(text_score, (10, 200))
            sc.blit(text_menu, (10, 350))

            pygame.display.update()
        while_change = 0
        coins = -1
        tube_up.__init__(tube_y, len_y)
        tube_down.__init__(tube_y, len_y)
        bird.__init__(filename)
        text_coins = coins_font.render("0", True, (255, 255, 51))
        jump_cold = 0
