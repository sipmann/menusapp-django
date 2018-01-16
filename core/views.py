from django.shortcuts import render

# Create your views here.
def listagem(request):
    return render(request, 'core/listagem.html')