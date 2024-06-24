from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document,Post
import cv2
import os
from django.conf import settings


# Create your views here.
def frontpage(request):
    return render(request, "food/frontpage.html")

def foodpage(request):
    posts = Post.objects.all()
    return render(request, "food/foodpage.html", {"posts": posts})

def capturepage(request):
    # Flag = Document.objects.get_or_none(id=1)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/capture/')

    # elif Flag != None:
    else:
        form = DocumentForm()
        max_id = Document.objects.latest('id').id
        obj = Document.objects.get(id = max_id)
        input_path = str(settings.BASE_DIR) + obj.photo.url
        output_path = str(settings.BASE_DIR) + "/media/output/output.jpg"
        detect(input_path,output_path)

    return render(request, 'food/capture.html', {
        'form': form,
        'obj':obj,
    })



def detect(input_path,output_path):
    if os.path.isfile(input_path) == True:
        img = cv2.imread(input_path)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(output_path, img_gray)