#! /usr/bin/env python

import io
import os
import RPi.GPIO as GPIO
import datetime
from datetime import date
import time
import picamera
import operator
import base64
from Garbage_labels_paralle import get_labels
from Display import LCD_REG, LCD_COLOURS
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from builtins import len
from picamera import PiCamera
from time import sleep
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account
from google.auth import credentials

label_num = 0
index = 2
ROW = 1
Total_Weight_Scanned = 0
LOOP = 0

GSPREAD = []
object_detected_Labels = []
object_detected_Web = []

Label = {}
WebLabel = {}

##GPIO.setmode(GPIO.BOARD)
##GPIO.setup(11,GPIO.OUT)
##servo1 = GPIO.PWM(11,50)

timestamp = datetime.datetime.today()
timestamp_long = timestamp.strftime('%s')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/Google_API/ADI BALA-3d3e968445c4.json"
 
credentials = service_account.Credentials.from_service_account_file('/home/pi/Google_API/ADI BALA-3d3e968445c4.json')


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Google_API/client_secret.json', scope)
Client = gspread.authorize(creds)
sheet = Client.open("ADI BALA").sheet1

# SEND FEEDBACK
# AI & Machine Learning Products 
# Cloud Vision API 
# Documentation 
# Guides
# Detect Labels

# Note: Cloud Vision now supports offline asynchronous batch image annotation for all features. This asynchronous request supports up to 2000 image files and returns response JSON files that are stored in your Google Cloud Storage bucket. For more information about this feature, refer to Offline batch image annotation.
# Instantiates a client
client = vision.ImageAnnotatorClient(credentials=credentials)

today = date.today()
camera = PiCamera()

LCD_REG()

while True:
    Current_date = date.today()

    camera.start_preview()
    camera.rotation = 90
    sleep(0.5)
    camera.capture('/home/pi/Pictures/Scanned_image.jpg')
    camera.stop_preview()
     
    # The name of the image file to annotate
    file_name = os.path.abspath('/home/pi/Pictures/Scanned_image.jpg')
    
    #FileName_base64 = base64.encodestring(open(file_image,"rb").read())
     
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
        

##    servo1.start(0)
##    servo1.ChangeDutyCycle(5)
##    time.sleep(0.5)
##    servo1.ChangeDutyCycle(0)


    print(response)


    # Goes through the first set of data and descriptions
    
    ##print('labels')
    lobject_detected, lbincolor, lobject_confidence = get_labels(labels)
    wobject_detected = None
    wbincolor =None
    wobject_confidence =0
 
    if (lobject_confidence < 0.65):
        # If nothing was found in the first set of data, move on to the web entities dataset           
        #if bincolor is None :
        #Goes through web detections,
        try:
            response = client.web_detection(image=image)
            #then webEntities' descriptions
            webEntities = Response.web_annotations
            webEntities = response.web_detection.web_entities
            #print(webEntities)
            #Then goes through the BLUEBIN, GREENBIN, BLACKBIN
            #print('webEntities')
            wobject_detected, wbincolor, wobject_confidence = get_labels(webEntities)
        except Exception as e:
            print(e.message)
        
        #print('Label results:  ' + str(lobject_confidence))
        #print('Web results:  ' + str(wobject_confidence))

    if (lobject_confidence > wobject_confidence):
            object_detected = lobject_detected
            bincolor = lbincolor
            object_confidence = lobject_confidence

    elif (lobject_confidence < wobject_confidence) :
            object_detected = wobject_detected
            bincolor = wbincolor
            object_confidence = wobject_confidence
    else:
        object_detected = 'Unknown'
        bincolor = 'Unknown'
        object_confidence = 0


    GSPREAD.append(str(object_detected))
    GSPREAD.append(bincolor)
    GSPREAD.append(str(object_confidence))
    GSPREAD.append(str(timestamp))
    GSPREAD.append(str(timestamp_long))

    ##if bincolor == 'Black':
    ##        servo1.start(0)
    ##        servo1.ChangeDutyCycle(1)
    ##        time.sleep(0.5)
    ##        servo1.ChangeDutyCycle(0)
    ##        time.sleep(1.5)
    ##        servo1.ChangeDutyCycle(5)
    ##        time.sleep(0.5)
    ##        servo1.ChangeDutyCycle(0)
    ##        GPIO.cleanup()
    ##
    ##
    ##if bincolor == 'Blue':
    ##        servo1.start(0)
    ##        servo1.ChangeDutyCycle(10)
    ##        time.sleep(0.5)
    ##        servo1.ChangeDutyCycle(0)
    ##        time.sleep(1.5)
    ##        servo1.ChangeDutyCycle(5)
    ##        time.sleep(0.5)
    ##        servo1.ChangeDutyCycle(0)
    ##        GPIO.cleanup()        

    ROW = len(sheet.get_all_values())
    values_list = sheet.row_values(ROW)

    LCD_COLOURS(bincolor)
          
    print ('final bin colour: ' + bincolor)
    print ('final object scanned: ' + object_detected)

    ##os.remove('/home/pi/Pictures/Scanned_image.jpg')

    if (str(today) != str(Current_date)):
        sheet = Client.create(str(today))
        sh.share('catb.23@gmail.com', perm_type= 'user', role='owner')
        sheet = Client.open(str(today)).sheet1
        today = date.today

    LOOP = LOOP + 1
    
    sheet.append_row(GSPREAD)
