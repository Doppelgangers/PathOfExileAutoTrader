import logging

import cv2

from modules.grids.inventory import Inventory_tab
from modules.grids.regular_tab import Regular_tab
from modules.window.window import Window
import settings


def main():
    logging.basicConfig(level=logging.INFO)

    game_window = Window(settings.WINDOW_NAME, fix_offset=settings.OFFSET_WINDOW)

    tab = Inventory_tab(window=game_window)
    img = game_window.get_screenshot_window()

    pos1, pos2 = tab.find_chell(1, 1)
    cv2.rectangle(img, pos1, pos2, (0, 0, 255), 2)

    cv2.imshow("name", img)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()


