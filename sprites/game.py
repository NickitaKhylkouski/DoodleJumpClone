import pygame
import sys


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.step = 0
        self.points = 0


        self.font = pygame.font.Font(r"assets/fonts/gamefont.ttf", 20)
        self.image = self.font.render(f"HI {self.points}", True, (83, 83, 83))
        self.rect = self.image.get_rect()
        self.rect.topleft = (20, 20)


        surface = pygame.display.get_surface()



    def draw(self, surface):
        surface.blit(self.image, self.rect)
        self.image = self.font.render(f"HI {self.points}", True, (83, 83, 83))


    def update(self, offset):
        self.points += offset


class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


        # ⭐ Конец игры
        self.font = pygame.font.Font(r"assets/fonts/gamefont.ttf", 20)
        self.image = self.font.render(f"G A M E  O V E R", True, (83, 83, 83))
        self.rect = self.image.get_rect()


        surface = pygame.display.get_surface()
        self.rect.center = surface.get_width() / 2, surface.get_height() / 4



    # ⭐ Конец игры
    def draw(self, surface):
        surface.blit(self.image, self.rect)
