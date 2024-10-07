from graphics import Point, Line, Window

def main():
    win = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(400, 400)
    line = Line(point1, point2)
    win.draw_line(line, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()