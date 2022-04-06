def print_none():
    print("No arguments")

def print_one(arg1):
    print(arg1)

def print_two(arg1,arg2):
    print(arg1,arg2)

# Print any number of argument
def print_any(*args):
    print(args)
    arg1,arg2,arg3 = args
    print(arg1,arg2,arg3)

print_none()
print_one("Argument 1")
print_two("Argument 1","Argument 2")
print_any("Argument 1","Argument 2","Argument 3")

