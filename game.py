import pygame
import random
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 720
screen_height = 1280
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithHarry")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0
snake_size = 20
fps = 30
food_size = 30
food_x = random.randint(0, screen_width)
food_y =  random.randint(0, screen_height)

clock = pygame.time.Clock()
# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_a:
                velocity_x = - 10
                velocity_y = 0

            if event.key == pygame.K_p:
                velocity_y = - 10
                velocity_x = 0

            if event.key == pygame.K_m:
                velocity_y = 10
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    gameWindow.fill(white)
   
    pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size]) 
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)


pygame.quit()
quit()

