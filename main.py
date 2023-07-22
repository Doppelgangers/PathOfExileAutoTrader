import keyboard
import cv2
from modules.window.window import Window
import settings


def find_chell(game_window, img, left, top, is_folder=False):
    inventory_chell_length = round(game_window.height * 0.048)
    base_x = 12
    base_y = round(game_window.height * 0.1256)
    if is_folder:
        base_y += round(game_window.height * 0.032)
    left = left - 1
    top = top - 1
    x1 = base_x + inventory_chell_length * left
    y1 = base_y + inventory_chell_length * top
    x2 = x1 + inventory_chell_length
    y2 = y1 + inventory_chell_length
    cv2.rectangle(img, (x1, y1), (x2, y2), (244, 103, 80), 2)
    return (x1, y1), (x2, y2)


def main():

    offset_windows = {"x": 8, "y": 8, "w": -16, "h": -16}
    offset_head = {"x": 0, "y": 23, "w": 0, "h": -23}
    summed_offset = {key: offset_windows[key] + offset_head[key] for key in offset_windows}

    game_window = Window(settings.WINDOW_NAME, fix_offset=summed_offset)
    # if not game_window.window.is_maximized():
    #     game_window.window.maximize()

    img = game_window.get_screenshot_window()
    # print(img)
    for stroka in range(1, 13):
        for riad in range(1, 13):
            find_chell(game_window, img, stroka, riad, False)
        find_chell(game_window, img, 12, 12, False)
        find_chell(game_window, img, 1, 1, False)
    cv2.imshow("qwer", img)
    cv2.waitKey(0)


    #
    #     stash = Template(os.path.join(settings.TEMPLATES_DIR, "stash_ru.png"))
    #     # finder = Base_finder().find_in_object(img, stash)
    #     # print(finder)
    #

    #     # while True:
    #     #     screenShot = screenshot.grab(monitor_manager.monitor)
    #     #     img_array = np.array(screenshot.grab(monitor_manager.monitor))
    #     #

# def print_zero():
#     print("0")

if __name__ == "__main__":
    main()
    # keyboard.add_hotkey('Ctrl+Shift+A', print_zero)
    # keyboard.wait('Ctrl+Esc')

