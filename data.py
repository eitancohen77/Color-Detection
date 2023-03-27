import pandas as pd
import random
from flask import Flask, request, jsonify, render_template


# Flask is a library which allows you to run a server from python. For this to work, we need to put our html files inside a 
# folder called templates. This folder will have all our rendering files. We then need a folder called static. This folder 
# hosts all the css, javascripts, or any pictures that we need will interact with the html files.
app = Flask(__name__)

# Create a function which returns the 3 colors from a string 'rgb'
def get_rgb_values(color):
    color = color.replace('rgb(', '').replace(')', '')
    r, g, b = color.split(',')
    return [int(r), int(g), int(b)]

colors = pd.read_csv("https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv", names=['color', 'color_name', 'hex', 'red', 'green', 'blue'], index_col='color')
#print(colors['red'])

# This would be the main route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_rgb', methods=['POST'])
def handle_rgb():
    data = request.get_json()
    rgb = data.get('rgb')

    color = rgb
    target_colors = get_rgb_values(color) # returns a list of 3 colors

    # Since we are labeling colors with its nearest neighbor, we would be using Classification
    # This project will also revolve around the K-nearest-Neighbors model.
    # Distance formula = sqrt((x2 - x1)^2 + (y2 - y1)^2). I would do the same but with a z vairable.

    # Turn these colors into an array with 3 columns:
    # We need to use a Series so we can subtract 1 value from the entire dataframe
    target_color_df = pd.Series({'red': target_colors[0], 'green': target_colors[1], 'blue': target_colors[2]})

    diff = colors[['red', 'green', 'blue']] - target_color_df
    diff_sq = diff**2
    diff_sum = diff_sq.sum(axis = 1)
    dist = diff_sum**(1/2)
    dist_sorted = dist.sort_values()

    print(dist_sorted)

    # In this case I am pulling the closest neighbor 
    k_closest = colors.loc[dist_sorted.index][:1]['color_name']
    # I want it to return only the string name and not the Series
    probable_color = k_closest.iloc[0]

    print(probable_color)
    return jsonify({'color': probable_color})

if __name__ == '__main__':
    app.run()