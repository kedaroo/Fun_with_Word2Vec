# importing dependencies
import json
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# loading dataset
json_colors = json.loads(open('xkcd.json').read())

def hex_to_rgb(hex):
    '''converts hex color values to rgb format'''
    hex = hex.strip('#')
    r, g, b = int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)
    return r, g, b

# initializing lists of rgb components of colors
reds = []
greens = []
blues = []

for item in json_colors['colors']:
    r, g, b = hex_to_rgb(item['hex'])
    reds.append(r), greens.append(g), blues.append(b)

# initializing list of hex values of colors
hex_colors = []
for item in json_colors['colors']:
    hex_colors.append(item['hex'])

# plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(reds, greens, blues, c = hex_colors, s = 200, alpha = 1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
plt.show()
