from termcolor import colored,cprint
from os import system

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

#SELECT
def select(function_code):
    try:
  
      
      # Create item
      if function_code == "C":
          input_item = user_input("Input item:")
          create(input_item)

      # Read item
      elif function_code == "R":
          item_index = int(user_input("Index Number?"))
          read(item_index)

      #Update
      elif function_code == "U":
        update_item = user_input("item")
        update_index = int(user_input("Index"))
        update(update_index, update_item)

      #Destroy 
      elif function_code == "D":
          index = int(user_input("index: "))
          destroy(index)

      # Print all items
      elif function_code == "P":
          list_all_items()
      elif function_code == "Q":
          # This is where we want to stop our loop
          return False
      elif function_code == "CL":
        system('clear')
      


      # Catch all
      else:
          print("Unknown Option")
      return True
    except ValueError:
      print("woops please input an ineger")
      return True
    except IndexError:
      print("woops please input an index in range")
      return True

#USER INPUT
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = str.upper(input(prompt))
    cprint(user_input, "red")
    return user_input

running = True
while running:
    selection = user_input(
        "Press D to destroy item, Press C to add to list, R to Read from list, P to display list, cl to quit, and Q to quit, ")
    running = select(selection)



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

    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    user_value = user_input("Please Enter a value:")
    print(user_value)
test()

