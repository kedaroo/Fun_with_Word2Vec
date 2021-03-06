import json
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import math

#load xkcd colors data
json_colors = json.loads(open('xkcd.json').read())

def hex_to_rgb(hex):
    '''converts hexadecimal color value to its rgb counterpart'''
    hex = hex.strip('#')
    r, g, b = int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)
    return r, g, b

def rgb_to_hex(color):
    '''converts rgb color to its hexadecimal counterpart
       takes in a tuple or a list'''
    r, g, b = color[0], color[1], color[2]
    hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return hex

# make colors dictionary
colors = dict()
for item in json_colors['colors']:
    colors[item['color']] = hex_to_rgb(item['hex'])

def distance(coord1, coord2):
    '''calculates Euclidean distance between two vectors'''
    dist = math.sqrt(sum([(i - j)**2 for i, j in zip(coord1, coord2)]))
    return dist

def closest(space, coord, n = 10):
    '''returns a list of n number of color vectors in proximity of given vectors
       space is a dictionary/ associative array
       coord is given vector
       n is the max number of closest vectors'''
    closest_values = list()
    for key in sorted(space.keys(), key = lambda x: distance(coord, space[x]))[:n]:
        closest_values.append(space[key])
    return closest_values

def visualize_color_math(operation, *args, rotate = False):

    # perform the operation
    if operation == 'sum':
        a = [*args]
        result = np.sum(a, axis = 0)
    elif operation == 'subtract':
        result = np.subtract(*args)
    else:
        a = [*args]
        result = np.mean(a, axis = 0)

    # remove floating points from the result elements
    revised_result = [int(x) for x in result]
    result = revised_result

    reds = list()
    greens = list()
    blues = list()
    hex_colors = list()

    # append rgb components and hex values of input colors to rgb lists
    for color in args:
        reds.append(color[0])
        greens.append(color[1])
        blues.append(color[2])
        hex_colors.append(rgb_to_hex(color))

    # find closest names and values of colors closest to the result
    closest_values = closest(colors, result, n = 3)

    # dissect rgb components of closest color values
    for color in closest_values:
        reds.append(color[0])
        greens.append(color[1])
        blues.append(color[2])
        hex_colors.append(rgb_to_hex(color))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(reds, greens, blues, c = hex_colors, alpha = 1, s = 1000)
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')

    if rotate:
        for angle in range(0, 360):
            ax.view_init(30, angle)
            plt.draw()
            plt.pause(.001)
    else:
        plt.show()

    return
