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

#TESTING
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(read(1))

test()
