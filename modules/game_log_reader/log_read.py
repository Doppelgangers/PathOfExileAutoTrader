import re

import tailer

from database.db import Database_Task
from modules.game_log_reader.log_parser import Parser_poe_log
from settings import logfile_path

DB = Database_Task()
while True:
    for line in tailer.follow(open(logfile_path, encoding="UTF-8")):
        log = line.strip()

        if re.findall(r"секция | stash", log):
            if data := Parser_poe_log.parse_trades_for_regular_tab(log):
                new_deal = DB.create_deal(**data)

