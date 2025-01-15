with open("example.txt", "r") as file:
    words = file.read().split()
    print("Word count:", len(words))