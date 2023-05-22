from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import QrForm
from .qrclass import ProductQr
import random

fs = FileSystemStorage(location="media/qr")

def name_generator():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
    random.shuffle(numbers)
    name_of_image = []
    for l in numbers:
        name_of_image.append(l)
    return "".join(name_of_image)

def read_and_return_response(location, img_name):
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
            qr = ProductQr(form.data.get('url'))
            img = qr.generate_qr_image()
            img_name = name_generator()
            img.save(f"{fs.location}/{img_name}.png")
            response = read_and_return_response(fs.location, img_name)
            return response

    else:
        form = QrForm()
    return render(request, "qr/index.html", {"form":form})
