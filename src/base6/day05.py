import random


# 游戏
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        print("游戏初始化成功,可以开始了")

    def start_game(self):
        self.player1.cast()
        self.player2.cast()
        print(self.player1)
        print(self.player2)

    # 判断输赢
    def get_win(self):
        self.player1.guess_dice()
        self.player2.guess_dice()


# 玩家
class Player:
    def __init__(self, name, sex, *dice):
        self.name = name
        self.sex = sex
        self.dices = dice  # 该玩家拥有的筛子列表(元祖)

    def cast(self):  # 摇色子
        for dice in self.dices:
            dice.move()

    def guess_dice(self):  # 猜结果
        return (4, 2)

    def __str__(self):
        play_dice_count_list = [self.dices[0].count, self.dices[1].count, self.dices[2].count]
        return "姓名为%s,投掷的点数为%s" % (self.name, str(play_dice_count_list))


# 筛子
class Dice:
    def __init__(self):
        self.count = 0

    # 骰子滚动的方法,滚动之后返回最终的结果
    def move(self):
        self.count = random.randint(1, 6)
        pass


# 游戏开始之前,准备6个筛子
d1 = Dice()
d2 = Dice()
d3 = Dice()
d4 = Dice()
d5 = Dice()
d6 = Dice()

# 玩家信息
p1 = Player("player1", "男", d1, d2, d3)
p2 = Player("player2", "女", d4, d5, d6)

for i in range(0, 5):
    g = Game(p1, p2)
    g.start_game()
    print("第%d次游戏的情况------" % i)
