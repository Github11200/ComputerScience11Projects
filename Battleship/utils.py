import pygame


class PygameUtils:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def display_text(self, text, font_size, color: pygame.Color, y_pos=650):
        font = pygame.font.SysFont("Arial", font_size)
        font_surface = font.render(text, False, color)
        center = font_surface.get_rect(
            center=(self.screen.get_width() / 2, y_pos))
        self.screen.blit(font_surface, center)
