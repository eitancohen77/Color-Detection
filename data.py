import pandas as pd

colors = pd.read_csv("https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv", names=['color', 'color_name', 'hex', 'red', 'green', 'blue'], index_col='color')
print(colors)