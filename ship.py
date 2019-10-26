import pygame
#创建飞船类，将飞船显示在屏幕上，负责飞船的大部分行为
class Ship():

    def __init__(self,ai_settings,screen): #screen指定了要将飞船绘制到什么地方,ai_settings获取飞船移动速度设置
        """初始化飞船并设置其初始值"""

        self.screen=screen
        # 将形参的只存储在一个属性中，以便在update()中能够使用它
        self.ai_settings=ai_settings
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #将每艘新飞船放置在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        #在飞船属性center中存储小数值 (rect属性只能存储整数值)
        self.center=float(self.rect.centerx)

        #为了允许飞船持续移动，使用moving_right/left标志，结合KEYDOWN和KEYUP事件
        self.moving_right=False
        self.moving_left=False

    def update(self):
        """根据移动标志调整飞船的位置"""

        #更新飞船的center值，而不是rect值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #根据self.center更新rect
        self.rect.centerx=self.center

    def blitme(self):
        """在指定位置(self.rect指定)绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕居中"""
        self.center=self.screen_rect.centerx

