from django.shortcuts import render


from .models import Record

# Create your views here.
def home_view(request):
    return render (request, "home.html", {})

def record_view(request):
    obj = Record.objects.get(id=1)
    context = {
        'object': obj
    }
    return render (request, "records/recordView.html", context)