from .base_grid import Base_grid


class Inventory_tab(Base_grid):

    def __init__(self, window):
        super().__init__(window=window)

    def find_chell(self, left: int, top: int) -> (tuple[int, int], tuple[int, int]):
        """
        params: left (number from 1 to 12, specifies the position of the cell in the row)
        params: top (number from 1 to 5, specifies the position of the cell in the column)
        return: postion (the position of the upper left corner of the cell and the position of the lower right corner of the cell)
        """
        base_offset_x = (self.window.width - 12) - (self.inventory_chell_length * 12 )
        base_offset_y = round(self.window.height * 0.548)
        left -= 1
        top -= 1
        x1 = base_offset_x + self.inventory_chell_length * left
        y1 = base_offset_y + self.inventory_chell_length * top
        x2 = x1 + self.inventory_chell_length
        y2 = y1 + self.inventory_chell_length
        return (x1, y1), (x2, y2)
