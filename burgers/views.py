from django.shortcuts import render
from burgers.models import Burger

# Create your views here.
def burger_list(request):
    burgers = Burger.objects.all()
    return render(request, "list.html")