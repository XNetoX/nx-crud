from wsgiref import validate
from django.shortcuts import render, redirect
from dados.forms import DadosForm
from dados.models import Dados
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse

# Create your views here.


def home(request):
    data = {}
    data['db'] = Dados.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = DadosForm()
    return render(request, 'form.html', data)


def view(request, pk):
    data = {}
    data['db'] = Dados.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Dados.objects.get(pk=pk)
    data['form'] = DadosForm(instance=data['db'])
    return render(request, 'form.html', data)

# ---------------------- funções de manipulação do banco


@csrf_protect
@csrf_exempt
def create(request):
    form = DadosForm(request.POST or None)
    # import pdb; pdb.set_trace()
    # print(form)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'form.html', {'form': form})


@csrf_protect
@csrf_exempt
def update(request, pk):
    data = {}
    data['db'] = Dados.objects.get(pk=pk)
    form = DadosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

    else:
        return render(request, '500.html')


def delete(request, pk):
    db = Dados.objects.get(pk=pk)
    db.delete()
    return redirect('home')
