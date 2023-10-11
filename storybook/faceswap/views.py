from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .forms import HotelForm
from .models import Hotel

import numpy
import os
import glob
import cv2
import matplotlib.pyplot as plt
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image



import glob

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


def display_hotel_images(request,plot_after=True):    
    if request.method == 'GET':
        # getting all the objects of hotel.
        Hotels = Hotel.objects.all().order_by('-id')[:1]

        swapper = insightface.model_zoo.get_model('./media/images/inswapper_128.onnx',download=False, download_zip=False)
        app = FaceAnalysis(name='buffalo_l')
        app.prepare(ctx_id=0, det_size=(640, 640))
        
        
        img2 = cv2.imread("./media/"+str(Hotels[0].face_Main_Img))
        img1 = cv2.imread("./media/"+str(Hotels[0].cartoon_Main_Img)) 
        # img1 = cv2.imread('./media/images/vijay.jpg') 
        # print(img2)
        # print(img1)
        
        # print(img1)
        # print(img2) 
        # Do the swap
        face1 = app.get(img1)[0]
        face2 = app.get(img2)[0]
      
        img1_ = img1.copy()
        img2_ = img2.copy()


        # face aligment start        
        # face aligment end


        if plot_after:
            img1 = swapper.get(img1, face1, face2, paste_back=True)
            img2_ = swapper.get(img2_, face2, face1, paste_back=True)
            fig, axs = plt.subplots(1, 2, figsize=(10, 5))
            axs[0].imshow(img1_[:,:,::-1])
            axs[0].axis('off')
            axs[1].imshow(img2_[:,:,::-1])
            axs[1].axis('off')
            cv2.imwrite("./media/images/change.jpg", img1)

        return render(request, 'display_hotel_images.html',{'swap_img': img2_})
        # return HttpResponse("test")
        

def swap_n_show(request,plot_before=True,plot_after=True):
    swapper = insightface.model_zoo.get_model('./media/images/inswapper_128.onnx',download=False, download_zip=False)
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))

    img1 = cv2.imread('./media/images/vijay.jpg')
    img2 = cv2.imread('./media/images/krunal.jpg') 

    if plot_before:
        fig, axs = plt.subplots(1,2, figsize=(10,5))
        axs[0].imshow(img1[:,:,::-1])
        axs[0].axis('off')
        axs[1].imshow(img2[:,:,::-1])
        axs[1].axis('off')
        # plt.show()

    # do the swap
    face1 = app.get(img1)[0]
    face2 = app.get(img2)[0]

    
    img1_ = img1.copy()
    img2_ = img2.copy()

    if plot_after:
        img1 = swapper.get(img1, face1, face2, paste_back=True)
        img2_ = swapper.get(img2_, face2, face1, paste_back=True)

        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        axs[0].imshow(img1_[:,:,::-1])
        axs[0].axis('off')
        axs[1].imshow(img2_[:,:,::-1])
        axs[1].axis('off')
        cv2.imwrite("./media/images/change.jpg", img2_)
        # plt.show()
    return render(request, 'display_hotel_images.html',{'swap_img': img1_})
    


