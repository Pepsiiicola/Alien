import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion():
    def __init__(self):
        # 初始化背景设置
        pygame.init()
        self.settings = Settings()
        # 创建一个显示窗口，大小为1200*800
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):

        # 每次循环时都重绘屏幕
        self.screen.fill(self.settings.bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

        """开始游戏的主循环"""
        while True:
            # 监听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            
        
    
if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()


