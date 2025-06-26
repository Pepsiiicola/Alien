import sys
import pygame

class AlienInvasion:
    def __init__(self):
        # 初始化背景设置
        pygame.init()
        # 创建一个显示窗口，大小为1200*800
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # 开始游戏的主循环
        while