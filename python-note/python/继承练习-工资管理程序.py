class Person:
    def __init__(self, num, name, salary):
        self.num = num
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = f'工号：{self.num}的{self.name}工资为{self.salary}'
        return msg

    def getSalary(self):
        return self.salary


class Worker(Person):
    def __init__(self, num, name, salary, hours, per_hour):
        super(Worker, self).__init__(num, name, salary)
        self.hours = hours
        self.per_hour = per_hour

    def getSalary(self):
        money = self.hours * self.per_hour
        self.salary += money
        return self.salary


class Salesman(Person):
    def __init__(self, num, name, salary, sale_money, percent):
        super(Salesman, self).__init__(num, name, salary)
        self.sale_money = sale_money
        self.percent = percent

    def getSalary(self):
        money = self.sale_money * self.percent
        self.salary += money
        return self.salary


class Manager(Person):
    def __init__(self, num, name, salary):
        super(Manager, self).__init__(num, name, salary)


class SaleManager(Person):
    def __init__(self, num, name, salary, sale_money, percent):
        super(SaleManager, self).__init__(num, name, salary)
        self.sale_money = sale_money
        self.percent = percent

    def getSalary(self):
        money = self.sale_money * self.percent
        self.salary += money
        return self.salary


# 创建子类对象
King = Worker('001', 'King', 2000, 160, 100)
print(f'工号 {King.num} 的工人 {King.name}，本月薪资为{King.getSalary()}')

lucy = Salesman('002', 'Lucy', 5000, 5000000, 0.03)
print(f'工号 {lucy.num} 的工人 {lucy.name}，本月薪资为{lucy.getSalary()}')
