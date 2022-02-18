from api.models import Purchase 

def purchase_counter(request):
    purchase_counter = Purchase.objects.filter(user=request.user).count()
    return {'purchase_counter': purchase_counter} 