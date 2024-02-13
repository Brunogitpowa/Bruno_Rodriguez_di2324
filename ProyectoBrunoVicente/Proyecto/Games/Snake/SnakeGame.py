import pygame
import random
import os

ruta_snake = os.path.dirname(__file__)

# Definir constantes
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# Direcciones
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        new_head = ((x + (dx * GRID_SIZE)) % SCREEN_WIDTH, (y + (dy * GRID_SIZE)) % SCREEN_HEIGHT)
        if new_head in self.body[1:]:
            return False  # Choca consigo misma, juego terminado
        self.body.insert(0, new_head)
        if len(self.body) > self.score + 1:
            del self.body[-1]
        return True

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def grow(self):
        self.score += 1

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (*segment, GRID_SIZE, GRID_SIZE))

    def get_head_position(self):
        return self.body[0]

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, (*self.position, GRID_SIZE, GRID_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # Cargar la imagen de fondo
    background_image = pygame.image.load(os.path.join(ruta_snake,"snake.jpg"))
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    snake = Snake()
    food = Food()

    running = True
    while running:
        # Dibujar la imagen de fondo
        screen.blit(background_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        if snake.move():
            if snake.get_head_position() == food.position:
                snake.grow()
                food.randomize_position()
            snake.draw(screen)
            food.draw(screen)
            pygame.display.update()
            clock.tick(10)  # Velocidad de la serpiente
        else:
            running = False

    pygame.quit()

if __name__ == "__main__":
    main()
