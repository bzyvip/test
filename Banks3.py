class Banks():
    """定义银行类"""

    def __init__(self,uname):
        self.__name = uname
        self.__balance = 0
        self.__bankname = "Taipei Bank"
        self.__rate = 30                    # 预设美金与台币之间的汇率
        self.__service_charge = 0.01        # 汇换的服务费

    def save_money(self,money):
        self.__balance += money
        print("存款",money,"完成")

    def withdraw_money(self,money):
        self.__balance -= money
        print("提款",money,"完成")

    def get_balance(self):
        print(self.__name.title(),"目前余额",self.__balance)

    def usa_to_taiwan(self,usa_d):          # 美金换台币方法
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self,usa_d):             # 计算换汇这是私有方法
        return int(usa_d * self.__rate * (1 - self.__service_charge))
    




hungbank = Banks("hung")
usdallor = 50
print(usdallor,"美金可以换",hungbank.usa_to_taiwan(usdallor),"台币")
