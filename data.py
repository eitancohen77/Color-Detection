import pandas as pd

import random

colors = pd.read_csv("https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv", names=['color', 'color_name', 'hex', 'red', 'green', 'blue'], index_col='color')
#print(colors['red'])

# Since we are labeling colors with its nearest neighbor, we would be using Classification
# This project will also revolve around the K-nearest-Neighbors model.

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return f'rgb({str(red)}, {str(green)}, {str(blue)})'

print(random_color())

# Distance formula = sqrt((x2 - x1)^2 + (y2 - y1)^2). I would do the same but with a z vairable.

rand_color = random_color()

# Create a function which returns the 3 colors from a string 'rgb'
target_colors = get_rgb_values(rand_color) # returns a list of 3 colors

# Turn these colors into an array with 3 columns:
target_color_df = pd.DataFrame([target_colors], names=['red', 'green', 'blue'])

diff = colors - target_color_df
diff_sq = diff**2
diff_sum = diff_sq.sum(axis = 1)
dist = diff_sum**(1/2)
dist_sorted = dist.sort_values()

# In this case I am pulling the closest neighbor 
k_closest = colors.loc[dist_sorted.index][:1]['color_name']
probable_color = k_closest