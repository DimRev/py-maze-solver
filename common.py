from graphics import Canvas


class Point:
    """A Point consisting for x, y coords."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    """A Line connecting two Points"""

    def __init__(self, p1: Point, p2: Point):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y, fill=fill_color, width=2
        )
