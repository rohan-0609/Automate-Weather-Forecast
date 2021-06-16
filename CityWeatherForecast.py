
import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

API_key = "1b1946d3bc7177abc8fc1266caf9b5d9"
city_list = ["Delhi", "Hyderabad", "Chicago", "Jaipur", "Atlanta"]
height = [300, 430, 550, 690, 810]

image = Image.open("Weather_post .png")# .png file that we added left side
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('Inter-Medium.ttf', size=50) # intert
content = "Recent weather forecast"
color = 'rgb(255, 255, 255)'
(x,y) = (55,50)
draw.text((x,y), content, color, font=font)

font = ImageFont.truetype('Inter-Medium.ttf', size=30) # intert
today = date.today()
content = date.today().strftime("%A- %B %d, %Y" ) #
color = 'rgb(255, 255, 255)'
(x,y) = (45,145)
draw.text((x,y), content, color, font=font)

index = 0 # counter attack --
for city in city_list:
    URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=1b1946d3bc7177abc8fc1266caf9b5d9&units=metric".format(city)

    response = requests.get(URL)
    Data = json.loads(response.text)

    font = ImageFont.truetype('Inter-Medium.ttf', size=50)  # intert
    color = 'rgb(0, 0, 0)' # (0,0,0) is for black font color for white background
    (x, y) = (135, height[index]) #  430 is for second row 300 is for first row
    draw.text((x, y), city, color, font=font)

    font = ImageFont.truetype('Inter-Medium.ttf', size=50)  # intert
    content = str(Data['main']['temp']) + "\u00b0" # for degree sign
    color = 'rgb(255, 255, 255)'
    (x, y) = (600, height[index])  # 430 is for second row 300 is for first row
    draw.text((x, y), content, color, font=font)

    font = ImageFont.truetype('Inter-Medium.ttf', size=50)  # intert
    content = str(Data['main']['humidity']) + "%" # for percent in humidityu
    color = 'rgb(255, 255, 255)'
    (x, y) = (810, height[index]) # 430 is for second row 300 is for first row
    draw.text((x, y), content, color, font=font)

    index += 1


image.show()# showing image
image.save("Weather_forecast.png")