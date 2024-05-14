from graphics import Window, Line, Point, Cell


def main():
    win = Window(800, 600)
    p1 = Point(10, 10)
    # p2 = Point(10, 20)
    p3 = Point(40, 80)
    # p4 = Point(20, 10)
    # l1 = Line(p1, p2)
    # l2 = Line(p2, p3)
    # l3 = Line(p3, p4)
    # l4 = Line(p4, p1)
    # win.draw_line(l1, "black")
    # win.draw_line(l2, "black")
    # win.draw_line(l3, "black")
    # win.draw_line(l4, "black")
    cell = Cell(p1, p3)
    win.draw_cell(cell, "black")
    win.wait_for_close()


main()
