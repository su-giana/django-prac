from django.http import HttpResponse

def main(request):
    return HttpResponse("Hi, welcome to my burger house")

def burger_list(request):
    return HttpResponse("This is a list of our buger's prices")