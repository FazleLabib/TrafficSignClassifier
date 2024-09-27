from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import classify_image

def classify(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            result, confidence = classify_image(image)
            return render(request, 'home.html', {'form': form, 'result': result, 'confidence': confidence})
    else:
        form = ImageUploadForm()
        
    return render(request, 'home.html', {'form': form})