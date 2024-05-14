import time

from tkinter import Tk, BOTH, Canvas
from common import Line


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

    def draw_line(self, line: "Line", fill_color: str):
        line.draw(self.__canvas, fill_color)

    def draw_cell(self, cell: "Cell", fill_color: str):
        cell.draw(self.__canvas, fill_color)

    def draw_move(self, from_cell: "Cell", to_cell: "Cell", undo=False):
        from_cell.draw_move(self.__canvas, to_cell, undo)


from graphics import Window
from common import Line, Point


class Cell:
    """A Cell connecting 4 points with lines"""

    def __init__(
        self,
        win: "Window",
        has_left_wall=True,
        has_top_wall=True,
        has_right_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.__win = win

    def draw(self, p1: "Point", p2: "Point", fill_color: str):
        if self.__win is None:
            return
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p2.y
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, fill_color)
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, fill_color)
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, fill_color)
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, fill_color)

    def draw_move(self, to_cell: "Cell", undo=False):
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1

        fill_color = "red"
        if undo:
            fill_color = "gray"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.__win.draw_line(line, fill_color)


class Maze:
    """A Maze built out of cell"""

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__create_cells()

    def __create_cells(self):
        self.__cells = []
        for j in range(self.__num_rows):
            row = []
            for i in range(self.__num_cols):
                cell = Cell(self.__win)
                row.append(cell)
            self.__cells.append(row)

        for j in range(self.__num_rows):
            for i in range(self.__num_cols):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return

        cell = self.__cells[j][i]

        offset_x = i * self.__cell_size_x
        offset_y = j * self.__cell_size_y

        curr_x1 = self.__x1 + offset_x
        curr_y1 = self.__y1 + offset_y

        curr_x2 = self.__x1 + self.__cell_size_x + offset_x
        curr_y2 = self.__y1 + self.__cell_size_y + offset_y

        p1 = Point(curr_x1, curr_y1)
        p2 = Point(curr_x2, curr_y2)

        cell.draw(p1, p2, "black")
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
