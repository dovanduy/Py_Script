# -*- coding: utf-8 -*-
import pytesseract
from PIL import Image

# pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(Image.open('a.jpg'), lang='chi_sim')

print text