shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")


def add_to_list(item):
    shopping_list.append(new_item)
    print("Added! List has {} items.".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()

while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

show_list()

def multiply(*args):
    count = 1
    is_list = []
    print(args)
    for i in args:
        print("loop started")
        if isinstance(i, list):
            print("a list was found")
            for x in i:
                count *= x
        if isinstance(i, dict):
            
        else:
            count *= i
    print("test")
    return count
print(multiply([2,2,2,2],2,[2]{2 : 2}))


