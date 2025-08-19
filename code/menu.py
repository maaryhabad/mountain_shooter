#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Rect, Surface
from pygame.font import Font

from code.const import MENU_FONT, WIN_WIDTH, YELLOW_DARK_SHADE1, MENU_OPTIONS, BLUE_DARK_SHADE2


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/background.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/music/menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(60, 'Mountain', YELLOW_DARK_SHADE1, ((WIN_WIDTH / 2), 70))
            self.menu_text(60, 'Shooter', YELLOW_DARK_SHADE1, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(30, MENU_OPTIONS[i], BLUE_DARK_SHADE2, ((WIN_WIDTH / 2), 230 + 50 * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(MENU_FONT, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)