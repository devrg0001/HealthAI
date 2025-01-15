import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PhotoUploadForm
from PIL import Image
from .Pneumonia_Model_script import runPneumonia
from .Lung_Cancer_script import runLungCancer

def testing(request):
    result_message = None  # Initialize result message

    if request.method == 'POST' and request.FILES.get('image'):
        form = PhotoUploadForm(request.POST, request.FILES)
        network_type = request.POST.get('network')


        if form.is_valid():
            # Get the uploaded image from the request
            image_file = request.FILES['image']

            # Open the image using PIL (Python Imaging Library)
            image = Image.open(image_file)

            result = None
            #pneumonia model:
            if network_type == "pneumonia":
                result = runPneumonia(image)
                result_message = f"Image analyzed. Result: {result}% of pneumonia"
            #lung cancer model:
            elif network_type == "lungCancer":
                print("lung cancer")
                result = runLungCancer(image)
                result_message = f"Image analyzed. Result: {result}"

            # Create a response message with the result

    else:
        form = PhotoUploadForm()

    return render(request, 'upload_photo.html', {
        'form': form, 
        'result_message': result_message,
        'MEDIA_URL': settings.MEDIA_URL
        })