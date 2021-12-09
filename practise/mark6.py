import pytesseract as tess
from PIL import Image

img = Image.open("practise/0001.jpg")
text = tess.image_to_string(img)

print(text)