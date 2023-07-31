import logging

import cv2

from modules.grids.inventory import Inventory_tab
from modules.grids.regular_tab import Regular_tab
from modules.image.image import Image
from modules.window.window import Window
import settings


def main():
    logging.basicConfig(level=logging.INFO)

    game_window = Window(settings.WINDOW_NAME, fix_offset=settings.OFFSET_WINDOW)

    img = Image(image=game_window.get_screenshot_window())

    template = Image(path_img=r"D:\dev\auro-poe\assets\chaos.png")

    # tab = Inventory_tab(window=game_window)
    # pos1, pos2 = tab.find_chell(1, 1)
    # cv2.rectangle(img, pos1, pos2, (0, 0, 255), 2)
    x= 0
    for pos in img.find_all_by_template(template, accuracy=0.6):
        x +=1
        pos1, pos2 = pos
        cv2.rectangle(img.image, pos1, pos2, (0, 0, 255), 2)
    print(x)


    cv2.imshow("name", img.image)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()


