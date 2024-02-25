import pygame
import time
import random

# Inisialisasi Pygame
pygame.init()

# Warna
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Lebar dan tinggi layar
dis_width = 800
dis_height = 600

# Membuat layar
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Coding with Fun')

# Kedua
clock = pygame.time.Clock()

# Ukuran grid dan ukuran blok
block_size = 20
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

# Fungsi yang menggambar ular
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], block_size, block_size])

# Menampilkan pesan di layar
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Game Loop
def gameLoop():
    game_over = False
    game_close = False

    # Koordinat awal ular
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Perubahan koordinat
    x1_change = 0
    y1_change = 0

    # List yang menyimpan koordinat ular
    snake_List = []
    Length_of_snake = 1

    # Koordinat makanan
    foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(block_size, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
