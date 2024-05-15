import unittest
from maze import Maze
from graphics import Window, Cell
from common import Point, Line


class Test(unittest.TestCase):
    def test_maze_create_cell(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)

        cells = m1.get_cells()

        self.assertEqual(len(cells), num_rows)
        self.assertEqual(len(cells[0]), num_cols)

    def test_point_creation(self):
        p1 = Point(10, 15)
        p2 = Point(20, 25)

        self.assertEqual(p1.x, 10)
        self.assertEqual(p1.y, 15)
        self.assertEqual(p2.x, 20)
        self.assertEqual(p2.y, 25)

    def test_line_length(self):
        p1 = Point(5, 0)
        p2 = Point(5, 5)
        p3 = Point(0, 0)
        p4 = Point(1.5, 2)
        l1 = Line(p1, p2)
        l2 = Line(p3, p4)

        self.assertEqual(l1.get_length(), 5.0)
        self.assertEqual(l2.get_length(), 2.5)

    def test_cell_area(self):
        p1 = Point(0, 0)
        p2 = Point(5, 5)
        c1 = Cell(None)
        c1.draw(p1, p2, "black")
        self.assertEqual(c1.area(), 25)


if __name__ == "__main__":
    unittest.main()
