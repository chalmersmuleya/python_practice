task = input("Enter a new task for your to-do list: ")

with open("todo.txt", 'a') as file:
    file.write(task + "\n")


print("\n Current To-Do List:")
with open("todo.txt", "a+") as file:
    tasks = file.readlines()
    for t in tasks:
        print("- " + t.strip())