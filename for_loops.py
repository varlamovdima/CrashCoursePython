grocery_list = ["apple","banana","chicken","salt","chocolate"]
print(f"Range of 5 = {range(5)}")
print(f"Length of out original list is {len(grocery_list)}")
for i in range(len(grocery_list)):
    print(f"Index {i}, Item {grocery_list[i]}")

for item in grocery_list:
    print(f"Item {item}")

for i, item in enumerate(grocery_list):
    print(f"Index {i}, Item {item}")

