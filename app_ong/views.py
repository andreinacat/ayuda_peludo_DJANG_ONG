from django.shortcuts import render

# Create your views here.
def index(request):
    tipos = ["gatos","perros"]
    cachupin = mascota("cachupin",5,"verde")
    contexto = {'usuario':'Marcelo lara','animalitos': tipos,'mascota': cachupin}
    return render(request, 'index.html', contexto)

    
    
def perritos(request):
    return render(request, 'perritos.html')
def gatitos(request):
    return render(request, 'gatitos.html')

class mascota:
    def __init__(self,nombre,edad,color):
        self.nombre=nombre
        self.edad=edad
        self.color=color
        super().__init__()
