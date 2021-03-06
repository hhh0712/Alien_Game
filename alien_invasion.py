import sys
import pygame
from settings import Setting
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scporeboard
from buttom import Button

def run_game():
    #   初始化游戏并创造一个屏幕对象
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #   创建一个用于存储游戏统计信息的实例,并创建计分牌
    stats = GameStats(ai_settings)
    sb = Scporeboard(ai_settings,screen,stats)
    #   创建一个play按钮
    play_button = Button(ai_settings,screen,"Play")

    #   创建一个飞船
    ship = Ship(ai_settings,screen)

    #   创建一个用于储存子弹的编组
    bullets = Group()
    aliens = Group()

    #   创建外星群
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #   开始游戏的主循环
    while True:
        #   监听鼠标和键盘事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()
