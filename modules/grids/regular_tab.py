from .base_grid import Base_grid


class Regular_tab(Base_grid):

    def __init__(self, window):
        super().__init__(window=window)

    def find_chell(self, left: int, top: int, is_folder=False) -> (tuple[int, int], tuple[int, int]):
        """
        params: left (number from 1 to 12, specifies the position of the cell in the row)
        params: top (number from 1 to 12, specifies the position of the cell in the column)
        params: is_folder (If your tab is in a folder, set the flag to True)
        return: postion (the position of the upper left corner of the cell and the position of the lower right corner of the cell)
        """
        base_offset_x = 12
        base_offset_y = round(self.window.height * 0.1256)
        if is_folder:
            base_offset_y += round(self.window.height * 0.032)
        left -= 1
        top -= 1
        x1 = base_offset_x + self.inventory_chell_length * left
        y1 = base_offset_y + self.inventory_chell_length * top
        x2 = x1 + self.inventory_chell_length
        y2 = y1 + self.inventory_chell_length
        return (x1, y1), (x2, y2)
