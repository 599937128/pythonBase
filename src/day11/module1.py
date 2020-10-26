import pygame, sys
from pygame.locals import *


# 坦克大战的主窗口
class TankeMain(object):
    # 屏幕的宽度和高度
    width = 600
    height = 500

    # 开始游戏的窗口
    def startGame(self):
        # 模块初始化,加载操作系统的资源
        pygame.init()
        # (600,400) 宽高像素 ,第二个参数,窗口的属性 可变 RESIZABLE 0 固定大小, 第三个参数 颜色的位数 32为
        screen = pygame.display.set_mode((TankeMain.width, TankeMain.height), 0, 32)
        # 给窗口设置一个标题
        pygame.display.set_caption('坦克大战')
        my_tank = My_Tank(screen)
        while True:
            # EGB color (0,100,200) 设置屏幕的背景色
            screen.fill((0, 0, 0))
            # 显示左上角的文字
            screen.blit(self.write_text(), (0, 10))
            # 获取事件
            self.get_event(my_tank)
            my_tank.display()
            # 显示重置
            pygame.display.update()

    # 获取所有的事件
    def get_event(self, my_tank):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame()  # 程序退出
            if event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    my_tank.direction = 'L'
                    my_tank.move()
                if event.key == K_RIGHT or event.key == K_d:
                    my_tank.direction = 'R'
                    my_tank.move()
                if event.key == K_UP:
                    my_tank.direction = 'U'
                    my_tank.move()
                if event.key == K_DOWN:
                    my_tank.direction = 'D'
                    my_tank.move()
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
        font = pygame.font.SysFont("SimHei", 20)  # 定义一个字体
        text_sf = font.render("敌方坦克数量:10", True, (255, 0, 0))  # 显示文字
        return text_sf


# 坦克大战游戏所有对象的父类
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 所有对象的公共属性


class Tank(BaseItem):
    # 定义类属性,所有的坦克高和宽度都是一致
    width = 60
    height = 60

    def __init__(self, screen, left, top):
        # 执行父类的方法
        super().__init__()
        self.screen = screen  # 坦克移动的时候需要显示的屏幕
        self.direction = 'D'  # 坦克的方向,默认的方向是向下 方向是上下左右
        self.speed = 5  # 坦克移动的速度
        self.images = {}  # 坦克的所有方向 key = 方向 value = 图片 (surface)
        self.images['L'] = pygame.image.load("../images/p1tankL.gif")
        self.images['R'] = pygame.image.load("../images/p1tankR.gif")
        self.images['U'] = pygame.image.load("../images/p1tankU.gif")
        self.images['D'] = pygame.image.load("../images/p1tankD.gif")
        self.image = self.images[self.direction]  # 坦克的图片 由方向决定
        self.rect = self.image.get_rect()  # 获取边界
        self.rect.left = left
        self.rect.top = top
        self.live = True  # 决定坦克是否被消灭了

    def display(self):
        self.image = self.images[self.direction]
        self.screen.blit(self.image, self.rect)

    def move(self):
        pass

    def fire(self):
        pass


class My_Tank(Tank):
    def __init__(self, screen):
        super().__init__(screen, 250, 290)  # 创建一个我方坦克

    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:  # 判断是否在屏幕的左边的边界上
                self.rect.left -= self.speed
            else:
                self.rect.left = 0
        elif self.direction == 'R':
            if self.rect.right < TankeMain.width:
                self.rect.right += self.speed
            else:
                self.rect.right = TankeMain.width
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.rect.top = 0
        elif self.direction == 'D':
            if self.rect.top < TankeMain.height:
                self.rect.top += self.speed
            else:
                self.rect.top = TankeMain.height


if __name__ == '__main__':
    game = TankeMain()
    game.startGame()
