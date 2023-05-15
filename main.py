
from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


# def main():
#     win = Window(800, 600)
#     line = Line(Point(50, 50), Point(400, 400))
#     win.draw_line(line, "black")
#     win.wait_for_close()

def main():
    # win = Window(800, 600)

    # # Line Drawing
    # p1 = Point(50, 10)
    # p2 = Point(50, 100)
    # line = Line(p1, p2)
    # win.draw_line(line, "Red")

    # # Cell Drawing
    # cell = Cell(10, 10, 100, win)
    # cell.has_right_wall = False
    # cell.draw()

    # cell = Cell(110, 10, 100, win)
    # cell.has_left_wall = False
    # cell.draw()

    # # Line-Cell Drawing
    # cell_1 = Cell(10, 1, 100, win)
    # cell_2 = Cell(110, 1, 100, win)
    # cell_1.draw_move(cell_2)

    # Maze testing
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols,
                cell_size_x, cell_size_y, win, 1)
    maze.solve()

    win.wait_for_close()


main()
