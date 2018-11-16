from visualizing_color_math import *

# Add two colors: green and red
visualize_color_math('sum', colors['green'], colors['red'], actual = False)

# Add all 3 primary colors: Red, Green, Blue
visualize_color_math('sum', colors['green'], colors['red'], colors['blue'])

# subtract pink from orange
visualize_color_math('subtract', colors['orange'], colors['pink'], actual = False)

# Take mean of all 3 primary colors: Red, Green, Blue
visualize_color_math('mean', colors['green'], colors['red'], colors['blue'])
