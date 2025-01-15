with open("example.txt", "r+") as file:
    content = file.read().replace("old_word", "new_word")
    file.seek(0)
    file.write(content)
    file.truncate()