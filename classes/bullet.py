import pygame
from pygame.sprite import Sprite

#子弹类，继承精灵类
class Bullet(Sprite):
    def __init__(self,setting,screen,ship):             #为什么可以识别setting ship？？？
        super().__init__()
        self.screen=screen
        #创建（0，0）子弹，再调整位置
        self.rect=pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        self.y=self.rect.y
        self.color=setting.bullet_color
        self.speed=setting.bullet_speed

    def update(self):
        #子弹向上走
        self.y-=self.speed
        self.rect.y=self.y

    #绘制子弹
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)