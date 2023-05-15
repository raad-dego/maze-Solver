from graphics import Line, Point
from cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if seed is None:
            random.seed(seed)
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visted()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)]
                       for i in range(self._num_cols)]
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
        self._cells[self._num_cols -
                    1][self._num_rows-1].has_bottom_wall = False
        self._draw_cells(self._num_cols-1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit_list = []
            to_visit_index = 0
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit_list.append((i - 1, j))
                to_visit_index += 1
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit_list.append((i + 1, j))
                to_visit_index += 1
            # top
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit_list.append((i, j - 1))
                to_visit_index += 1
            # bottom
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit_list.append((i, j + 1))
                to_visit_index += 1
            # if there is nowhere to go from here, just break out
            if to_visit_index == 0:
                self._draw_cells(i, j)
                return

            direction_index = random.randrange(to_visit_index)
            di, dj = to_visit_list[direction_index]

            if di == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            elif di == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            elif dj == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            elif dj == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(di, dj)

    def _reset_cells_visted(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        self._solve_r(i=0, j=0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        # right
        if (i < self._num_cols-1
                and not self._cells[i][j].has_right_wall
                and not self._cells[i+1][j].visited
                ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)
        # left
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
            # top
        if (j > 0
                and not self._cells[i][j].has_top_wall
                and not self._cells[i][j-1].visited
                ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        # bottom
        if (j < self._num_rows-1
                and not self._cells[i][j].has_bottom_wall
                and not self._cells[i][j+1].visited
                ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False
