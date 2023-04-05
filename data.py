import sys
import json
import pandas as pd


def get_rgb_values(color):
    color = color.replace('rgb(', '').replace(')', '')
    r, g, b = color.split(',')
    return [int(r), int(g), int(b)]           

colors_df = pd.read_csv("https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv", names=['color', 'color_name', 'hex', 'red', 'green', 'blue'], index_col='color')


data = sys.argv[1]

parsed_data = json.loads(data)

# Manipulate the data
colors = get_rgb_values(parsed_data)
target_color_df = pd.Series({'red': colors[0], 'green': colors[1], 'blue': colors[2]})

diff = colors_df[['red', 'green', 'blue']] - target_color_df
diff_sq = diff**2
diff_sum = diff_sq.sum(axis = 1)
dist = diff_sum**(1/2)
dist_sorted = dist.sort_values()

k_closest = colors_df.loc[dist_sorted.index][:1]['color_name']
k_closest_red =colors_df.loc[dist_sorted.index][:1]['red']
k_closest_green =colors_df.loc[dist_sorted.index][:1]['green']
k_closest_blue =colors_df.loc[dist_sorted.index][:1]['blue']

probable_name = k_closest.iloc[0]
probable_red = k_closest_red.iloc[0]
probable_green = k_closest_green.iloc[0]
probable_blue = k_closest_blue.iloc[0]

rgb = f'rgb({probable_red}, {probable_green}, {probable_blue})'
output = {
    'color_name': probable_name,
    'rgb': rgb
}

# Convert the manipulated data to JSON format
json_output = json.dumps(output)

# Return the JSON output to stdout
sys.stdout.write(json_output)