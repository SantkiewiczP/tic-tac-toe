import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_place_returns_false_if_occupied(self):
        m = Matrix()
        m.place([0, 0], "X")

        self.assertFalse(m.place([0, 0], "O"))

    def test_place_if_occupied_does_not_set_symbol(self):
        m = Matrix()
        m.place([0, 0], "X")

        m.place([0, 0], "O")

        self.assertEqual(m.grid[0][0], "X")

    def test_place_returns_false_if_out_of_bounds_column_negative(self):
        m = Matrix()

        self.assertFalse(m.place([-1, 0], "X"))

    def test_place_returns_false_if_out_of_bounds_column_positive(self):
        m = Matrix()

        self.assertFalse(m.place([10, 0], "X"))

    def test_place_returns_false_if_out_of_bounds_row_negative(self):
        m = Matrix()

        self.assertFalse(m.place([0, -1], "X"))

    def test_place_returns_false_if_out_of_bounds_row_positive(self):
        m = Matrix()

        self.assertFalse(m.place([0, 10], "X"))

    def test_place_returns_true_if_not_occupied(self):
        pass
    def test_place_sets_symbol_if_not_occupied(self):
        pass

    def test_clear_all_slots_empty(self):
        m = Matrix()
        m.place([0, 0], "X")

        m.clear()

        for col in m.grid:
            for row in col:
                self.assertEqual("_", row)

    def test_constructor_all_slots_empty(self):
        m = Matrix()

        for col in m.grid:
            for row in col:
                self.assertEqual("_", row)