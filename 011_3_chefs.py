class AbstractCook:

    food = ""
    beverage = ""

    def __init__(self):
        self.food_total = 0
        self.beverage_total = 0

    def add_food(self, food_amount, food_price):
        self.food_total += food_amount * food_price

    def add_drink(self, drink_amount, drink_price):
        self.beverage_total += drink_amount * drink_price

    def total(self):
        f, b = self.food_total, self.beverage_total
        return f"{self.food}: {f}, {self.beverage}: {b}, Total: {f+b}"


class JapaneseCook(AbstractCook):
    food = "Sushi"
    beverage = "Tea"


class RussianCook(AbstractCook):
    food = "Dumplings"
    beverage = "Compote"


class ItalianCook(AbstractCook):
    food = "Pizza"
    beverage = "Juice"


if __name__ == '__main__':

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"

    print("OK")
