#创建设置类，将所有的设置存储在一个地方
#创建一个设置对象来调用不同的设置
class Settings():
    """存储alien_invasion的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,235)
        #调整飞船移动速度
        self.ship_speed_factor=1.5
        #子弹设置
        self.bullet_speed_factor=1
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3
