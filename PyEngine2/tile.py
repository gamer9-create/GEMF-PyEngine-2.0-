import pygame


pygame.init()


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, size, screen, image):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        self.render_offset = [0, 0]
        self.group = None
        self.color = (0,0,0)


    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.image.fill(self.color)
        self.screen.blit(self.image, (self.x + self.render_offset[0], self.y + self.render_offset[1]))
