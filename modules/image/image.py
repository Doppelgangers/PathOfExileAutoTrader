import numpy as np


class Image:

    def __init__(self, image: np.asarray):
        self.image = image

    def __dict__(self):
        return self.image

    def find_by_template(self, template: dict, accuracy: [float | int] = 0.8) -> (tuple[int], tuple[int]):
        pass

    def find_all_by_template(self, template: dict, accuracy: [float | int] = 0.8) -> dict[tuple[int], tuple[int]]:
        pass

    def find_by_color(self, hsv: (tuple[int] | dict[int]), size: float | int = 2) -> dict[tuple[int], tuple[int]]:
        pass

    