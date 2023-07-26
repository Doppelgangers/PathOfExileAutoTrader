import os

"""PATHS"""
BASE_DIR = "D:\dev\auro-poe"
TEMPLATES_DIR = os.path.join(BASE_DIR, "assets")


"""WINDOW"""
WINDOW_NAME = "Path of Exile"
WINDOW_WIDTH = 424
WINDOW_HEIGHT = 727
DEFAULT_WINDOW = {"x": 8, "y": 8, "w": -16, "h": -16}
OFFSET_WINDOW_HEADER = {"x": 0, "y": 23, "w": 0, "h": -23}
OFFSET_WINDOW = {key: DEFAULT_WINDOW[key] + OFFSET_WINDOW_HEADER[key] for key in DEFAULT_WINDOW}

"""TELEGRAM"""
TELEGRAM_API_KEY = '1219818658:AAERsK7cI_NPgqPz8naLk1EuS8822FtyudM'
TELEGRAM_CHAT_ID = '-1001240340647'


hotkey_take_loot = ""
hotkey_open_door = ""
hotkey_open_chest = ""

hsv_min_heist_chest_border_color, hsv_max_heist_chest_border_color = (0, 218, 171), (0, 230, 176)
hsv_min_white_text, hsv_max_white_text = (120, 23, 183), (120, 29, 230)
hsv_min_loot, hsv_max_loot = (0, 74, 190), (23, 255, 255)
