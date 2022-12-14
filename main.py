import math
from PIL import Image, ImageDraw

img = Image.new('RGBA', (960, 960), (255, 255, 255))
draw = ImageDraw.Draw(img)

angle_rad = math.radians(30)

with open("DS2.txt", "r") as file:
    for line in file:
        coordinates = line.split()
        i = int(coordinates[0]) - 480
        j = int(coordinates[1]) - 480
        x = math.cos(angle_rad) * i - math.sin(angle_rad) * j
        y = math.sin(angle_rad) * i + math.cos(angle_rad) * j
        draw.line((x + 480, y + 480, x + 481, y + 481), fill=(0, 0, 255))

img.show()
img.save('transformed_image.png')
