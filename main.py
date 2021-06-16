# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import json
from PIL import Image, ImageFont, ImageDraw

API_key = "1b1946d3bc7177abc8fc1266caf9b5d9"
city = "Chicago"
URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=1b1946d3bc7177abc8fc1266caf9b5d9&units=metric".format(city)

response = requests.get(URL)
Data = json.loads(response.text)
print(Data)

image = Image.open("Weather_post .png")# .png file that we added left side
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('Inter-Medium.ttf', size=50) # intert
content = "Recent weather forecast"
color = 'rgb(255, 255, 255)'
draw.text((55,50), content, color, font=font)

image.save("Weather_forecast.png")