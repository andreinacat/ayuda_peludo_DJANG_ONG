from django.shortcuts import render
from .models import Categoria, Mascota

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

def registro(request):
    categorias = Categoria.objects.all() # select * from categoria
    context = {"categorias":categorias}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        edad = request.POST.get("txtEdad")
        desc = request.POST.get("txtDesc")
        cate = request.POST.get("cboCategoria")
        obj_cate = Categoria.objects.get(nombre=cate)
        mas = Mascota(
            nombre=nombre,
            edad=edad,
            descripcion=desc,
            categoria=obj_cate
        )
        mas.save()
        context = {"categorias":categorias,"mensaje":"grabo"}

    return render(request, "registro.html", context)