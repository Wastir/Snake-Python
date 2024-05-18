import pygame
from class_snake import Snake
from class_food import Food  # Import klasy Food z pliku food.py

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake = Snake(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT)  # Inicjalizacja węża w środku ekranu
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)  # Inicjalizacja jedzenia
# Główna pętla gry
running = True
clock = pygame.time.Clock()  # Dodane zegara
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # Obsługa klawiszy
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
            elif event.key == pygame.K_ESCAPE:
                running = False

    snake.move(food)  # Przesuń węża

    screen.fill((224,159,116))  # Wypełnienie ekranu kolorem czarnym
    snake.draw(screen)  # Narysuj węża na ekranie
    food.draw(screen)  # Narysuj jedzenie na ekranie
    pygame.display.flip()  # Odświeżenie ekranu

    clock.tick(10)  # Dodana kontrola prędkości

pygame.quit()
