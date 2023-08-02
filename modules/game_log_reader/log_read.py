import tailer
from settings import logfile_path
while True:
    for line in tailer.follow(open(logfile_path, encoding="UTF-8")):
        log = line.strip()
        try:
            mas = log.split("@От кого ")[1].split(":")
            name = mas[0]
            if name.find(" "):
                name = name.split(" ")[1]
            mas = "".join(mas[1:]).split("купить у вас ")[1]
            mas = mas.split(" за ")
            item = mas[0].replace(",", "")
            mas = mas[1].split(" в лиге ")
            price, orb = mas[0].split(" ")
            mas = mas[1].split(" (секция \"")
            league = mas[0]
            mas = mas[1].split("\"; позиция ")
            section = mas[0]
            mas = mas[1].split(" столбец, ")
            left = mas[0]
            top = mas[1].split(' ')[0]

            print(f"""
            Покупатель: {name}
            Покупает: {item}
            За: {price} - {orb}
            В лиге: {league}
            Находится по координатам (left: {left}, top: {top}) в секции {section}
            """)
            data = {"name": name,
                    "item": item,
                    "price": price,
                    "orb": orb,
                    "league": league,
                    "section": section,
                    "left": left,
                    "top": top
                    }
            print(data)
        except:
            pass
#
log2 = '2023/08/01 17:33:18 21682453 cffb0719 [INFO Client 7764] @От кого <•ÐiS•> Snow_Fairy: Здравствуйте, хочу купить у вас Разумный стимул, Сапоги крови за 4 divine в лиге Crucible (секция "T1"; позиция: 11 столбец, 11 ряд)'

log_string = '2023/08/01 16:35:50 18233718 cffb0719 [info client 7764] @От кого <poour> howiwander: Здравствуйте, хочу купить у вас Громадный виток, Железное кольцо за 20 chaos в лиге crucible (секция "t5"; позиция: 12 столбец, 7 ряд)'

