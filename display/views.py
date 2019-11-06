from django.shortcuts import render
from .form import SampleForm
from .models import SampleModel


def index(request):
    form = SampleForm(request.POST)
    context = {'form': form}
    return render(request, 'index.html', context)


def submitted(request):
    form = SampleForm(request.POST)
    # print(form)
    form.save()
    entries = SampleModel.objects.all()
    context = {'entries': entries}
    return render(request, 'list.html', context)
