from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.exceptions import ValidationError


def compress_image(image):
    try:
        img = Image.open(image).convert('RGB')
    except Exception:
        raise ValidationError("Not image provided")
    output = BytesIO()
    img.save(output, format='JPEG', quality=70)
    output.seek(0)

    return InMemoryUploadedFile(
        output, 'ImageField', f"{image.name.split('.')[0]}.jpg", 'image/jpeg', output.getbuffer().nbytes, None
    )
