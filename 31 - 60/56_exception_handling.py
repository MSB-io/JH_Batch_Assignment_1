def safe_convert(s):
    try:
        return int(s)
    except ValueError:
        print("Error: Invalid input")

safe_convert("abc")