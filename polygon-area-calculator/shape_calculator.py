class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return pow(pow(self.width, 2) + pow(self.height, 2), .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for line in range(0, self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape):
        if shape.width > self.width or shape.height > self.height:
            return 0
        else:
            return (self.width // shape.width) * (self.height // shape.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.width, self.height = side, side

    def set_width(self, width):
        self.width, self.height = width, width

    def set_height(self, height):
        self.height, self.width = height, height
