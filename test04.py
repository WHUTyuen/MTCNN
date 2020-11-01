from PIL import Image
from PIL import ImageDraw
import os

IMG_DIR = r"D:\cebela\img_celeba"
ANO_DIR = r"D:\cebela\Anno"

img = Image.open(os.path.join(IMG_DIR, "000002.jpg"))
imgDraw = ImageDraw.Draw(img)
imgDraw.rectangle((72, 94, 72 + 221, 94 + 306),outline="red")
img.show()
