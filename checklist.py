checklist = list()

#CREATE
def create(item):
    checklist.append(item)

#READ
def read(index):
    if index < len(checklist):
        return checklist[index]
    else:
        return("Index " + str(index) + " is invalid!")

#UPDATE
def update(index, item):
    checklist[index]

#DESTROY
def destroy(index):
    checklist.pop(index)

#LISTITEMS
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index+= 1

#COMPLETEDMARK
def mark_completed(index):
    print("{} {}".format("√",checklist[index]))

#SELECT
def select(function_code):
    #Create item
    if function_code == "C" or "c":
        input_item = user_input("Input item: ")
        create(input_item)

    #Read item
    elif function_code == "R" or "r":
        item_index = user_input("Index Number to be read?")
        if item_index < len(checklist):
            read(item_index)
        else:
            return("Index " + str(index) + " is invalid!")

    #List Items
    elif function_code == "P" or "p" or "L" or "l":
        list_all_items()

    #Catch Unknown Key
    else:
        print("This key is not an option:(")

#INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input


#TESTING
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))

    list_all_items()

    mark_completed(0)

    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
test()
