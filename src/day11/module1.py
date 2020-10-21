import pygame, sys
from pygame.locals import *


# 坦克大战的主窗口
class TankeMain(object):
    # 开始游戏的窗口
    def startGame(self):
        # 模块初始化,加载操作系统的资源
        pygame.init()
        # (600,400) 宽高像素 ,第二个参数,窗口的属性 可变 RESIZABLE 0 固定大小, 第三个参数 颜色的位数 32为
        screen = pygame.display.set_mode((600, 400), 0, 32)
        # 给窗口设置一个标题
        pygame.display.set_caption('坦克大战')
        while True:
            # EGB color (0,100,200) 设置屏幕的背景色
            screen.fill((0, 0, 0))
            # 显示左上角的文字
            screen.blit(self.write_text(), (0, 10))
            # 获取事件
            self.get_event()
            # 显示重置
            pygame.display.update()

    # 获取所有的事件
    def get_event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame()  # 程序退出
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pass
                if event.key == K_RIGHT:
                    pass
                if event.key == K_UP:
                    pass
                if event.key == K_DOWN:
                    pass
                # 敲击esc键
                if event.key == K_ESCAPE:
                    self.stopGame()

    # 停止游戏
    def stopGame(self):
        sys.exit()

    # 设置标题
    def setTitle(self):
        pass

    # 在屏幕的左上角显示文字内容
    def write_text(self):
        font = pygame.font.SysFont("simsunexttb", 20)  # 定义一个字体
        text_sf = font.render("敌方坦克数量:10", True, (255, 0, 0))  # 显示文字
        return text_sf


if __name__ == '__main__':
    game = TankeMain()
    game.startGame()
