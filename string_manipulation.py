from sys import argv
name, csv_string = argv
s="Test string"
print(s[0:4:1]) # print characters from position 0 up to position 4(not included) and in increments of 1
print(s[5:]) # print the rest of the string starting from position 5
s = s.split(" ")
print(s)
s = " ".join(s)
print(s)
print(csv_string)
csv_string = csv_string.split(",")
print(csv_string)
s=s.upper()
print(s)
s=s.lower()
print(s)

