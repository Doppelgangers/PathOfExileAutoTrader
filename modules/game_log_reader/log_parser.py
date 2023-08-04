

class Parser_poe_log:

    @staticmethod
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

        return {"name": name,
                "item": item,
                "price": price,
                "orb": orb,
                "league": league,
                "section": section,
                "left": left,
                "top": top
                }


"///TODO: проверить разделение по словам на разных языках"
# import re
#
# text = "Hello world! This is a sample text."
#
# # List of possible words to split the text
# possible_words = ["world", "sample"]
#
# # Create a regular expression pattern by joining the possible words with the "|" OR operator
# pattern = r"\b(" + "|".join(map(re.escape, possible_words)) + r")\b"
#
# # Split the text using the pattern
# result = re.split(pattern, text)
#
# # Print the result
# print(result)