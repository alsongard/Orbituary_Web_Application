from django.shortcuts import render
from django import forms

from .models import Record
from .form import RecordForm
# Create your views here.
def home_view(request):
    return render (request, "home.html", {})

def record_view(request):
    obj = Record.objects.get(id=1)
    context = {
        'object': obj
    }
    return render (request, "records/recordView.html", context)

def records_create_view(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RecordForm()
    context = {
        'form': form
    }

    return render(request, 'records/recordData.html', context)