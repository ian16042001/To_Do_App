from django.shortcuts import render
from app.models import ToDo
from django.http import HttpResponseRedirect


def index(request):
    context = {
        'text': ToDo.objects.all().order_by('-created_at')
    }
    return render(request, 'app/index.html', context)


def add_todo(request):
    search = request.POST.get("text")
    ToDo.objects.create(text=search)
    return HttpResponseRedirect("/")


def remove_todo(request, pk):
    ToDo.objects.get(id=pk).delete()
    return HttpResponseRedirect("/")
