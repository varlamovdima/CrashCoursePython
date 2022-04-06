a = 3
b = 5
if(a==3):
    print("a==3")
elif(b==5):
    print("b==5")
else:
    print("All other cases!")

i = 0
while(i!=10):
    i+=1
    if i==3:
        print(f"Only prints on third iteration ({i})")
        # Continue immediately starts the next iterations
        continue
    print(f"Prints on every other iteration ({i})")

    if i==7:
        # Immediately leave the loop
        break

print(f"Exited the loop on iteration {i}")
