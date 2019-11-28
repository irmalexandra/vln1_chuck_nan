LINE_LEN = 88
T_LEN = 8
TRUE_LEN = LINE_LEN + 2 * T_LEN
def print_NaN():
    print("\t███╗   ██╗ █████╗ ███╗   ██╗     █████╗ ██╗██████╗ ██╗     ██╗███╗   ██╗███████╗███████╗")
    print("\t████╗  ██║██╔══██╗████╗  ██║    ██╔══██╗██║██╔══██╗██║     ██║████╗  ██║██╔════╝██╔════╝")
    print("\t██╔██╗ ██║███████║██╔██╗ ██║    ███████║██║██████╔╝██║     ██║██╔██╗ ██║█████╗  ███████╗")
    print("\t██║╚██╗██║██╔══██║██║╚██╗██║    ██╔══██║██║██╔══██╗██║     ██║██║╚██╗██║██╔══╝  ╚════██║")
    print("\t██║ ╚████║██║  ██║██║ ╚████║    ██║  ██║██║██║  ██║███████╗██║██║ ╚████║███████╗███████║")
    print("\t╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝")
print("This product is a copyright of some stuff from some company\n")
print("\n\n{}\n{}".format("_" * TRUE_LEN, "_" * TRUE_LEN))
print_NaN()
print("{}\n{}".format("_" * TRUE_LEN, "_" * TRUE_LEN))
menu = ["1. Some stuff","  2. More stuff","  3. Bunch of more stuff","  4. There is so much stuff here like omg"]
menu2 = ["1. Lol stuff", "  2. IDk fam"]

print("|Menu:"," " * (TRUE_LEN - T_LEN), "|")
true_menu = "".join(menu)
true_menu2  = "".join(menu2)
print("|{}{}|".format(true_menu," " * (TRUE_LEN - len(true_menu)-1)))
print("|{}{}|".format(true_menu2," " * (TRUE_LEN - len(true_menu2)-1)))
thing = input("\nInput: ")

print("{}\n{}\n\n".format("_"*TRUE_LEN,"_"*TRUE_LEN))