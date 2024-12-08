class ElementFatkullina:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f"Name: {self.name}, Symbol: {self.symbol}, Number: {self.number}")


element = ElementFatkullina("Vanadium", "V", 23)

element.dump()
