LINE_LEN = 88
T_LEN = 8
TRUE_LEN = LINE_LEN + 2 * T_LEN
distinguisher = "{}\n{}\n\n".format("_"*TRUE_LEN,"_"*TRUE_LEN)
import string
print(string.ascii_letters)

def print_NaN():
    print("\t███╗   ██╗ █████╗ ███╗   ██╗     █████╗ ██╗██████╗ ██╗     ██╗███╗   ██╗███████╗███████╗")
    print("\t████╗  ██║██╔══██╗████╗  ██║    ██╔══██╗██║██╔══██╗██║     ██║████╗  ██║██╔════╝██╔════╝")
    print("\t██╔██╗ ██║███████║██╔██╗ ██║    ███████║██║██████╔╝██║     ██║██╔██╗ ██║█████╗  ███████╗")
    print("\t██║╚██╗██║██╔══██║██║╚██╗██║    ██╔══██║██║██╔══██╗██║     ██║██║╚██╗██║██╔══╝  ╚════██║")
    print("\t██║ ╚████║██║  ██║██║ ╚████║    ██║  ██║██║██║  ██║███████╗██║██║ ╚████║███████╗███████║")
    print("\t╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝")



def print_main_menu():
    menu = ["1. Some stuff","  2. More stuff","  3. Bunch of more stuff","  4. There is so much stuff here like omg"]
    menu2 = ["1. Lol stuff", "  2. IDk fam"]
    true_menu = "".join(menu)
    true_menu2  = "".join(menu2)
    print("This product is a copyright of some stuff from some company\n")
    print(distinguisher)
    print_NaN()
    print(distinguisher)
    print("|{}{}|".format(true_menu," " * (TRUE_LEN - len(true_menu)-1)))
    print("|{}{}|".format(true_menu2," " * (TRUE_LEN - len(true_menu2)-1)))

print_main_menu()