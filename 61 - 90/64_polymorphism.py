class Shape:
    def draw(self):
        raise NotImplementedError

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()