import sys
import pygame
from bullet import Bullet

def check_keydown_event(event,ai_settings,screen,ship,bullets):
    '''按键响应'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #   创建一颗子弹，并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        exit()

def check_keyup_event(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    '''响应键盘事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type ==pygame.KEYUP:
            check_keyup_event(event,ship)

def update_screen(ai_settings,screen,ship,bullets):
    #   每次循环时都刷新
    screen.fill(ai_settings.bg_color)
    #   在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #   让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    # 删除已消失的子弹
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    print(len(bullets))