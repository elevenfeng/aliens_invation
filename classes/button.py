import pygame.font

class Button():
    def __init__(self,screen,msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.width=100
        self.height=50
        self.bt_color=(0,255,0)
        self.txt_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        self.pre_msg(msg)


    def pre_msg(self,msg):
        #将文字渲染为图片显示
        self.msg_image=self.font.render(msg,True,self.txt_color,self.bt_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_bt(self):
        self.screen.fill(self.bt_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)