running = True
checklist = list()

#CREATE
def create(item):
    checklist.append(item)

#READ
def read(index):
    if index < len(checklist):
        print(checklist[index])
    else:
        print("Index " + str(index) + " is invalid!")

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
    if index < len(checklist):
        checklist[index] = "{} {}".format("√",checklist[index])
    else:
        print("Index " + str(index) + " is invalid!")



#REMOVECOMPLETEDMARK
def remove_completed(index):
    if index < len(checklist):
        checklist[index] = checklist[index].replace("√","")
    else:
        print("Index " + str(index) + " is invalid!")


#SELECT
def select(function_code):
    #Create item
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input item: ")
        create(input_item)

    #Read item
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number to be read?: ")
        read(int(item_index))

    #List Items
    elif function_code == "P" or function_code == "p" or function_code == "L" or function_code == "l":
        list_all_items()

    #Mark Completed
    elif function_code == "D" or function_code == "d":
        item_index = user_input("Index Number to be marked completed?: ")
        mark_completed(int(item_index))

    #Mark UnCompleted
    elif function_code == "X" or function_code == "x":
        item_index = user_input("Index Number to be marked UNcompleted?: ")
        remove_completed(int(item_index))

    #Quit
    elif function_code == "Q" or function_code == "q":
        exit()

    #Catch Unknown Key
    else:
        print("This key is not an option:(")
    return True


#INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input

#TESTING
#def test():
    #create("purple sox")
    #create("red cloak")

    #print(read(0))
    #print(read(1))

    #update(0, "purple socks")
    #destroy(1)

    #print(read(0))

    #list_all_items()

    #mark_completed(0)

    #select("C")
    ##View the results
    #list_all_items()
    ## Call function with new value
    #select("R")
    ## View results
    #list_all_items()
    ## Continue until all code is run


#test()


while running:
    selection = user_input("Press C to add to list, R to Read from list, L to display list, D to mark completed, X to UNmark completed and Q to quit: ")
    select(selection)
