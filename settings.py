#创建设置类，将所有的设置存储在一个地方
#创建一个设置对象来调用不同的设置
class Settings():
    """存储alien_invasion的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""

        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,235)
        #飞船设置
        #self.ship_speed_factor=1.5
        self.ship_limit=3
        #子弹设置
        #self.bullet_speed_factor=3
        self.bullet_width=800
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=5
        #外星人设置
        #self.alien_speed_factor=1
        self.fleet_drop_speed=50
        #self.fleet_direction=1

        #加快游戏节奏的速度
        self.speedup_scale=1.1
        #提高外星人点数的速度
        self.score_scale=1.5
        #初始化动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的属性"""
        # 设置了外星人,子弹,飞船的初始速度
        self.alien_speed_factor=1
        self.bullet_speed_factor=3
        self.ship_speed_factor=1.5
        #初始化外星人的移动方向,始终先向右
        self.fleet_direction=1
        #记分设置
        self.alien_points=50

    def increase_speed(self):
        """提高速度设置和外星人点数"""

        self.alien_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.ship_speed_factor*=self.speedup_scale

        self.alien_points*=self.score_scale



