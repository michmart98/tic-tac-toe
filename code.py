import os



### this is a method to clear the diplay of our console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# now, to clear the screen
cls()