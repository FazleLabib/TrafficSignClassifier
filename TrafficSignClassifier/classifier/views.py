from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import classify_image
from PIL import Image
from django.templatetags.static import static


def classify(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            img = Image.open(image)

            if img.mode == 'RGBA':
                img = img.convert('RGB')

            
            from io import BytesIO
            img_io = BytesIO()
            img.save(img_io, format='PNG')
            img_io.seek(0)

            label, confidence, class_val = classify_image(img_io)
            
            meta_url = static('media/meta/' + str(class_val) + '.png') 
            confidence_percentage = float(confidence) * 100
            confidence_str = f"{int(confidence_percentage)}%" if confidence_percentage.is_integer() else f"{confidence_percentage:.1f}%"

            return render(request, 'home.html', {
                'form': form, 
                'label': label, 
                'confidence': confidence_str, 
                'meta_url': meta_url
            })
    else:
        form = ImageUploadForm()

    return render(request, 'home.html', {'form': form})