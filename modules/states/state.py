import re

import settings
from modules.window.window import Window


class States:

    def __init__(self):
        pass

    def is_game_not_running(self):
        try:
            test = Window(settings.WINDOW_NAME, fix_offset=settings.OFFSET_WINDOW)
            return True
        except Exception:
            return False

    def is_menu(self):
        return False

    def is_character_selection(self):
        return False

    def is_encampments(self):
        return False

    def is_hideout(self):
        return False

    def is_open_stash(self):
        return False

    def is_waiting_trade(self):
        return False

    def is_trade(self):
        return True

    def check_state(self):
        for func in self.__class__.__dict__:
            if re.findall(r"\bis_", func):
                if eval(f"self.{func}()"):
                    return func[3:]


s = States()
s.check_state()


