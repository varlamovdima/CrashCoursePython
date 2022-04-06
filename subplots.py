import matplotlib.pyplot as plt
plt.figure(1,figsize=(9,3))
values = [1,10,100]
labels = ["A","B","C"]
# Make a bar graph
plt.subplot(131) # 1- rows 3- columns 1-first position
plt.bar(labels,values)
# Make a scatter plot
plt.subplot(132)
plt.scatter(labels,values)
# Make a line plot like we've seen before
plt.subplot(133)
plt.plot(labels,values)

plt.suptitle("There different plots on the same figure")
plt.show()

