import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, setting, screen):
        super().__init__()
        self.screen = screen
        self.setting = setting

        self.image = pygame.image.load(r'D:\python workspace\alien_invasion\image\alien.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.setting.alien_speed * self.setting.alien_move_direct
        self.rect.x = self.x


    # 检测外星人是否到达屏幕边缘
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    # 改变外星人移动方向
    def change_direct(self,aliens):
        self.setting.alien_move_direct *= -1
        for alien in aliens:
            alien.rect.y+=self.setting.alien_drop_speed
