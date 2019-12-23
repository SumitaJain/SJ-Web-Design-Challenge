import pandas as pd

# Read data file and create dataframe
path = "resources/cities.csv"
df = pd.read_csv(path, encoding="utf-8")

# Render dataframe as html
html = df.to_html()

#write html to file
text_file = open("sj_data_table.html", "w")
text_file.write(html)
text_file.close()