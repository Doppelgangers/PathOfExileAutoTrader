import logging
import mss
import ahk.window
import numpy as np
from ahk import AHK


class Window:

    _left: int = 0
    _top: int = 0
    _width: int = 0
    _height: int = 0

    def __init__(self, name_window, fix_offset: dict = {"x": 0, "y": 0, "w": 0, "h": 0}):
        self.__logger = logging.getLogger(__name__)
        self.fix_offset_window = fix_offset
        self.__ahk = AHK()
        self.name_window: str = name_window
        self.window = self.get_window_by_name(name_window=name_window)
        self.name_window = self.window.title.decode('utf-8')
        self.window.activate()
        self.update_window_position()

    @property
    def left(self):
        return self._left

    @property
    def top(self):
        return self._top

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def window_position_in_monitor(self) -> dict:
        self.update_window_position()
        return {"left": self._left, "top": self._top, "width": self._width, "height": self._height}

    def get_window_by_name(self, name_window) -> ahk.window:
        """
        Ищет окно приложения по имени и возвращает объект ahk.window, в сам класс изменений функиця не внсить
        """
        window = self.__ahk.find_window_by_title(bytes(name_window, "utf-8"))

        if not window:
            self.__logger.critical(f"Окно {name_window} не найдено!")
            raise Exception(f"Окна с именем '{name_window}' не найдено! ")

        self.__logger.debug(f"Окно {name_window} найдено.")
        return window

    def update_window_position(self, log_position: bool = False):
        """
        Обновляет данные объекта
        """
        size = self.window.rect
        self._left = size[0] + self.fix_offset_window["x"]
        self._top = size[1] + self.fix_offset_window["y"]
        self._width = size[2] + self.fix_offset_window["w"]
        self._height = size[3] + self.fix_offset_window["h"]

        self.__logger.debug(f""" Обновление позиции window.
        { f"Координаты окна {self.name_window} [left = {self._left}, top = {self._top}, width = {self._width}, height = {self._height}]" if log_position else f""}
        """)

    def set_size_window(self, width: int = 424, height: int = 727):
        """Изменяет размеры окна"""
        self.window.move(width=width, height=height)
        self.update_window_position()
        self.__logger.info(f"""Размер окна был изменён\n width = {width}, height = {height}""")

    def move_window_to(self, x: int = 0, y: int = 0):
        self.window.move(x=x, y=y)
        self.update_window_position()
        self.__logger.info("Окно перемещено программой.")

    def get_screenshot_window(self) -> np.asarray:
        """
        Возвращает скриншот окна в виде numpy массива
        """
        with mss.mss() as screenshot:
            return np.asarray(screenshot.grab(monitor=self.window_position_in_monitor))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_window = Window("Кальку")
    print(test_window.name_window)
    print(test_window.window_position_in_monitor)

