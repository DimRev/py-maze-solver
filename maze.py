from graphics import Window, Cell
from common import Point
import time


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

    def get_cells(self):
        return self.__cells
