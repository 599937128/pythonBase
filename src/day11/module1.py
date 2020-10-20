import pygame, sys
from pygame.locals import *


# 坦克大战的主窗口
class TankeMain(object):
    # 开始游戏的窗口
    def startGame(self):
        # (600,400) 宽高像素 ,第二个参数,窗口的属性 可变 RESIZABLE 0 固定大小, 第三个参数 颜色的位数 32为
        screen = pygame.display.set_mode((600, 400), 0, 32)
        # 给窗口设置一个标题
        pygame.display.set_caption('坦克大战')
        while True:
            # EGB color (0,100,200) 设置屏幕的背景色
            screen.fill((0, 0, 0))
            # 显示重置
            pygame.display.update()

    # 停止游戏
    def stopGame(self):
        sys.exit()

    # 设置标题
    def setTitle(self):
        pass


if __name__ == '__main__':
    game = TankeMain()
    game.startGame()
