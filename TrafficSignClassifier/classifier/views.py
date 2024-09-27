from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import classify_image
from django.templatetags.static import static


def classify(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            label, confidence, class_val = classify_image(image)
            meta_url = static('media/meta/' + str(class_val) + '.png') 
            confidence_percentage = float(confidence) * 100
            confidence_str = f"{confidence_percentage}%"
            return render(request, 'home.html', {'form': form, 'label': label, 'confidence': confidence_str, 'meta_url': meta_url})
    else:
        form = ImageUploadForm()
        
    return render(request, 'home.html', {'form': form})