class GameStates():
    """跟踪游戏统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings=ai_settings
        self.reset_states()
        #游戏开始时处于非活动状态
        self.game_active=False #(游戏开始结束标志)

    def reset_states(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left=self.ai_settings.ship_limit
