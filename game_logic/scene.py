import pygame

class IsometricScene:
    def __init__(self, assets):
        self.assets = assets
        self.grid_size = 32  # Grid tile size
        self.grid_width = 10
        self.grid_height = 10

    def render(self, screen):
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                screen_x = (x - y) * self.grid_size + 640  # Centered grid
                screen_y = (x + y) * self.grid_size // 2 + 100
                pygame.draw.polygon(screen, (200, 200, 200), [
                    (screen_x, screen_y),
                    (screen_x + self.grid_size, screen_y + self.grid_size // 2),
                    (screen_x, screen_y + self.grid_size),
                    (screen_x - self.grid_size, screen_y + self.grid_size // 2)
                ])
