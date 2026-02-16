import re
#Write a regex to check if a string contains only digits.

print(re.findall(r"^\d+$","24516553"))

#Write a pattern to match a 10-digit mobile number.

print(re.findall(r"^\d{10}$","2451651153"))

#Find all lowercase letters in a string.

print(re.findall(r"[a-z]","24516adgb511ax53"))

#Extract all uppercase letters from a sentence.

print(re.findall(r"[A-Z]","2451651AJDFHJJKD1aefjdn53"))

#Match a string that starts with "Hello".

print(re.findall(r"^Hello","Hello kdv kndjmz knf"))

#Match a string that ends with "world".

print(re.findall(r"world$","skvkdjv lkld world"))

#Find all words separated by spaces.

print(re.findall(r"\b\w+\b","245 1651 153"))

#Match exactly 5 characters.

print(re.findall(r"^.{5}$","21153"))

#Find all occurrences of the word "python" (case-sensitive).

print(re.findall(r"python","2451651153 python sdvPythondmcskm csldlpython"))

#Replace all spaces in a string with underscores.
print(re.sub(r"\s+","_","24 516 553"))
