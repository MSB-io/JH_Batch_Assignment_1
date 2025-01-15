text = input("Enter text to write to file: ")
with open("example.txt", "w") as file:
    file.write(text)