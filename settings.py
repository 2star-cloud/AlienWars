class Settings:
    """存储《外星人入侵》所有设置的类。"""

    def __init__(self):
        """初始化游戏的静态设置。"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置。
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设定
        self.fleet_drop_speed = 10

        # 游戏加速的速度
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化在整个游戏中更改的设置。"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction 的 1 表示右;-1 表示左。
        self.fleet_direction = 1

        # 得分
        self.alien_points = 50

    def increase_speed(self):
        """增加速度设置和外星人分数。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
