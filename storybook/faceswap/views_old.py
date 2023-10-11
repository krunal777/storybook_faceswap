from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .forms import HotelForm
from .models import Hotel

import cv2
import easygui
import numpy as np

import glob

# Create your views here.
# def homePage(request):
#     return render(request,"index.html")

def homePage(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('/hotel_images')
    else:
        form = HotelForm()
      
    return render(request, 'index.html', {'form': form})
   
def success(request):
    return HttpResponse('successfully uploaded')


def display_hotel_images(request):
    
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all()

        # img = [cv2.imread(file) for file in glob.glob("media/images/*.png")]

        # print(img.dtype)
        # face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        # gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
        # print(gray)

        # # detects faces in the input image
        # faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        # print('Number of detected faces:', len(faces))

        # if len(faces) > 0:
        #     for i, (x, y, w, h) in enumerate(faces):
            
        #         # To draw a rectangle in a face
        #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        #         face = img[y:y + h, x:x + w]
        #         cv2.imshow("Cropped Face", face)
        #         cv2.imwrite(f'face{i}.jpg', face)
        #         print(f"face{i}.jpg is saved")
        
        # # display the image with detected faces
        # cv2.imshow("image", img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # # read the input image
        # for img_face in Hotels:
        #     print(img_face)
            

        return render(request, 'display_hotel_images.html',{'hotel_images': Hotels})
        