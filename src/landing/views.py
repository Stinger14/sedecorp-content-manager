from django.shortcuts import render
from items.models import Item
# Create your views here.

def home_page_view(request):
    if not request.user.is_authenticated:
        return render(request, "landing/home.html", {})
    qs = Item.objects.filter(project=request.project)
    return render(request, "dashboard/home.html", {"items": qs})

def about_page_view(request):
    print(request.project)
    return render(request, "landing/home.html", {})

def server_error_page(request):
    raise Exception
    return render(request, "landing/error.html", {})