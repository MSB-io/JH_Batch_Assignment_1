search_term = input("Enter word to search: ")
with open("example.txt", "r") as file:
    for line in file:
        if search_term in line:
            print(line.strip())