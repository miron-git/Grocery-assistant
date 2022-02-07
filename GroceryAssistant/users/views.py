from django.views.generic import CreateView
#  функция reverse_lazy позволяет получить URL по параметру "name" функции path()
from django.urls import reverse_lazy
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm #из какого класса взять форму
    success_url = reverse_lazy("index") #  где login — это параметр "name" в path() куда переадресовать пользователя после успешной отправки формы
    template_name = "registration/reg.html" # имя шаблона, куда будет передана переменная form с объектом HTML-формы.



