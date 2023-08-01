from modules.grids.base_grid import Base_grid


class Trade_grid(Base_grid):

    def __init__(self, window):
        super().__init__(window=window)

    def find_chell(self, left: int, top: int,  bottom: bool = False) -> (tuple[int, int], tuple[int, int]):
        """
        params: left (number from 1 to 12, specifies the position of the cell in the row)
        params: top (number from 1 to 5, specifies the position of the cell in the column)
        return: postion (the position of the upper left corner of the cell and the position of the lower right corner of the cell)
        """
        width_inventory = self.window.height * 0.61714286
        width_trade = self.window.height * 0.63571429
        offset = round((self.window.width - width_inventory - width_trade)/2)
        base_offset_x = round(offset+width_trade*0.03926702)
        base_offset_y = round(self.window.height*0.19041096) if not bottom else round(self.window.height * 0.49657064)
        left -= 1
        top -= 1
        x1 = base_offset_x + self.inventory_chell_length * left
        y1 = base_offset_y + self.inventory_chell_length * top
        x2 = x1 + self.inventory_chell_length
        y2 = y1 + self.inventory_chell_length
        return (x1, y1), (x2, y2)
