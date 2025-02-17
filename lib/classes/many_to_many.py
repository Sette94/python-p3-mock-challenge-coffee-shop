class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str) and 3 <= len(val) and not hasattr(self, "name"):
            self._name = val

    def orders(self):
        # What do I have in my Coffee class, self.name  (Name of the coffee)
        # Where is all the data = Order.all contains Coffee class

        # Through a For loop which works
        # coffee_orders = []
        # for order in Order.all:
        #     if order.coffee == self:
        #         coffee_orders.append(order)
        # return coffee_orders

        # Through list consolidation
        # return ["what we want retunr"   "Our for loop through the data" "Logic the work the data"]
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        # This is the right answer
        # return list(set([order.customer for order in Order.all if order.coffee == self]))

        # This is the right answer cut down
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        # number_of_orders = 0

        # for order in Order.all:
        #     if order.coffee == self:
        #         number_of_orders += 1
        # return number_of_orders

        return len(self.orders())

    def average_price(self):
        # For an average we need Price/# of Orders

        total_price = 0
        for order in Order.all:
            # order  =  order.price, order.customer, order.coffee
            if order.coffee == self:
                total_price += order.price

        return total_price/self.num_orders()


class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if isinstance(val, str) and 1 <= len(val) <= 15:
            self._name = val

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in Order.all if order.customer == self]))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.getter
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if isinstance(val, float) and 1.0 <= val <= 10.0 and not hasattr(self, "price"):
            self._price = val

    @property
    def customer(self):
        return self._customer

    @customer.getter
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, val):
        if isinstance(val, Customer):
            self._customer = val

    @property
    def coffee(self):
        return self._coffee

    @coffee.getter
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, val):
        if isinstance(val, Coffee):
            self._coffee = val
