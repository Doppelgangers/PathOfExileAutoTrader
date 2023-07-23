import cv2
import numpy as np


class Base_grid:

    def __init__(self, window):
        self.window = window
        self.inventory_chell_length = round(self.window.height * 0.048)


