import pygame, sys, time
from random import randint
from pygame.locals import *


# 坦克大战的主窗口
class TankeMain(object):
    # 屏幕的宽度和高度
    width = 1000
    height = 800
    my_tank_missle_list = []
    # enemy_list = []
    enemy_list = pygame.sprite.Group()  # 敌方坦克的组群
    explode_list = []
    Wall = None
    my_tank = None
    enemy_missile_list = pygame.sprite.Group()  # 敌方坦克炮弹

    # 开始游戏的窗口
    def startGame(self):
        # 模块初始化,加载操作系统的资源
        pygame.init()
        # (600,400) 宽高像素 ,第二个参数,窗口的属性 可变 RESIZABLE 0 固定大小, 第三个参数 颜色的位数 32为
        screen = pygame.display.set_mode((TankeMain.width, TankeMain.height), 0, 32)
        # 给窗口设置一个标题
        pygame.display.set_caption('坦克大战')
        TankeMain.Wall = Wall(screen, 65, 160, 30, 100)
        TankeMain.my_tank = My_Tank(screen)
        if len(TankeMain.enemy_list):
            for i in range(1, 6):
                TankeMain.enemy_list.add(Enemy_Tank(screen))

        while True:
            if len(TankeMain.enemy_list) < 5:
                TankeMain.enemy_list.add(Enemy_Tank(screen))
            # EGB color (0,100,200) 设置屏幕的背景色
            screen.fill((0, 0, 0))
            # 显示左上角的文字
            for i, text in enumerate(self.write_text(), 0):  # 使用枚举
                screen.blit(text, (0, 5 + (15 * i)))
            # 显示墙, 并且对墙和其他的做碰撞检测
            TankeMain.Wall.display()
            TankeMain.Wall.hit_other()
            # 获取事件
            self.get_event(TankeMain.my_tank, screen)
            if TankeMain.my_tank:
                TankeMain.my_tank.hit_enemy_missile()  # 我方坦克和敌方的炮弹进行碰撞检测
            if TankeMain.my_tank and TankeMain.my_tank.live:
                TankeMain.my_tank.display()  # 在屏幕上显示我方坦克
                TankeMain.my_tank.move()  # 坦克移动
            else:
                print("GAME OVER")
                TankeMain.my_tank = None
            # 创建敌方坦克
            for enemy in TankeMain.enemy_list:
                enemy.display()
                enemy.random_move()
                enemy.random_fire()
            # 显示我方坦克发射的炮弹
            for m in TankeMain.my_tank_missle_list:
                if m.live:
                    m.display()
                    m.hit_tank()  # 打中敌方坦克
                    m.move()
                else:
                    TankeMain.my_tank_missle_list.remove(m)

            # 显示敌方坦克发射的炮弹
            for m in TankeMain.enemy_missile_list:
                if m.live:
                    m.display()
                    m.move()
                else:
                    TankeMain.enemy_missile_list.remove(m)

            # 显示爆炸效果
            for explode in TankeMain.explode_list:
                explode.display()
            time.sleep(0.05)  # 每次休眠0.05秒跳到下一帧
            # 显示重置
            pygame.display.update()

    # 获取所有的事件
    def get_event(self, my_tank, screen):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.stopGame()  # 程序退出
            if event.type == KEYDOWN and (not my_tank) and event.key == K_n:
                TankeMain.my_tank = My_Tank(screen)
            if event.type == KEYDOWN and my_tank:
                if event.key == K_LEFT or event.key == K_a:
                    my_tank.direction = 'L'
                    my_tank.stop = False
                    # my_tank.move()
                if event.key == K_RIGHT or event.key == K_d:
                    my_tank.direction = 'R'
                    my_tank.stop = False
                    # my_tank.move()
                if event.key == K_UP:
                    my_tank.direction = 'U'
                    my_tank.stop = False
                    # my_tank.move()
                if event.key == K_DOWN:
                    my_tank.direction = 'D'
                    my_tank.stop = False
                    # my_tank.move()
                # 敲击esc键
                if event.key == K_ESCAPE:
                    self.stopGame()
                if event.key == K_SPACE:
                    m = my_tank.fire()
                    m.good = True
                    TankeMain.my_tank_missle_list.append(m)
            if event.type == KEYUP and my_tank:
                if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_UP or event.key == K_DOWN:
                    my_tank.stop = True

    # 停止游戏
    def stopGame(self):
        sys.exit()

    # 设置标题
    def setTitle(self):
        pass

    # 在屏幕的左上角显示文字内容
    def write_text(self):
        font = pygame.font.SysFont("SimHei", 20)  # 定义一个字体
        text_sf = font.render("敌方坦克数量:%d" % len(TankeMain.enemy_list), True, (255, 0, 0))  # 显示文字
        text_sf2 = font.render("我方坦克子弹数量:%d" % len(TankeMain.my_tank_missle_list), True, (255, 0, 0))  # 显示文字
        return text_sf, text_sf2


# 坦克大战游戏所有对象的父类
class BaseItem(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        # 所有对象的公共属性
        self.screen = screen

    def display(self):
        if self.live:
            self.image = self.images[self.direction]
            self.screen.blit(self.image, self.rect)


class Tank(BaseItem):
    # 定义类属性,所有的坦克高和宽度都是一致
    width = 60
    height = 60

    def __init__(self, screen, left, top):
        # 执行父类的方法
        super().__init__(screen)
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
        self.rect.bottom = top
        self.live = True  # 决定坦克是否被消灭了
        self.oldtop = self.rect.top
        self.oldleft = self.rect.left

    def stay(self):
        self.rect.top = self.oldtop
        self.rect.left = self.oldleft

    def move(self):
        if not self.stop:  # 如果坦克不是停止状态
            self.oldleft = self.rect.left
            self.oldtop = self.rect.top
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
                if self.rect.bottom < TankeMain.height:
                    self.rect.bottom += self.speed
                else:
                    self.rect.bottom = TankeMain.height

    def fire(self):
        m = Missile(self.screen, self)
        return m


# 我方坦克
class My_Tank(Tank):
    def __init__(self, screen):
        super().__init__(screen, 250, 290)  # 创建一个我方坦克
        self.stop = Tank
        self.live = True

    def hit_enemy_missile(self):
        hit_list = pygame.sprite.spritecollide(self, TankeMain.enemy_missile_list, False)
        for m in hit_list:  # 我方坦克中弹
            self.live = False
            m.live = False
            TankeMain.enemy_missile_list.remove(m)
            explode = Explode(self.screen, self.rect)
            TankeMain.explode_list.append(explode)


# 敌方坦克
class Enemy_Tank(Tank):
    def __init__(self, screen):
        super().__init__(screen, randint(1, 5) * 100, 200)
        self.images = {}  # 坦克的所有方向 key = 方向 value = 图片 (surface)
        self.images['L'] = pygame.image.load("../images/enemy1L.gif")
        self.images['R'] = pygame.image.load("../images/enemy1R.gif")
        self.images['U'] = pygame.image.load("../images/enemy1U.gif")
        self.images['D'] = pygame.image.load("../images/enemy1D.gif")
        self.speed = 3
        self.step = 6  # 坦克按照某个方向移动的步骤
        self.get_random_direction()

    def get_random_direction(self):
        r = randint(0, 4)  # 得到一个坦克移动方向和停止方向的随机数
        if r == 4:
            self.stop = True
        elif r == 1:
            self.direction = 'L'
            self.stop = False
        elif r == 2:
            self.direction = 'R'
            self.stop = False
        elif r == 0:
            self.direction = 'D'
            self.stop = False
        elif r == 3:
            self.direction = 'U'
            self.stop = False

    # 地方坦克 按照一个随即的方向 连续移动 6步 然后才能改变方向
    def random_move(self):
        if self.live:
            if self.step == 0:
                self.get_random_direction()
                self.step = 6
            else:
                self.move()
                self.step -= 1

    def random_fire(self):
        r = randint(0, 50)
        if r == 10:
            m = self.fire()
            TankeMain.enemy_missile_list.add(m)


# 炮弹
class Missile(BaseItem):
    width = 17
    height = 17

    def __init__(self, screen, tank):
        super().__init__(screen)
        self.tank = tank
        self.direction = tank.direction  # 炮弹的方向 由所发射的坦克决定
        self.speed = 15  # 炮弹移动的速度
        self.images = {}  # 炮弹的图片
        self.images['L'] = pygame.image.load("../images/enemymissile.gif")
        self.images['R'] = pygame.image.load("../images/enemymissile.gif")
        self.images['U'] = pygame.image.load("../images/enemymissile.gif")
        self.images['D'] = pygame.image.load("../images/enemymissile.gif")
        self.image = self.images[self.direction]  # 炮弹的图片 由方向决定
        self.rect = self.image.get_rect()  # 获取边界
        self.rect.left = tank.rect.left + (tank.width - self.width) / 2
        self.rect.top = tank.rect.top + (tank.height - self.height) / 2
        self.live = True  # 炮弹是否消灭了
        self.good = True

    def move(self):
        if self.live:  # 如果炮弹存在
            if self.direction == 'L':
                if self.rect.left > 0:  # 判断是否在屏幕的左边的边界上
                    self.rect.left -= self.speed
                else:
                    self.live = False
            elif self.direction == 'R':
                if self.rect.right < TankeMain.width:
                    self.rect.right += self.speed
                else:
                    self.live = False
            elif self.direction == 'U':
                if self.rect.top > 0:
                    self.rect.top -= self.speed
                else:
                    self.live = False
            elif self.direction == 'D':
                if self.rect.bottom < TankeMain.height:
                    self.rect.bottom += self.speed
                else:
                    self.live = False

    # 炮弹击中坦克 第一种 我方坦克的炮弹击中敌方的坦克 第二种 敌方坦克的炮弹击中我方坦克
    def hit_tank(self):
        if self.good:
            hit_list = pygame.sprite.spritecollide(self, TankeMain.enemy_list, False)
            for e in hit_list:
                e.live = False
                self.live = False
                TankeMain.enemy_list.remove(e)  # 敌方坦克被击中删除坦克
                explode = Explode(self.screen, e.rect)
                TankeMain.explode_list.append(explode)  # 产生爆炸对象


# 爆炸类
class Explode(BaseItem):

    def __init__(self, screen, rect):
        super().__init__(screen)
        self.live = True
        self.images = [pygame.image.load("../images/blast1.gif"), \
                       pygame.image.load("../images/blast2.gif"), \
                       pygame.image.load("../images/blast3.gif"), \
                       pygame.image.load("../images/blast4.gif"), \
                       pygame.image.load("../images/blast5.gif"), \
                       pygame.image.load("../images/blast6.gif"), \
                       pygame.image.load("../images/blast7.gif")
                       ]
        self.step = 0
        self.rect = rect  # 爆炸的位置就是炮弹碰到坦克的位置.构建的时候把坦克的rect传入进来

    # display 这个方法是这整个系统中循环调用的,每隔0.05秒调用一次
    def display(self):
        if self.live:
            if self.step == len(self.images):  # 最后一张图片爆炸以及显示了
                self.live = False
            else:
                self.image = self.images[self.step]
                self.screen.blit(self.image, self.rect)
                self.step += 1


# 游戏中的墙
class Wall(BaseItem):
    def __init__(self, screen, left, top, width, height):
        super().__init__(screen)
        self.rect = Rect(left, top, width, height)
        self.color = (255, 0, 0)

    def display(self):
        self.screen.fill(self.color, self.rect)

    # 针对墙和其他的炮弹的碰撞检测
    def hit_other(self):
        if TankeMain.my_tank:
            is_hit = pygame.sprite.collide_rect(self, TankeMain.my_tank)
            if is_hit:
                TankeMain.my_tank.stop = True
                TankeMain.my_tank.stay()

        if TankeMain.enemy_list:
            hit_list = pygame.sprite.spritecollide(self, TankeMain.enemy_list, False)
            for e in hit_list:
                e.stop = True
                e.stay()

        if TankeMain.enemy_missile_list:
            hit_list = pygame.sprite.spritecollide(self, TankeMain.enemy_missile_list, False)
            for e in hit_list:
                e.live = False
                hit_list.remove(e)
        if TankeMain.my_tank_missle_list:
            hit_list = pygame.sprite.spritecollide(self, TankeMain.my_tank_missle_list, False)
            for e in hit_list:
                e.live = False
                hit_list.remove(e)


if __name__ == '__main__':
    game = TankeMain()
    game.startGame()
