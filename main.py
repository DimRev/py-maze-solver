from graphics import Window, Cell
from common import Point


def main():
    win = Window(800, 600)
    p1 = Point(10, 10)
    p2 = Point(40, 40)

    p3 = Point(40, 10)
    p4 = Point(70, 40)

    p5 = Point(70, 10)
    p6 = Point(100, 40)

    c1 = Cell(win)
    c2 = Cell(win)
    c3 = Cell(win)

    c1.draw(p1, p2, "black")
    c2.draw(p3, p4, "black")
    c3.draw(p5, p6, "black")
    c3.draw_move(c2)
    c2.draw_move(c1, undo=True)

    win.wait_for_close()


main()
