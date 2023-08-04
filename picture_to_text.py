import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

from tkinter.filedialog import *
link = askopenfilename()

print(pytesseract.image_to_string(link))