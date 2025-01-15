text = input("Enter text to append to file: ")
with open("example.txt", "a") as file:
    file.write(text + "\n")