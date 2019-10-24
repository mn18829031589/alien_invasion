#此模块存储让游戏运行的函数，简化run_game(),避免alien_invasion.py过长，逻辑性更强
#可用于退出游戏
import sys
import pygame
from bullet import Bullet

#管理事件函数
def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""

    # 监视键盘和鼠标事件(用户的执行操作),根据发生的事件类型执行相应的任务
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 每次按键都在pygame中注册成一个KEYDOWN事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        #松键是KEYUP事件
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""

    # 检查按下的是否是特定的键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True   # 一直向右移动飞船
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  # 一直向左移动飞船
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_q:   #快捷键退出 q
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制，就发射一颗子弹"""

    # 创建一个子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """响应松开"""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False   # 停止向右移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False  # 停止向左移动


#更新屏幕函数
def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""

    pygame.display.flip()  # 让最近绘制的屏幕可见(屏幕的更新)
    screen.fill(ai_settings.bg_color)   # 每次循环都重绘屏幕 (背景色填充屏幕)
    for bullet in bullets.sprites(): #重绘子弹(出现在飞船和外星人后面),bullets.sprites()返回一个列表
        bullet.draw_bullet()
    ship.blitme()  # 重绘飞船(确保出现在背景前面)

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""

    bullets.update()  #更新子弹位置
    for bullet in bullets.copy():   # 删除已消失的子弹
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

