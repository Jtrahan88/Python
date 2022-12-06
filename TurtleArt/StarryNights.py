import random
from PIL import Image, ImageDraw

# create a new image
width, height = 400, 400
image = Image.new('RGB', (width, height), (255,255,255))
draw = ImageDraw.Draw(image)

# draw the sky
draw.rectangle([(0, 0), (width, height)], fill=(0,0,128))

# draw the stars
for i in range(200):
  x = random.randint(0, width)
  y = random.randint(0, height)
  r = random.randint(1, 3)
  draw.ellipse([(x, y), (x+r, y+r)], fill=(255,255,255))

# draw the moon
x = random.randint(0, width)
y = random.randint(0, height)
r = 50
draw.ellipse([(x, y), (x+r, y+r)], fill=(255,255,0))

# draw the hills
draw.polygon([(0, height), (width/2, height/2), (width, height)], fill=(0,128,0))

# draw the church
draw.rectangle([(150, 200), (250, 300)], fill=(255,0,0))
draw.polygon([(150, 200), (225, 100), (250, 200)], fill=(128,0,0))
draw.rectangle([(165, 230), (235, 260)], fill=(255,255,255))
draw.line([(165, 245), (235, 245)], fill=(0,0,0), width=2)

# save the image
image.save('starry_night.png')
