def note():
    print("What is the name of your note?")
    note_name = input("> ")
    print("Please write your note")
    note_contents = input("> ")
    f = open(note_name +".txt", "x")
    f = open(note_name +".txt", "a")
    f.write(note_contents)
    f.close()



print("Welcome to PyPlanner were we help you get on track")
print("Add a new [note] or start a new [timer],[alarm],[settings],or [quit]")
while True:
    choice = input("> ")
    if choice == "note":
        note()

