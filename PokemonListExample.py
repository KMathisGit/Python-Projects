pokemonCantoList = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur']
pokemonJohtoList = ['Chikorita', 'Cyndaquil', 'Totodile']
print("\nThe Johto Pokemon list:",pokemonJohtoList)
while True:
    print("\n\nThe Canto Pokemon list:",pokemonCantoList)
    print("=========== THE 9 LIST COMMANDMENTS ===========")
    print("1. Append object to list.\n",
          "2. Count objects in list.\n",
          "3. Extend a list to another.\n",
          "4. Return index of object.\n",
          "5. Insert object at index.\n",
          "6. Pop list (removes & returns last).\n",
          "7. Remove object from list.\n",
          "8. Reverse order of list.\n",
          "9. Sort objects of list.\n",sep='')
    choice = int(input("Which function would you like to do?"))
    if(choice == 0):
        break
    def append():
        appendingItem = input("Enter object you wish to append to list:")
        pokemonCantoList.append(appendingItem)
    def count():
        countObject = input("Enter object you wish to count:")
        print(countObject,"was found",pokemonCantoList.count(countObject),"times")
    def extend():
        pokemonCantoList.extend(pokemonJohtoList)
        print(pokemonCantoList)
    def returnIndex():
        indexChoice = input("Enter object you wish to return index of:")
        print(pokemonCantoList.index(indexChoice))
    def insert():
        insertObject = input("Enter object you wish to insert:")
        indexChoice = int(input("Enter index you wish to insert at:"))
        pokemonCantoList.insert(indexChoice, insertObject)
    def pop():
        pokemonCantoList.pop()
    def remove():
        removeObject = input("Enter object you wish to remove:")
        pokemonCantoList.remove(removeObject)
    def reverse():
        pokemonCantoList.reverse()
    def sort():
        pokemonCantoList.sort()
    commandmentChoices = {
               1 : append,
               2 : count,
               3 : extend,
               4 : returnIndex,
               5 : insert,
               6 : pop,
               7 : remove,
               8 : reverse,
               9 : sort
    }
    commandmentChoices[choice]()




