from unittest import TestCase
from sapper import *


class TestCell(TestCase):
    def test_boom(self):
        cl = create_field()
        create_bomb()
        for cell in cl.cells:
            if cell.bomb:
                cell.boom()
                assert cell.opened is True

    def test_set_label(self):
        cl = create_field()
        create_bomb()
        for cell in cl.cells:
            cell.set_label()
        for cell in cl.cells:
            assert cell.label == "!"
        for cell in cl.cells:
            cell.set_label()
        for cell in cl.cells:
            assert cell.label is None


class Test(TestCase):
    def test_create_field(self):
        cl = create_field()
        assert len(cl.cells) == pow(SIZE[0] // CELL_WIDTH, 2)
        for cell in cl.cells:
            assert isinstance(cell, Cell) is True

    def test_create_bomb(self):
        cl = create_field()
        create_bomb()
        bomb_count = 0
        for cell in cl.cells:
            if cell.bomb:
                bomb_count += 1
        assert bomb_count == BOMBS_COUNT

    def test_count_labels(self):
        cl = create_field()
        create_bomb()
        for cell in sample(cl.cells, k=15):
            cell.set_label()

        assert count_labels() == 15
