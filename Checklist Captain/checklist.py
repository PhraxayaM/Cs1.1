checklist = list()
# checklist.append("Hello")
# print(checklist)
# checklist.append("World")
# print(checklist)

def create(item):
    checklist.append(item)
def read(index):
    return checklist[index]
# checklist = ['Hello', 'World']
# checklist[1] = "Cats"
# print(checklist)

def update(index, item):
    checklist[index] = item
# checklist = ['Hello', 'World']
# checklist.pop(1)
# print(checklist)

def destroy(index):
    checklist.pop(index)
def list_all_items():
    index = 0
    for list_item in checklist:
    # print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

# def mark_completed(index):
    # Add code here that marks an item as completed
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        print(read(int(item_index)))

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # Stop loop
        return False

    # Catch all
    else:
         print("Unknown Option")
    return True




# while condition:
    # Run this code



def test():
    create("purple sox")
    create("purple sox")
    create("red cloak")
    list_all_items()
    # Add your testing code here
#     print(read(0))
#     print(read(1))
#     update(0, "purple socks")
#     destroy(1)
#     print(read(0))
#     select("C")
#     list_all_items()
# # Call function with new value
#     select("R")
# # View results
#     list_all_items()
#     select("U")
#     list_all_items()
#     select("D")
#     list_all_items()
#     user_value = user_input("Please enter a value:")
#     print(user_value)

list_all_items()

test()
running = True
while running:
    selection = user_input(
    "Press C to add to list, R to read from list, and P to display to list, and Q to quit")
    running = select(selection.upper())
