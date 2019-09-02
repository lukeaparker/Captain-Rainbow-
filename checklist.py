checklist = list()


#CREATE
def create(item):
    checklist.append(item)

#READ
def read(index):
    return checklist[index]

#UPDATE
def update(index, item):
    checklist[index] = item

#DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
      print("{} {}".format(index, list_item))
      index +=1

def mark_completed(index):
    update(index,'{} {}'.format('√',read(index)))
    print(read(index))
#TEST
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
test()

