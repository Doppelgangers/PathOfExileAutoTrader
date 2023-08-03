

def parse_trades_for_regular_tab(message: str) -> dict:
    message = message.split("@От кого ")[1].split(":")
    name = message[0]
    if len(name.split(" ")) > 1:
        name = name.split(" ")[1]
    message = "".join(message[1:]).split("купить у вас ")[1]
    message = message.split(" за ")
    item = message[0].replace(",", "")
    message = message[1].split(" в лиге ")
    price, orb = message[0].split(" ")
    message = message[1].split(" (секция \"")
    league = message[0]
    message = message[1].split("\"; позиция ")
    section = message[0]
    message = message[1].split(" столбец, ")
    left = message[0]
    top = message[1].split(' ')[0]
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
    return data

