import cv2
import numpy as np


class Image:

    def __init__(self, image: np.asarray):
        self.image = image

    def __dict__(self):
        return self.image

    def find_by_template(self, template: "Image", accuracy: [float | int] = 0.8) -> (tuple[int], tuple[int]):
        width_template, height_template = template.image.shape[::-1]
        result = cv2.matchTemplate(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY), cv2.cvtColor(template.image, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        location_of_matches = np.where(result >= accuracy)
        for pt in zip(*location_of_matches[::-1]):
            return {"x1": pt[0], "y1": pt[1], "x2": pt[0] + width_template, "y2": pt[1] + height_template}
        else:
            return None



    def find_all_by_template(self, template: dict, accuracy: [float | int] = 0.8) -> dict[tuple[int], tuple[int]]:
        width_template, height_template = template.image.shape[::-1]
        result = cv2.matchTemplate(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY),
                                   cv2.cvtColor(template.image, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        location_of_matches = np.where(result >= accuracy)
        matches = []
        for pt in zip(*location_of_matches[::-1]):
            matches.append({"x1": pt[0], "y1": pt[1], "x2": pt[0] + width_template, "y2": pt[1] + height_template})
            if len(matches) > 0:
                return matches
            else:
                return None

    def find_by_color(self, hsv: (tuple[int] | dict[int]), size: float | int = 2) -> dict[tuple[int], tuple[int]]:
        pass

    def check_color_hcv(self, hsv: (tuple[int] | dict[int])) -> int:
        hMin, sMin, vMin, hMax, sMax, vMax = hsv
        hsv_min = (hMin, sMin, vMin)
        hsv_max = (hMax, sMax, vMax)

        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        masc = cv2.inRange(hsv, hsv_min, hsv_max)
        moments = cv2.moments(masc, 1)
        dM01 = moments['m01']
        dM10 = moments['m10']
        dArea = moments['m00']

im = Image([])
im.find_by_template(im)
