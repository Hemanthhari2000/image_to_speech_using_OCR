# importing Libraries
import cv2
import pytesseract
from speak import speak

"""

	DOWNLOAD LINK FOR TESSERACT: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-4.00.00dev.exe

"""
# Location of the tesseract.exe file
pytesseract.pytesseract.tesseract_cmd = 'XXXXX\\tesseract.exe' 

# Read images using cv2.
img = cv2.imread('./imgs/1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get the text from pytesseract
text = pytesseract.image_to_string(img)

# show the original image
cv2.imshow('Image', img)

# print the detected text
print(text)

# let the bot speak the text for you
speak(text)

cv2.waitKey(0)