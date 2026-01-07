import pygame
from constants import (
    SCREEN_WIDTH,
    UI_HEIGHT,
    DARK_GRAY,
    WHITE
)


class GameBar(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.rectangle = pygame.Rect(0, 0, SCREEN_WIDTH, UI_HEIGHT)
        self.font = pygame.font.SysFont(None, 30)
        self.score = 0

    def draw(self, screen):
        pygame.draw.rect(screen, DARK_GRAY, self.rectangle)
        score_surface = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_surface, (10, 10))

    def update(self, dt):
        pass
