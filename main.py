import ahk
import keyboard
import cv2
from ahk import AHK

from modules.grids.regular_tab import Regular_tab
from modules.window.window import Window
import settings




def main():

    offset_windows = {"x": 8, "y": 8, "w": -16, "h": -16}
    offset_head = {"x": 0, "y": 23, "w": 0, "h": -23}
    summed_offset = {key: offset_windows[key] + offset_head[key] for key in offset_windows}

    game_window = Window(settings.WINDOW_NAME, fix_offset=summed_offset)
    # if not game_window.window.is_maximized():
    #     game_window.window.maximize()

    tab = Regular_tab(game_window)
    lt, rb = tab.find_chell(9, 11)
    x,y = lt
    ahk.AHK().click(x+game_window.left,y+game_window.top)
    lt, rb = tab.find_chell(2, 2)
    x, y = lt
    ahk.AHK().click(x+game_window.left,y+game_window.top)
    lt, rb = tab.find_chell(2, 3)
    x, y = lt
    ahk.AHK().click(x + game_window.left, y + game_window.top)

    img = game_window.get_screenshot_window()
    # print(img)
    # for stroka in range(1, 13):
    #     for riad in range(1, 13):
    #         find_chell(game_window, img, stroka, riad, False)
    #     find_chell(game_window, img, 12, 12, False)
    #     find_chell(game_window, img, 1, 1, False)
    # cv2.imshow("qwer", img)
    cv2.waitKey(0)

    # offset_windows = {"x": 8, "y": 8, "w": -16, "h": -16}
    # offset_head = {"x": 0, "y": 23, "w": 0, "h": -23}
    # summed_offset = {key: offset_windows[key] + offset_head[key] for key in offset_windows}
    # paint_window = Window("Без", fix_offset=summed_offset)
    # paint_window.click(x= 150, y = 150)
    # ahk = AHK()
    # ahk.mouse_move(x= paint_window.left +150, y = paint_window.top+150)
    # ahk.key_down("Shift")
    # ahk.click(direction = "D")
    # ahk.mouse_move(x= paint_window.left +250, y = paint_window.top+160)
    # ahk.click(direction = "U")
    # ahk.key_up("Shift")
    # img = paint_window.get_screenshot_window()
    # cv2.imshow("qwer", img)
    # cv2.waitKey(0)
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

