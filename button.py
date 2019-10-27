#pygame没有内置创建按钮的方法,创建button类用于创建带标签的实心矩形
import pygame.font  #能够将文本渲染到屏幕上
class Button():
    def __init__(self,screen,ai_settings,msg):
        """初始化按钮的属性"""

        self.screen=screen
        self.screen_rect=screen.get_rect()
        #设置按钮的尺寸和其它属性
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        #创建按钮的rect对象,并将其居中
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center
        #按钮的标签只需要创建一次
        self.prep_msg(msg)
    def prep_msg(self,msg):
        """将msg渲染为图像,并使其在按钮上居中"""

        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)#将文本转换为图像，最后一个参数是背景色
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center
    def draw_button(self):
        """绘制一个用颜色填充的按钮,再绘制文本"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)