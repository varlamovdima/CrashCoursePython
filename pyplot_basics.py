import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2,100)
print(x)
# Create figure
fig = plt.figure()
plt.plot(x,x,label="Linear")
plt.plot(x,x**2,label="Quadratic")
plt.plot(x,x**3,label="Cubic")

# Add title to the plot
plt.title("Simple Plot")
# Show the legend of the plot
plt.legend()
# Print out the final plot
plt.show()

