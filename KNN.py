import sys
import json
import pandas as pd

# Create a function which returns the 3 colors from a string 'rgb'
def get_rgb_values(color):
    color = color.replace('rgb(', '').replace(')', '')
    r, g, b = color.split(',')
    return [int(r), int(g), int(b)]    

def k_nearest_neighbors(colors, target_colors):
    target_color_df = pd.Series({'red': target_colors[0], 'green': target_colors[1], 'blue': target_colors[2]})

# Manipulate the data

    diff = colors[['red', 'green', 'blue']] - target_color_df
    diff_sq = diff**2
    diff_sum = diff_sq.sum(axis = 1)
    dist = diff_sum**(1/2)
    dist_sorted = dist.sort_values()

    # In this case I am pulling the closest neighbor 
    k_closest = colors.loc[dist_sorted.index][:1]['color_name']

    k_closest_red = colors.loc[dist_sorted.index][:1]['red']
    k_closest_green = colors.loc[dist_sorted.index][:1]['green']
    k_closest_blue = colors.loc[dist_sorted.index][:1]['blue'] 
    # I want it to return only the string name and not the Series
    probable_color = k_closest.iloc[0]
    red = k_closest_red.iloc[0]
    green = k_closest_green.iloc[0]
    blue = k_closest_blue.iloc[0]

    return ({
        'color_name': probable_color,
        'red': int(red),
        'green': int(green),
        'blue': int(blue)
    })      

data = sys.argv[1]
rgb = json.loads(data)['dataIn']
color = rgb['rgb']

colors = pd.read_csv("https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv", names=['color', 'color_name', 'hex', 'red', 'green', 'blue'], index_col='color')

#print("FROM THE PYTHON FILE", color)

target_colors = get_rgb_values(color) # returns a list of 3 colors

# Since we are labeling colors with its nearest neighbor, we would be using Classification
# This project will also revolve around the K-nearest-Neighbors model.
# Distance formula = sqrt((x2 - x1)^2 + (y2 - y1)^2). I would do the same but with a z vairable.

# Turn these colors into an array with 3 columns:
# We need to use a Series so we can subtract 1 value from the entire dataframe

output = k_nearest_neighbors(colors, target_colors)
sys.stdout.write(json.dumps(output))
