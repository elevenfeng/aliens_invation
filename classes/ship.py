import pygame
from setting.settings import Setting
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.setting=Setting()
        self.screen = screen
        # 加载飞机图片
        self.image = pygame.image.load(r'D:\python workspace\alien_invasion\image\ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 飞机在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # 初始化飞机位置
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += self.setting.ship_speed
            if self.rect.right>=self.screen_rect.width:
                self.rect.centerx=self.screen_rect.width-self.rect.width/2
        elif self.moving_left:
            self.rect.centerx -= self.setting.ship_speed
            if self.rect.left<=0:
                self.rect.centerx=self.rect.width/2

    def center_ship(self):
        self.rect.centerx=self.screen_rect.centerx
