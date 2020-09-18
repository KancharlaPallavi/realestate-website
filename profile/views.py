from .models import Images
from .forms import UploadFileForm
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            x=Images(image=request.FILES['image'])
            x.save()
            messages.success(request, f'Uploaded successfully')
            return HttpResponseRedirect('upload')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

    
def showImage(request):
    img = Images.objects.get(id=1)
    return render(request, 'image_preview.html', {"file":img})
    