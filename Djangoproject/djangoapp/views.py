from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'djangoapp/index.html', {'title':'Главная страница!!!!!!!', 'task':tasks})

class AppDetailView(DetailView):
    model = Task
    template_name = 'djangoapp/details_view.html'
    context_object_name = 'task'
    fields = ['title', 'task']

class AppUpdateView(UpdateView):
    model = Task
    success_url = '/'
    template_name = 'djangoapp/update.html'
    fields = ['title', 'task']

class AppDeleteView(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'djangoapp/delete.html'
    fields = ['title', 'task']

def about(request):
    return render(request, 'djangoapp/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма не заполнена"

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'djangoapp/create.html', context)