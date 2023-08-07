from database.db import Database_Task


def main():
    db = Database_Task()
    while True:
        if task := db.fetch_task():

            ...
            res = ''
            if res:
                task.status = "completed"
            else:
                task.status = "fail"

            db.session.commit()

            break

    if __name__ == "__main__":
        main()

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


