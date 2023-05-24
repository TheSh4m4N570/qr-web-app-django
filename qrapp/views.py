from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import QrForm
from .qrclass import ProductQr
import random
import os

fs = FileSystemStorage(location="media/qr")


def remove_downloaded_files(folder: str = ""):
    """
    This function remove all the generated file in the designated file system storage
    :param folder:
    :return: None
    """
    folder = os.path.join(os.getcwd(), "media/qr")
    files = os.listdir(folder)
    for file in files:
        os.remove(f"{folder}/{file}")


def name_generator():
    """
    This function generate a random numeric namefile for the generated Qr
    :return: str
    """
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ]
    random.shuffle(numbers)
    name_of_image = [number for number in numbers]
    return "".join(name_of_image)


def read_and_return_response(location: str, img_name: str):
    """
    This function take 2 params, reads the filename and return an httpresponse to download the file
    :param location:
    :param img_name:
    :return: Response
    """
    with open(f"{location}/{img_name}.png", "rb") as fprb:
        response = HttpResponse(fprb.read(), content_type="image/png")
        response["Content-Disposition"] = f"attachment; filename={img_name}.png"
    return response


def home(request):
    return render(request, "qr/index.html")


def get_url(request):
    if request.method == "POST":
        form = QrForm(request.POST)
        if form.is_valid():
            qr = ProductQr(form.data.get('url')) #instance of custom QrCode Class
            img = qr.generate_qr_image()
            img_name = name_generator() #getting a custom name for the image
            img.save(f"{fs.location}/{img_name}.png")
            response = read_and_return_response(fs.location, img_name) #downloading the image
            remove_downloaded_files(folder="fs") #removing all the files in the folder after the download for security reasons

            return response

    else:
        form = QrForm()
    return render(request, "qr/index.html", {"form": form})
