import logging
import datetime
import cv2
from sqlalchemy.orm import Session, selectinload

from database.db import Database, Database_Task
from modules.grids.inventory import Inventory_tab
from modules.grids.regular_tab import Regular_tab
from modules.grids.trade_grid import Trade_grid
from modules.image.image import Image
from modules.window.window import Window
import settings

from models import Base, Currency, Deal
import sqlalchemy


def main():
    db = Database_Task()
    print(db.fetch_task())

        # create_deal(session, name="Evil_doppelganger", item="Devil sword", price=10, currency="Chaos", league="Crushible", section="T1", left=1, top=1)
        # task = fetch_task(session)
        # task.price = 100
        # session.commit()
        # print(task)

        # sqlalchemy.update(Deal).





    # logging.basicConfig(level=logging.INFO)
    #
    # game_window = Window(settings.WINDOW_NAME, fix_offset=settings.OFFSET_WINDOW)
    #
    # img = Image(image=game_window.get_screenshot_window())
    #
    # template = Image(path_img=r"D:\dev\auro-poe\assets\chaos.png")

    # tab = Trade_grid(window=game_window)
    # pos1, pos2 = tab.find_chell(1, 1, bottom=True)
    # cv2.rectangle(img.image, pos1, pos2, (0, 0, 255), 2)

    # x= 0
    # for pos in img.find_all_by_template(template, accuracy=0.6):
    #     x += 1
    #     pos1, pos2 = pos
    #     cv2.rectangle(img.image, pos1, pos2, (0, 0, 255), 2)
    # print(x)

    # cv2.imshow("name", img.image)
    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
