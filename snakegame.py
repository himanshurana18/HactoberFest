import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game dimensions
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20

# Directions
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

# Initialize screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    snake = [(5, 5), (4, 5), (3, 5)]
    direction = RIGHT
    food = (random.randint(0, (WIDTH//CELL_SIZE) - 1), random.randint(0, (HEIGHT//CELL_SIZE) - 1))
    running = True

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT
                elif event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN

        head = snake[0]
        next_cell = (head[0] + direction[0], head[1] + direction[1])

        if next_cell == food:
            snake.insert(0, next_cell)
            food = (random.randint(0, (WIDTH//CELL_SIZE) - 1), random.randint(0, (HEIGHT//CELL_SIZE) - 1))
        else:
            snake.insert(0, next_cell)
            snake.pop()

        if (next_cell[0] < 0 or next_cell[0] >= WIDTH//CELL_SIZE or
            next_cell[1] < 0 or next_cell[1] >= HEIGHT//CELL_SIZE or
            next_cell in snake[1:]):
            running = False

        draw_snake(snake)
        draw_food(food)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
