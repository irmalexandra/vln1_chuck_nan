creation_process_dict = {1: get_input("Country: "), 2: get_input("Airport: ")}

def get_input(string):
    return input(string)
destination = Destination()
create_list = []
print("-"*30)
for key, value in creation_process_dict:
    print("-"*30)
    print("Create Destination ({}/6)".format(key))
    print("-"*30)
    input = value

    create_list.append(input)
