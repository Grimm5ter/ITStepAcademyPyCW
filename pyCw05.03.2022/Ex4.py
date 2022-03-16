class Vector2D:

    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    @classmethod #Копируем из строки
    def from_string(cls, string):
        x, y = string.strip().split()
        x = float(x)
        y = float(y)
        return cls(x=x, y=y)



    @property #свойства работают на экземлярах
    def left(self):
        return Vector2D(-1, 0)

    @staticmethod
    def right():
        return Vector2D(-2, 0)

    @property
    def copy(self):
        return Vector2D(x=self.x, y=self.y)

class ColoredVector2D(Vector2D):

    def __init__(self, x=0.0, y=0.0, color="black"):
        super(ColoredVector2D, self).__init__(x=x, y=y)
        self.color = str(color)

if __name__ == '__main__':
    v1 = Vector2D(x=6, y=8.9)
    v2 = v1.left
    v3 = Vector2D.right() #Статический метод привязывается к имени класса
    v4 = v3.copy

    v5 = Vector2D.from_string("4 5")
    v6 = ColoredVector2D.from_string("8 0.6")

    print(type(v5))
    print(type(v6))
