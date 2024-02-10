from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFilter
import numpy as np
import webcolors as wb



#dict de dict??


COLORS_DEFINED = {
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Red": (255, 0, 0),
    "Lime": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    # "Gray": (128, 128, 128),
    "Green": (0, 128, 0),
    "Purple": (128, 0, 128),
    "Navy": (0, 0, 128),
    "Orange": (255, 165, 0),
    "Pink": (255, 105, 180),
    "Brown": (255, 105, 180),
    "Light Salmon": (255,160,122),
    "Coral": (255,127,80),
}

def closest_color(color):
    min_colors = {}
    for name in COLORS_DEFINED:
        rPixel, gPixel, bPixel = COLORS_DEFINED[name]
        rDiff = (rPixel - color[0]) ** 2
        gDiff = (gPixel - color[1]) ** 2
        bDiff = (bPixel - color[2]) ** 2
        min_colors[(rDiff + gDiff + bDiff)] = name
    return min_colors[min(min_colors.keys())]


colors = dict()
total_colors = 0

image = Image.open("noi.jpeg")
imageReconstructed = image

for i in range(image.size[0]):
    for j in range(image.size[1]):
        closest_color_name = closest_color(image.getpixel((i,j)))
        if closest_color_name in colors:
            colors[closest_color_name] += 1
        else:
            colors[closest_color_name] = 1
        imageReconstructed.putpixel((i, j), COLORS_DEFINED[closest_color_name])

# print(colors)
for key in colors:
    print(f"Culoare: {key}, Procentaj: {colors[key] / (image.size[0] * image.size[1]) * 100:.2f}%")


img = np.asarray(imageReconstructed)
imgplot = plt.imshow(img)
plt.show()


