import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)
soup = bs(page.text, "html.parser")

table = soup.find("table")
temp_list = []

rows = table.find_all("tr")
for tr in rows:
    td = tr.find_all("td")
    row = [i.text.rstrip() for i in td] #gives the value of one cell
    temp_list.append(row)

star_names = []
distance = []
mass = []
radius = []
luminosity = []

for i in range(1, len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    luminosity.append(temp_list[i][7])

df = pd.DataFrame(list(zip(star_names, distance, mass, radius, luminosity)), columns = ["star_names", "distance", "mass", "radius", "luminosity"])
df.to_csv("bright_stars.csv")