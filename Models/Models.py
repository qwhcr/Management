import datetime


class Car:

    def __init__(self, *args):
        if len(args) == 0:
            self.__date = None
            self.__brand_name = None
            self.__weight = None
            self.__price = None
            self.__total_price = None
            self.__car_num = None
            self.__costumer_name = None
        elif len(args) == 1:
            args = str(args)
            attrs = args.split(" ")
            date_array = attrs[0].split("-")
            self.__date = datetime.datetime(int(date_array[0]), int(date_array[1]), int(date_array[2]))
            self.__brandName = attrs[1]
            self.__weight = float(attrs[2])
            self.__price = float(attrs[3])
            self.__total_price = float(attrs[3]) * float(attrs[2])
            self.__car_num = attrs[4]
            self.__costumer_name = attrs[5]
        else:
            self.__date = args[0]
            self.__brand_name = args[1]
            self.__weight = float(args[2])
            self.__price = float(args[3])
            self.__total_price = float(args[2]) * float(args[3])
            self.__car_num = args[4]
            self.__costumer_name = args[5]

    def get_date(self):
        return self.__date

    def set_date(self, date: datetime.date):
        self.__date = date

    def get_brand_name(self):
        return self.__brand_name

    def set_brand_name(self, brand_name: str):
        self.__brand_name = brand_name

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight: float):
        self.__weight = weight

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price

    def get_total_price(self):
        return self.__total_price

    def get_car_num(self):
        return self.__car_num

    def set_car_num(self, car_num: str):
        self.__car_num = car_num

    def get_costumer_name(self):
        return self.__costumer_name

    def set_costumer_name(self, costumer: str):
        self.__costumer_name = costumer

    def __str__(self):
        return str(self.get_date()).split(" ")[0],  self.get_brand_name()\
            , self.get_weight(), "吨 ", self.get_price(), "元/吨 总计：", self.get_total_price()\
            , "元 车号:", self.get_car_num(), + self.get_costumer_name()


class Costumer:
    def __init__(self, name: str):
        self.__name = name
        self.__bills = {}
        self.__payments = {}
        self.__cars = []

    def add_car(self, car: Car):
        self.__cars.append(car)

    def get_cars(self):
        return self.__cars

    def get_bills(self):
        return self.__bills

    def set_bill_entry(self, time: datetime.date, amount: float):
            self.__bills[time] = amount

    def add_bill_entry(self, time: datetime.date, amount: float):
        if time in self.__bills.keys():
            self.__bills[time] = self.__bills[time] + amount
        else:
            self.__bills[time] = amount

    def set_payment_entry(self, time:datetime.date, amount: float):
        self.__payments[time] = amount

    def add_payment_entry(self, time:datetime.date, amount: float):
        if time in self.__payments.keys():
            self.__payments[time] = self.__payments[time] + amount
        else:
            self.__payments[time] = amount

