from unittest import TestCase
from sapper import *


class Test(TestCase):
    def test_create_field(self):
        cl = create_field()
        assert len(cl.cells) == pow(SIZE[0] // CELL_WIDTH, 2)
        for cell in cl.cells:
            assert isinstance(cell, Cell) is True
