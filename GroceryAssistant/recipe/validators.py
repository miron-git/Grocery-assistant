from django.core.exceptions import ValidationError

def validate_time(time):
    if time > 1440:
        raise ValidationError(
            message=('Время приготовления больше суток'
            )
        )
    else:
        return time

def validate_file_size(image):
    filesize = image.size
    if filesize > 100000:
        raise ValidationError(
            message=(
                'Максимальный размер изображения не должен превышать  1000 Кбайт'
            )
        )
    else:
        return image