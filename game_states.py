class GameStates():
    """跟踪游戏统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings=ai_settings
        self.reset_states()
        #游戏开始时处于非活动状态
        self.game_active=False #(游戏开始结束标志)
        # 最高分设置
        self.high_score = 0

    def reset_states(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left=self.ai_settings.ship_limit  #游戏中的飞船数量
        self.score=0  #得分
        self.level=1  #等级
