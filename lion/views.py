from django.shortcuts import render

# Create your views here.
def pagina_inicial(request):
    context = {
    'nome': 'Obede', 
    'cachorros':
    ['mel','tobias','bob', 'costela', 'layla']}
    return render(request, 'index.html', context)