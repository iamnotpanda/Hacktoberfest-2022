from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
font = ImageFont.truetype('ProductSansRegular.ttf',100)
for index,j in df.iterrows():
    img = Image.open('certificate.jpeg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(130,675),text='{}'.format(j['name']),fill=(0,0,0),font=font)
    img.save('pictures/{}.jpg'.format(j['name']))