class Settings:
    """存储游戏《外星人入侵》中所有的类"""

    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_size = (self.screen_width, self.screen_height)
        self.bg_color = (230, 230, 230)

        #速度设置
        self.ship_speed = 1