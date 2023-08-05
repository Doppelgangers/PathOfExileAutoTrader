import re


class Parser_poe_log:
    message_en = """2023/08/05 20:44:10 23767031 cffb0719 [INFO Client 7156] @От кого <•ÐiS•> Snow_Fairy: Hi, I would like to buy your Great Old One's Ward Corrugated Buckler listed for 1 alch in Crucible (stash tab "for sale 3"; position: left 6, top 9)"""

    @staticmethod
    def parse_trades_for_regular_tab(message: str) -> dict | None:
        rus_pattern = """@От кого (\S+)(?: (\S+))?: Здравствуйте, хочу купить у вас (.+) за ([0-9]+) (.+) в лиге (.+) \(секция "(.+)"; позиция: (\d+) столбец, (\d+) ряд"""
        en_pattern =  """@От кого (\S+)(?: (\S+))?: Hi, I would like to buy your (.+) listed for ([0-9]+) (.+) in (.+) \(stash tab "(.+)"; position: left (\d+), top (\d+)"""
        match = re.findall(rus_pattern, message)
        match2 = re.findall(en_pattern, message)
        if not match and not match2:
            return None
        match = match[0] if match else match2[0]
        name = match[0] if match[1] == '' else match[1]
        item = match[2]
        price = match[3]
        orb = match[4]
        league = match[5]
        section = match[6]
        left = match[7]
        top = match[8]

        return {"name": name,
                "item": item,
                "price": price,
                "orb": orb,
                "league": league,
                "section": section,
                "left": left,
                "top": top
                }


if __name__ == "__main__":
    p = Parser_poe_log
    message =      '2023/08/05 18:38:18 16215546 cffb0719 [INFO Client 2488] @От кого DIS Snow_Fairy: Здравствуйте, хочу купить у вас Естественная иерархия Талисман перогнильца за 100 alch в лиге Crucible (секция "Sale"; позиция: 11 столбец, 21 ряд)'
    message_en =  """2023/08/05 20:44:10 23767031 cffb0719 [INFO Client 7156] @От кого <•ÐiS•> Snow_Fairy: Hi, I would like to buy your Great Old One's Ward Corrugated Buckler listed for 1 alch in Crucible (stash tab "for sale 3"; position: left 6, top 9)"""
    print(p.parse_trades_for_regular_tab(message_en))
