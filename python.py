#Loop Control Statements

fruits = ["apple", "mango", "litchi", "grapes"]

for fruit in fruits:
    if fruit == "litchi":
        break # Exits the loop if litchi is found
    print(fruit)
    
    print()
   
for fruit in fruits:
    if fruit == "litchi":
        continue # Skips the litchi to the iteration
    print(fruit)
    
    print()
   
for fruit in fruits:
    if fruit == "litchi":
        pass # Placeholder, no action is needed for litchi
    print(fruit)
    
    count = 0
    
    while count < 5:
        print(count)
        count += 1
        if count == 3:
            break # Exits the loop when the count  is reached = 3