import os
import pathlib
from dotenv import load_dotenv


"""PATHS"""
BASE_DIR = pathlib.Path(__file__).resolve().parent
TEMPLATES_DIR = os.path.join(BASE_DIR, "assets")
__DOTENV_PATH = BASE_DIR.joinpath(".env")
load_dotenv(dotenv_path=__DOTENV_PATH)


"""WINDOW"""
WINDOW_NAME = "Path of Exile"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DEFAULT_WINDOW = {"x": 8, "y": 8, "w": -16, "h": -16}
OFFSET_WINDOW_HEADER = {"x": 0, "y": 23, "w": 0, "h": -23}
OFFSET_WINDOW = {key: DEFAULT_WINDOW[key] + OFFSET_WINDOW_HEADER[key] for key in DEFAULT_WINDOW}

"""TELEGRAM"""
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


# hotkey_take_loot = ""
# hotkey_open_door = ""
# hotkey_open_chest = ""

# hsv_min_heist_chest_border_color, hsv_max_heist_chest_border_color = (0, 218, 171), (0, 230, 176)
# hsv_min_white_text, hsv_max_white_text = (120, 23, 183), (120, 29, 230)
# hsv_min_loot, hsv_max_loot = (0, 74, 190), (23, 255, 255)


"""GAME SETTINGS"""
logfile_path = pathlib.Path('D:\SteamLibrary\steamapps\common\Path of Exile\logs\Client.txt')

"""DATA BASE"""
NAME_DATABASE = "database.db"
DB_PATH = BASE_DIR.joinpath(NAME_DATABASE)
SQLALCHEMY_PATH = f"sqlite:///{DB_PATH}"
SQLALCHEMY_ECHO = False