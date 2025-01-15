with open("example.txt", "r") as file:
    words = file.read().split()
    print("Longest word:", max(words, key=len))