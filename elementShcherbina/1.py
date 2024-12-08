class ElementSherbina:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


element = ElementSherbina("Ferrum", "Fe", 26)


print(f"Name: {element.name}, Symbol: {element.symbol}, Number: {element.number}")
