example_list = []
example_list.append("Hello")
example_list.append(1)
example_list.append(True)

print(f"Contents of lise {example_list}")
print(f"Size of list {len(example_list)}")
print(example_list[0])
print(example_list[1])
print(example_list[2])

example_list.clear()
print(f"New size of list {len(example_list)}")

example_list = [4,2,21,19,45,5]
example_list.sort()
print(f"Sorted list {example_list}")
example_list.reverse()
print(f"Reversed list {example_list}")
example_list.pop()
print(f"Removed last element {example_list}")
example_list.insert(1,10)
example_list.insert(3,10)
example_list.insert(5,10)
print(f"Insert 3 elements of 10 {example_list}")
print(f"There are {example_list.count(10)} 10s in the list")
print(f"Removing 10 from position {example_list.index(10)}")
example_list.remove(10)
print(example_list)
print(f"Removing 10 from position {example_list.index(10)}")
example_list.remove(10)
print(example_list)
print(f"Removing 10 from position {example_list.index(10)}")
example_list.remove(10)
print(example_list)
