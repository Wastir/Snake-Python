import pygame
import random

class Food:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("food.png")  # Załaduj obraz jedzenia
        self.image = pygame.transform.scale(self.image, (20, 20))  # Skaluj obraz do 20x20 pikseli
        self.position = [random.randrange(0, screen_width, 20), random.randrange(0, screen_height, 20)]
        self.color = (255, 0, 0)  # Czerwony kolor jedzenia

    def respawn(self):
        while True:
            self.position = [random.randrange(0, self.screen_width, 20), random.randrange(0, self.screen_height, 20)]
            break


    def draw(self, surface):
        surface.blit(self.image, self.position)  # Narysuj obraz jedzenia na ekranie