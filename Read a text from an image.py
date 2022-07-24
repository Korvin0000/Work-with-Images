import cv2
import pylab as pl
import pytesseract


im = "C:\\Users\\Nikolay\\Desktop\\Stuff\\Smith.png"

img = cv2.imread(im)
text = pytesseract.image_to_string(img)
pl.imshow(img, cmap='gray')
print(text)

