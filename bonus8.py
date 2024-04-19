date = input("Enter the date: ")
mood = input("Enter the mood today from 1 to 10?: ")
journal= input("Write down your thought: \n")

with open(f"journal/{date}.txt","w") as file :
    file.write(mood + "\n")
    file.write(journal)
