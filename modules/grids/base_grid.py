import cv2
import numpy as np


class Base_grid:

    def __init__(self, window):
        self.window = window
        self.inventory_chell_length = round(self.window.height * 0.0482579)

    def find_chell(self, left: int, top: int) -> (tuple[int, int], tuple[int, int]):
        return (0, 0), (0, 0)

