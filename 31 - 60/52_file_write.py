text = input("Enter text: ")
with open("output.txt", "w") as file:
    file.write(text)