class GameStats:
    """记录外星人入侵的统计数据。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 以非活动状态启动游戏。
        self.game_active = False

        # 永远不重置高分。
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏过程中可能更改的统计信息。"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1