# creating a scatter plot from the exercise handout
x = [14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5]
y = [220, 330, 190, 340, 410, 445, 415]
import matplotlib.pyplot as plt
import numpy as np
# temperature data
x = np.array([14.2, 16.5, 11.8, 15.3, 18.8, 22.5, 19.5])
# number of soup sales
y = np.array([220, 330, 190, 340, 410, 445, 415])
# regression line
m,b = np.polyfit(x,y,1) # m == slope, b = intercept
# placing x and y labels
plt.plot(x, m*x + b)
plt.xlabel("Temperature")
plt.ylabel("Price in (R)")
# scatter plot title
plt.title("Soup sales in relation to temperature")
plt.scatter(x,y)
plt.show()