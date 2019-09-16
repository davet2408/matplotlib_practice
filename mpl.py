from matplotlib import pyplot as plt

print(plt.style.available)

# ages for devs x axis
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# salaries for y axis
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
# plot the data
# can use hex values for the line color
# can use a formated string input for styles or named params as below
# marker='.' for a marker style
plt.plot(dev_x, dev_y, color="k", linestyle="--", marker=".", label="All Devs")

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
# add second line
plt.plot(dev_x, py_dev_y, color="b", linewidth=3, label="Python")

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
# JS line
plt.plot(dev_x, js_dev_y, color="#adad3b", linewidth=3, label="JavaScript")
# add labels to the graph
plt.xlabel("Dev age")
plt.ylabel("Median salary USD $")
plt.title("Median salary by age")

# can pass in a list [] of arguments coresponding to the order in which the plots were made.
# however if using lable='plot name' then this is not needed
plt.legend()

plt.grid(True)

# padding adjustment
plt.tight_layout()
# display a visual of the data
plt.show()
