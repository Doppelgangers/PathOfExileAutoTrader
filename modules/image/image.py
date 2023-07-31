import cv2
import numpy as np


class Image:

    def __init__(self, image: np.asarray = np.asarray([]), path_img: str = ""):
        if image.size != 0:
            self.image = image
        elif path_img:
            self.image = cv2.imread(path_img)
        else:
            raise AttributeError

    def __dict__(self):
        return self.image

    def find_by_template(self, template: "Image", accuracy: [float | int] = 0.8) -> (tuple[int], tuple[int]):
        z, width_template, height_template = template.image.shape[::-1]
        result = cv2.matchTemplate(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY),
                                   cv2.cvtColor(template.image, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        location_of_matches = np.where(result >= accuracy)
        for pt in zip(*location_of_matches[::-1]):
            return (pt[0], pt[1]), (pt[0] + width_template, pt[1] + height_template)
        else:
            return None

    def __check_is_overlap(self, array: tuple, new_item: list, threshold_overlap: int = 3):
        """
        Функция проверяет перекрывает ли новый элемент существующие элементы
        array: список внесённых объектов --- формат [ ((x1, y1),(x2, y2)) , ... ]
        new_item: объект с координатами нового элемента --- формат [ x1, y1 ...]
        threshold_overlap: пороговое значение, на сколько пикселей изображения могут перекрывать друг друга
        """
        for reservation in array:
            if (abs(reservation[0][0] - new_item[0]) <= threshold_overlap) and \
                    (abs(reservation[0][1] - new_item[1]) <= threshold_overlap):
                return True
        return False

    def find_all_by_template(self, template: "Image", accuracy: [float | int] = 0.8, threshold_overlap=3) -> dict[
        tuple[int], tuple[int]]:
        z, width_template, height_template = template.image.shape[::-1]
        result = cv2.matchTemplate(cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY),
                                   cv2.cvtColor(template.image, cv2.COLOR_BGR2GRAY),
                                   cv2.TM_CCOEFF_NORMED)
        location_of_matches = np.where(result >= accuracy)
        match_list = []

        for pt in zip(*location_of_matches[::-1]):
            if not self.__check_is_overlap(match_list, pt, threshold_overlap):
                match_list.append(((pt[0], pt[1]), (pt[0] + width_template, pt[1] + height_template)))
        if len(match_list) > 0:
            return match_list
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
