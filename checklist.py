checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

def create(item):
    checklist.append('Blue')

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

#TEST
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