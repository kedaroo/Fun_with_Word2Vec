import json
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import math

json_colors = json.loads(open('xkcd.json').read())

def hex_to_rgb(hex):
    hex = hex.strip('#')
    r, g, b = int(hex[:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)
    return r, g, b
# print(hex_to_rgb('#ffffff'))

def rgb_to_hex(color):
    r, g, b = color[0], color[1], color[2]
    hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex
# print(rgb_to_hex(255,255,255))


colors = dict()
for item in json_colors['colors']:
    colors[item['color']] = hex_to_rgb(item['hex'])

def distance(coord1, coord2):
    dist = math.sqrt(sum([(i - j)**2 for i, j in zip(coord1, coord2)]))
    return dist

def closest(space, coord, n = 10):
    '''returns a list of n number of color vectors in proximity of given vectors
       space is a dictionary/ associative array
       coord is given vector
       n is the max number of closest vectors'''
    closest_names = list()
    closest_values = list()
    for key in sorted(space.keys(), key = lambda x: distance(coord, space[x]))[:n]:
        closest_names.append(key)
        closest_values.append(space[key])
    return closest_names, closest_values

def visualize_color_math(operation, *args):

    # perform the operation
    if operation == 'add':
        result = np.add(*args)
    elif operation == 'subtract':
        result = np.subtract(*args)
    else:
        a = [*args]
        result = np.mean(a, axis = 0)

    # find closest names and values of colors closest to the result
    closest_names, closest_values = closest(colors, result, n = 5)

    # make list of hex values of closest colors to pass into scatter plot
    hex_colors = [item['hex'] for item in json_colors['colors'] if item['color'] in closest_names]

    # dissect rgb components of closest color values
    reds = [r[0] for r in closest_values]
    greens = [g[1] for g in closest_values]
    blues = [b[2] for b in closest_values]
    # print(f'Reds: {reds} \nGreens: {greens} \nBlues: {blues}')

    # append rgb components and hex values of input colors to previous lists
    for color in args:
        print(color)
        reds.append(color[0])
        greens.append(color[1])
        blues.append(color[2])
        hex_colors.append(rgb_to_hex(color))

    # print(f'Reds: {reds} \nGreens: {greens} \nBlues: {blues} \nHex colors: {hex_colors}')
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(reds, greens, blues, c = hex_colors, alpha = 1, s = 200)
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    plt.show()
    return

visualize_color_math('mean', colors['orange'], colors['blue'])
# visualize_color_math('add', colors['green'], colors['pink'])
# visualize_color_math('subtract', colors['olive'], colors['purple'])
