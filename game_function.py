#此模块存储让游戏运行的函数，简化run_game(),避免alien_invasion.py过长，逻辑性更强
#可用于退出游戏
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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
def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""

    screen.fill(ai_settings.bg_color)   # 每次循环都重绘屏幕 (背景色填充屏幕)
    for bullet in bullets.sprites(): #重绘子弹(出现在飞船和外星人后面),bullets.sprites()返回一个列表
        bullet.draw_bullet()
    ship.blitme()  # 重绘飞船(确保出现在背景前面)
    aliens.draw(screen)  #重绘外星人
    pygame.display.flip()  # 让最近绘制的屏幕可见(屏幕的更新)

def update_bullets(ai_settings,screen,ship,aliens,bullets):
    """更新子弹的位置，并删除已消失的子弹"""

    bullets.update()  #更新子弹位置
    for bullet in bullets.copy():   # 删除已消失的子弹
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_aliens_collisions(ai_settings, screen, aliens, ship, bullets)

def check_bullet_aliens_collisions(ai_settings, screen, aliens,ship,bullets):
    """响应子弹和外星人的碰撞"""

    #删除子弹与外星人碰撞后的外星人
    collisions=pygame.sprite.groupcollide(bullets,aliens,False,True) #sprite.groupcollide()检查两个编组中元素碰撞,返回值是一个字典包括碰撞的子弹和外星人,两个实参True,False表示了碰撞后子弹和外星人是否消失
    #删除现有的子弹并创建新的外星人群
    if len(aliens)==0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens,ship)

def get_number_aliens_x(alien_width,ai_settings):
    """计算一行可容纳多少外星人"""

    available_apace_x=ai_settings.screen_width-2*alien_width#(左1右1留白)
    number_aliens_x=int(available_apace_x/(2*alien_width))  #外星人间距为外星人的宽度
    return number_aliens_x


def get_number_rows(alien_height, ship_height,ai_settings):
    """计算一列可容纳多少外星人"""

    available_apace_y = ai_settings.screen_height -ship_height- 3* alien_height#(上1下2留白)
    number_rows= int(available_apace_y / (2 * alien_height))  # 外星人间距为外星人的宽度
    return number_rows

def create_aliens(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并将其放在当前行"""

    alien = Alien(ai_settings, screen)
    alien_width=alien.rect.width
    alien_height=alien.rect.height
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens,ship):
    """创建外星人群"""

    # 创建一个外星人，并计算一行可容纳多少外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(alien.rect.width, ai_settings)
    number_rows=get_number_rows(alien.rect.height, ship.rect.height,ai_settings)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_aliens(ai_settings, screen, aliens, alien_number,row_number)

#向下移动外星人群并改变移动方向
def check_fleet_edges(ai_settings,aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    """先将整群外星人下移,再改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1
def update_aliens(ai_settings,aliens,ship,stats,bullets,screen):
    """检查外星人是否到屏幕边缘,更新外星人群中所有外星人的位置"""

    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens): #spritecollideany()传入的实参是一个精灵,一个编组,返回第一个碰撞精灵的编组成员或None
        ship_hit(ai_settings, stats, aliens, bullets, screen, ship)
    #检查是否有外星人到达屏幕底端
    check_aliens_bottom(screen,aliens,ai_settings,stats,bullets,ship)

def ship_hit(ai_settings, stats, aliens, bullets, screen, ship):
    """响应被外星人撞到的飞船"""

    if stats.ships_left>0:
        stats.ships_left -= 1
        sleep(0.5)
    else:
        stats.game_active=False
    # 清空子弹和外星人列表
    aliens.empty()
    bullets.empty()
    # 创建一批新的外星人，并将飞船至于屏幕底部中央
    create_fleet(ai_settings, screen, aliens, ship)
    ship.center_ship()
    #暂停
    sleep(0.5)

def check_aliens_bottom(screen,aliens,ai_settings,stats,bullets,ship):
    """检查外星人是否到屏幕底端"""

    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #像飞船被撞到一样处理
            ship_hit(ai_settings, stats, aliens, bullets, screen, ship)
            break





