import pygame  #可用于管理图形，动画和声音
from settings import Settings  #导入设置类
from ship import Ship  #导入飞船类
import game_function as gf   #导入事件管理类,简化起别名
from pygame.sprite import Group  #创建一个pygame.sprite.Group类的一个实例group(编组),
# 用于存储所有有效的子弹，以便能够管理发射出去的所有子弹

def run_game():

    pygame.init()  #初始化游戏并创建一个屏幕对象
    ai_settings=Settings()    #创建一个Settings实例并将其存储在ai_settings变量中
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("alien_invasion")
    ship=Ship(ai_settings,screen)  #创建一个飞船
    bullets=Group()   #创建一个存储子弹的编组

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)  #监控事件
        ship.update()   #更新飞船位置
        gf.update_bullets(bullets)  #更新子弹
        gf.update_screen(ai_settings,screen,ship,bullets)  #更新屏幕

run_game()