from PIL import Image
import pytesseract

file_path = "./OJF5.png"

img = Image.open(file_path)

print(pytesseract.image_to_string(img))