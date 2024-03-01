import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """代表舰队中单个外星人的类。"""

    def __init__(self, ai_game):
        """初始化外星人并设置其起始位置。"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并设置其 rect 属性。
        self.image = pygame.image.load("C:/Users/X1603Z/Desktop/alien_invasion/alien.bmp")
        self.rect = self.image.get_rect()

        # 在屏幕左上角附近启动每个新外星人。
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的确切水平位置。
        self.x = float(self.rect.x)

    def check_edges(self):
        """如果外星人在屏幕边缘，则返回 True。"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """向右或向左移动外星人。/==-=-09R5T6"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
