'''from colorama import Fore

colorama.init(autoreset=True)

Cash = int(input("Enter random number here (This is how much money a player has)"))
print("Money: ", Fore.GREEN + str(Cash) if Cash >= 0 else Fore.RED + str(Cash))
'''


class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)

    def color_text(code):
        return "\33[{code}m".format(code=code)


'''
background: allows background formatting. Accepts ANSI codes between 40 and 47, 100 and 107
style_text: corresponds to formatting the style of the text. Accepts ANSI code between 0 and 8
color_text:  Corresponds to the text of the color. Accepts ANSI code between 30 and 37, 90 and 97
'''

example_ansi = ANSI.background(
    97) + ANSI.color_text(36) + ANSI.style_text(4) + " Testi testi"
print(example_ansi)
