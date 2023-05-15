from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point


class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "Black")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "White")
        if self.has_right_wall:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "Black")
        else:
            self._win.draw_line(
                Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "White")
        if self.has_top_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "Black")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "White")
        if self.has_bottom_wall:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "Black")
        else:
            self._win.draw_line(
                Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "White")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        if undo:
            color = "Grey"
        else:
            color = "Red"
        x_mid, y_mid = (self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2
        to_x_mid, to_y_mid = (
            to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid, to_y_mid),
                        Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, color)

        # moving right
        elif self._x2 > to_cell._x2:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, color)
            line = Line(Point(to_cell._x1, to_y_mid),
                        Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, color)
        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid, to_cell._y2),
                        Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, color)
            line = Line(Point(to_x_mid, to_y_mid),
                        Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, color)

        self._win.draw_line(
            Line(Point(x_mid, y_mid), Point(to_x_mid, to_y_mid)), color)
