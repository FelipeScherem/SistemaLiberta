from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import bebida, comida, usuario
from .forms import bebidaForm, comidaForm

TEMPLATES_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
                )

def pedidos(request):
    bebidas = bebida.objects.all()
    comidas = comida.objects.all()
    return render(request,"pedidos.html",
                    {'bebida': bebidas,
                    'comida': comidas}
                  )

def login(request):
    return render(request, "login.html")

def charts (request):
    return render(request, "graficos.html")

def clientes (request):
    nomes = nome.objects.all()
    nums = num.objects.all()
    gastos = gasto.objects.all()
    return render(request, 'clientes.html',
                  {
                   'nome': nomes,
                   'num': nums,
                   'gasto': gastos}
                  )

def produtos(request):
    if request.method == 'POST':
        bebidaform = bebidaForm(request.POST)
        print('IF 1')
        if bebidaform.is_valid():
            print('SALVOU')
            bebidas = bebidaform.save(commit=True)
            bebidas.save()
            return redirect('produtos')
    else:
        print('ELSE')
        bebidaform = bebidaForm()
        comidaform = comidaForm
        bebidas = bebida.objects.all()
        comidas = comida.objects.all()
        return render(request, 'produtos.html',
                      {'bebidaform': bebidaform,
                       'comidaform': comidaform,
                       'bebida': bebidas,
                       'comida': comidas}
                      )