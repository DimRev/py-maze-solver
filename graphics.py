from tkinter import Tk, BOTH, Canvas


class Point:
    """docstring for Point."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Line:
    """docstring for Line."""

    def __init__(self, p1: Point, p2: Point):
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__p1.x, self.__p1.y, self.__p2.x, self.__p2.y, fill=fill_color, width=2
        )


class Cell(object):
    """docstring for Cell."""

    def __init__(
        self,
        p1: Point,
        p2: Point,
        has_left_wall=True,
        has_top_wall=True,
        has_right_wall=True,
        has_bottom_wall=True,
    ):
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self, canvas: Canvas, fill_color: str):
        p1 = Point(self.__x1, self.__y1)
        p2 = Point(self.__x2, self.__y1)
        p3 = Point(self.__x2, self.__y2)
        p4 = Point(self.__x1, self.__y2)
        if self.has_top_wall:
            top_line = Line(p1, p2)
            top_line.draw(canvas, fill_color)
        if self.has_right_wall:
            right_line = Line(p2, p3)
            right_line.draw(canvas, fill_color)
        if self.has_bottom_wall:
            bottom_line = Line(p3, p4)
            bottom_line.draw(canvas, fill_color)
        if self.has_bottom_wall:
            left_line = Line(p4, p1)
            left_line.draw(canvas, fill_color)


class Window:
    """docstring for Window."""

    def __init__(self, width: str, height: str):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell: Cell, fill_color: str):
        cell.draw(self.__canvas, fill_color)
