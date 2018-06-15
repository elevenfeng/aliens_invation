import sys
import pygame
from setting.settings import Setting
from classes.ship import Ship
import game_functions as gf
from pygame.sprite import Group
from classes.game_states import GameStates
from classes.button import Button
from classes.score_board import ScoreBoard

def run_game():
    #初始化游戏并创建屏幕对象
    pygame.init()
    setting=Setting()
    screen=pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("打飞机")

    #实例化飞机
    ship=Ship(screen)

    #储存子弹编组
    bullets=Group()

    #实例化外星人
    aliens=Group()
    gf.create_fleet(setting,screen,ship,aliens)

    #游戏状态
    states=GameStates(setting)

    #开始按钮
    play_bt=Button(screen,'play')

    #记分板
    sb=ScoreBoard(setting,screen,states)
    #开始游戏主循环
    while True:
        #监视鼠标和键盘事件
        gf.check_events(setting,screen,ship,bullets,aliens,states,play_bt,sb)
        if states.game_active:
            #更新飞机位置
            ship.update()
            #子弹更新
            gf.update_bullets(setting,screen,ship,aliens,bullets,states,sb)
            #外星人更新
            gf.update_aliens(ship,aliens,bullets,setting,screen,states,sb)
        #让最近的屏幕绘制可见
        gf.update_screen(setting,screen,ship,bullets,aliens,states,play_bt,sb)

run_game()


