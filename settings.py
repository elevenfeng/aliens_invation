class Setting():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # 飞船初始数量
        self.ship_left = 3

        # 子弹
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (0, 0, 0)
        self.bullet_allow = 10

        # 外星人
        self.alien_drop_speed = 2

        self.speedup_scale=2
        self.aliens_scoreup=2
        self.init_dynamic_pra()

    def init_dynamic_pra(self):

        self.ship_speed = 2
        self.bullet_speed = 3
        self.alien_speed = 0.3
        # 向左-1，向右1
        self.alien_move_direct = 1

        self.alien_points=50


    def increase_speed(self):
        self.ship_speed*=self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points*=self.aliens_scoreup