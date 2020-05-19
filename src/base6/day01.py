# 定义了一个类
class Car:
    def start(self):
        print("汽车启动")
    def print_car_info(self):
        print('汽车名称为%s,汽车颜色为%s'%(self.name, self.color))
# 创建对象
c = Car()
c.name = '迈腾'
c.color = '红色'
c.start()
c.print_car_info()