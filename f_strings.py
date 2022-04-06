# F-string
normal_string = "Hello there!"
f_string = f"Look how I can automatically say, {normal_string}"
print(normal_string)
print(f_string)

empty_f_string = "Is this a valid f-string? {}"
print(empty_f_string.format(True))

first_half = "We can combine the first half of the string"
second_half = " with a second half!"

print(first_half+second_half)

divider = "-"
dividing_line = "{}"

print(dividing_line.format(divider*10))

