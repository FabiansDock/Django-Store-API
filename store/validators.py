from django.core.exceptions import ValidationError


def validate_max_image_size(file):
    max_image_size = 50

    if file.size > max_image_size * 1024:
        raise ValidationError(f'Image size cannot exceed {max_image_size}KB !')
