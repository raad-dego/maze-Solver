import unittest
from maze import Maze


class Tests(unittest.TestCase):
    # def test_maze_create_cells(self):
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m1._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m1._cells[0]),
    #         num_rows,
    #     )

    # def test_maze_different_dimensions(self):
    #     num_cols = 8
    #     num_rows = 6
    #     m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m2._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m2._cells[0]),
    #         num_rows,
    #     )

    # def test_maze_zero_dimensions(self):
    #     num_cols = 0
    #     num_rows = 0
    #     m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     self.assertEqual(
    #         len(m3._cells),
    #         num_cols,
    #     )
    #     self.assertEqual(
    #         len(m3._cells),
    #         0,
    #     )

    def test_break_exit(self):
        num_cols = 12
        num_rows = 10
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m4._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m4._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_visited_false(self):
        num_rows = 12
        num_cols = 16
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Check that the top-left cell has no top walls
        for col in m5._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
