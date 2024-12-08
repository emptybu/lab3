import math

class Circle:
    def __init__(self, radius):  # Начальное определение родительского класса и атрибутов
        try:
            radius = float(radius)
            if radius <= 0:
                print("Радиус должен быть положительным числом больше нуля.")
                self._radius = None
            else:
                self._radius = radius
        except ValueError:
            print("Радиус должен быть числом.")
            self._radius = None

    @property  # Геттер для радиуса
    def radius(self):
        return self._radius

    @staticmethod  # Статический метод для вывода информации по команде
    def about():
        print("Программа выполнена командой разработчиков:\n"
              "1 разработчик: Шарафутдинов А.Б.\n"
              "2 разработчик: Щербина Л.А.\n"
              "3 разработчик: Фаткуллина Л.А.")
class Ball(Circle):
    def __init__(self, radius, height):  # Наследование от родительского класса, инициализация
        super().__init__(radius)
        try:
            height = float(height)
            if height <= 0:
                print("Высота должна быть положительным числом больше нуля.")
                self._height = None
            else:
                self._height = height
        except ValueError:
            print("Высота должна быть числом.")
            self._height = None
    @staticmethod
    def about():
        print("Программа выполнена командой разработчиков:\n"
              "1 разработчик: Шарафутдинов А.Б.\n"
              "2 разработчик: Щербина Л.А.\n"
              "3 разработчик: Фаткуллина Л.А.")

    def sector_volume(self, height=None):
        if self._radius is None:
            print("Объем шарового сектора не может быть рассчитан, так как радиус не был корректно задан.")
            return None
        if height is None:
            height = self._height
        if height is None:
            print("Высота не задана для расчета объема шарового сектора.")
            return None
        try:
            height = float(height)
            if height <= 0:
                print("Высота должна быть положительным числом больше нуля.")
                return None
            return (2 / 3) * math.pi * self.radius ** 2 * height
        except (ValueError, TypeError):
            print("Высота и радиус должны быть числами для вычисления объема шарового сектора.")
            return None

# Вывод информации о программе
Ball.about()

# Запуск основной программы
while True:
    try:
        radius = input("Введите радиус шара (или 'exit' для завершения): ")
        if radius.lower() == 'exit':
            print("Программа завершена.")
            break
        height = input("Введите высоту для расчета сектора (или 'exit' для завершения): ")
        if height.lower() == 'exit':
            print("Программа завершена.")
            break
        if radius and height:
            ball = Ball(radius, height)
            sector_volume = ball.sector_volume()
            if sector_volume is not None:
                print("Объем шарового сектора:", sector_volume)
            else:
                print("Радиус и высота должны быть заданы для выполнения расчетов.")
        print('')
    except Exception as e:
        print("Произошла ошибка:", e)
