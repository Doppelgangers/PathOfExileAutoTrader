from ahk import AHK


class Controller:

    def __init__(self):
        self.ahk = AHK()

    def click_on_coordinates(self, x, y, x2, y2):
        self.ahk.key_press("")
        self.ahk.click(x, y, direction="d")
        # self.ahk.mouse_move()
        self.ahk.click(x2, y2, direction="u")

if __name__ == "__main__":
    controller = Controller()

    controller.click_on_coordinates(2648, 445, 2700, 460)
