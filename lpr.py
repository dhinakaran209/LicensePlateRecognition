!pip install opencv-python
!pip install pytesseract
!pip install twilio
!apt-get install tesseract-ocr

import cv2
import numpy as np
import pytesseract
import re
from google.colab.patches import cv2_imshow

frameWidth = 640    #Frame Width
franeHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier("CLASSIFIER PATH")
minArea = 500

cap =cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,franeHeight)
cap.set(10,150)
count = 0

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import pytesseract

# Load the image
image_path = "IMAGE PATH HERE"  # Replace with the actual image path
img = cv2.imread(image_path)

# Load the pre-trained Haar Cascade for license plate detection
plate_cascade = cv2.CascadeClassifier("CLASSIFER PATH HERE")

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply image pre-processing to enhance text visibility
img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
img_gray = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Detect license plates in the image
number_plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

# Initialize pytesseract with the correct path
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Iterate through detected plates and extract and print the number
for (x, y, w, h) in number_plates:
    plate_img = img[y:y + h, x:x + w]  # Crop the plate region
    number = pytesseract.image_to_string(plate_img, config='--psm 7 tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    print("Detected Number Plate:", number)

# Draw rectangles around detected plates
for (x, y, w, h) in number_plates:
    result2 = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the image with detected plates
cv2_imshow(result2)

# Sample dictionary of car owner information
def remove(string):
    return np.char.replace(string, ' ', '')

# Recognized license plate number
recognized_plate_number = remove(number)
recognized_plate_number = str(recognized_plate_number)
recognized_plate_number = recognized_plate_number.replace(",", "").replace(".", "").replace("-", "").replace("!","")
print(recognized_plate_number)
  # Replace with the recognized plate number from your code

# Create a dictionary of car owner information

import requests

url = "API URL"

querystring = {"authorization":"API KEY","message":"SAMPLE MESSAGE","language":"english","route":"dlt","numbers":"9789288163"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

import re
car_owner_info = {
    "HR26BR9044": {"owner_name": "Hariprasath", "mobile_number": "8888888888"},
    "H982FKL": {"owner_name": "Dhinakaran", "mobile_number": "77777777777"},
    "HR26DK8337": {"owner_name": "Gokul Prasath", "mobile_number": "9999999999"}
}

recognized_plate_number= re.sub(r'[^a-zA-Z0-9]', '', recognized_plate_number)

if recognized_plate_number in list(car_owner_info.keys()):
    owner_info = car_owner_info[recognized_plate_number]
    owner_name = owner_info["owner_name"]
    mobile_number = owner_info["mobile_number"]
    # Simulate sending an SMS
    print(f"Sending SMS to {mobile_number}: Hello {owner_name}, your car has been detected.")
else:

if recognized_plate_number in list(car_owner_info.keys()):
    owner_info = car_owner_info[recognized_plate_number]
    owner_name = owner_info["owner_name"]
    mobile_number = owner_info["mobile_number"]
    try:
      send_sms(name=owner_name,number=mobile_number)
      print("message send successfully")
    except:
      print("failed to send sms")
else:
    print("License plate not found in the dictionary")
