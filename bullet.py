import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理从船上发射的子弹的类"""

    def __init__(self, ai_game):
        """在飞船的当前位置创建一个子弹对象。"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在 （0， 0） 处创建一个项目符号矩形，然后设置正确的位置。
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 将项目符号的位置存储为十进制值。
        self.y = float(self.rect.y)

    def update(self):
        """将子弹向上移动屏幕。"""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """将子弹绘制到屏幕上。"""
        pygame.draw.rect(self.screen, self.color, self.rect)
