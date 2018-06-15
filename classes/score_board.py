
import pygame.font
from pygame.sprite import Group
from classes.ship import Ship

class ScoreBoard():
    #显示得到面板类
    def __init__(self,setting,screen,states):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.setting=setting
        self.states=states

        self.font=pygame.font.SysFont(None,48)
        self.txt_color=(0,0,0)

        self.pre_score()
        self.pre_ship()

    def pre_score(self):
        self.round_score=int(round(self.states.score,-1))
        self.socre_str="{:,}".format(self.round_score)
        self.score_image=self.font.render('Score:'+self.socre_str,True,self.txt_color,self.setting.bg_color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def pre_ship(self):
        self.ships=Group()
        for ship_num in range(self.states.ship_left):
            ship=Ship(self.screen)
            ship.rect.x=10+ship_num*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.ships.draw(self.screen)