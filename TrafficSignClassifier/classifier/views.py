from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import classify_image
from PIL import Image, UnidentifiedImageError
from django.templatetags.static import static
from io import BytesIO

def classify(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            try:
                img = Image.open(image)

                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                
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

            except UnidentifiedImageError:
                form.add_error(None, 'The uploaded file is not a valid image.')

            except Exception as e:
                form.add_error(None, f'An error occurred: {str(e)}')

    else:
        form = ImageUploadForm()

    return render(request, 'home.html', {'form': form})