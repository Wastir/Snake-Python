import pygame
import sys
class Snake:
    def __init__(self, x, y, screen_width, screen_height):
        self.head = [x, y]
        self.body = [[x, y], [x-20, y], [x-(2*20), y]]  # Początkowa długość węża
        self.direction = "LEFT"  # Początkowy kierunek ruchu
        self.grow_flag = False  # Flaga określająca, czy wąż powinien rosnąć
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Załaduj obrazy dla głowy i tułowia
        self.head_image = pygame.image.load("head.png")
        self.body_image = pygame.image.load("body.png")

        self.head_image = pygame.transform.scale(self.head_image, (20, 20))
        self.body_image = pygame.transform.scale(self.body_image, (20, 20))


    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def move(self, food):
        if self.direction == "UP":
            self.head[1] -= 20
            if self.head[1] < 0:  # Sprawdź, czy wąż przekroczył górną krawędź ekranu
                self.head[1] = self.screen_height - 20
        elif self.direction == "DOWN":
            self.head[1] += 20
            if self.head[1] >= self.screen_height:  # Sprawdź, czy wąż przekroczył dolną krawędź ekranu
                self.head[1] = 0
        elif self.direction == "LEFT":
            self.head[0] -= 20
            if self.head[0] < 0:  # Sprawdź, czy wąż przekroczył lewą krawędź ekranu
                self.head[0] = self.screen_width - 20
        elif self.direction == "RIGHT":
            self.head[0] += 20
            if self.head[0] >= self.screen_width:  # Sprawdź, czy wąż przekroczył prawą krawędź ekranu
                self.head[0] = 0

        if self.head == food.position:
            food.respawn()
            self.grow()

        if not self.grow_flag:
            # Usuń ostatni segment, aby zachować stałą długość węża
            self.body.pop()
        else:
            self.grow_flag = False
        if self.head == food.position:
            print("Snake ate food!")
            food.respawn(self.body)
            self.grow()
        
        # Dodanie nowej głowy
        self.body.insert(0, list(self.head))
        # Sprawdź kolizję z ogonem
        for segment in self.body[3:]:  # Pomijamy pierwszy segment (głowę węża)
            if self.head == segment:
                print("nastąpiła kolizja z ogonem")
                self.game_over()  # Wywołanie funkcji zakończenia gry
                break


        

    def game_over(self):
        # Kod zakończenia gry, np. wyświetlenie komunikatu i zatrzymanie pętli gry
        print("Game Over")
        pygame.quit()
        sys.exit()
    def grow(self):
        self.grow_flag = True

    def draw(self, surface):
        
        # Narysuj tułów z obrotem
        for i in range(1, len(self.body)):
            segment = self.body[i]
            previous_segment = self.body[i-1]
            angle = self.get_segment_angle(previous_segment, segment)
            rotated_body_image = pygame.transform.rotate(self.body_image, angle)
            surface.blit(rotated_body_image, (segment[0], segment[1]))
        
        # Narysuj głowę
        surface.blit(self.head_image, (self.body[0][0], self.body[0][1]))

    def get_segment_angle(self, previous_segment, segment):
        dx = segment[0] - previous_segment[0]
        dy = segment[1] - previous_segment[1]
        if dx == 20:
            return -90
        elif dx == -20:
            return 90
        elif dy == 20:
            return 0
        elif dy == -20:
            return 180
        return 0