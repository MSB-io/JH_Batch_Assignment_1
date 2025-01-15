import re

text = "Contact us at email@example.com or support@domain.org."
emails = re.findall(r'[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}', text)
print(emails)