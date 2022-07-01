from django.core.exceptions import ValidationError

def validate_time(time):
    # Валидатор времени приготовления(time в мин.)
    if time > 1440:
        raise ValidationError(
            message=('Время приготовления больше суток'
            )
        )
    else:
        return time

def validate_file_size(image):
    # Валидатор размера 
    filesize = image.size
    if filesize > 1000000:
        raise ValidationError(
            message=(
                'Максимальный размер изображения не должен превышать  1000 Кбайт'
            )
        )
    else:
        return image