from django.shortcuts import render
from .models import Categoria, Mascota


# Create your views here.
def index(request):
    tipos = ["gatos","perros"]
    cachupin = mascota("cachupin",5,"verde")
    contexto = {'usuario':'Marcelo lara','animalitos': tipos,'mascota': cachupin}
    return render(request, 'index.html', contexto)

    


def filtro_categoria(request):
    masco = Mascota.objects.all()
    categorias = Categoria.objects.all()
    cant = Mascota.objects.all().count()
    if request.POST:
        cate= request.POST.get("cboCategoria")
        masco = Mascota.objects.filter(categoria__pk=cate)
        cant= Mascota.objects.filter(categoria__pk=cate).count()
    contexto ={"mascotas":masco,"categorias": categorias,"cantidad":cant}
    return render(request, 'animalitos_todos.html',contexto)


def filtro_descripcion(request):
    masco = Mascota.objects.all()
    categorias = Categoria.objects.all()
    cant = Mascota.objects.all().count()
    if request.POST:
        texto = request.POST.get("txtDesc")
        masco = Mascota.objects.filter(descripcion__contains=texto)
        cant = Mascota.objects.filter(descripcion__contains=texto).count()
    contexto ={"mascotas":masco,"categorias": categorias,"cantidad":cant}
    return render(request, 'animalitos_todos.html',contexto)

def gatitos(request):
    masco = Mascota.objects.all()
    categorias = Categoria.objects.all()
    cate = 'gatos'
    masco = Mascota.objects.filter(categoria__pk=cate)     
    cant= Mascota.objects.filter(categoria__pk=cate).count()
    contexto ={"mascotas":masco,"categorias": categorias,"cantidad":cant}

    return render(request, 'gatitos.html',contexto)

def perritos(request):
    masco = Mascota.objects.all()
    categorias = Categoria.objects.all()
    cate = 'perros'
    masco = Mascota.objects.filter(categoria__pk=cate)     
    cant= Mascota.objects.filter(categoria__pk=cate).count()
    contexto ={"mascotas":masco,"categorias": categorias,"cantidad":cant}

    return render(request, 'perritos.html',contexto)

def animalitos(request):
    masco = Mascota.objects.all()
    categorias = Categoria.objects.all()
    contexto ={"mascotas":masco,"categorias": categorias}
    return render(request, 'animalitos_todos.html',contexto)


def ficha(request, id):
    mascota= Mascota.objects.get(nombre=id)
    contexto = {"mascota":mascota}
    return render(request,"ficha.html",contexto)

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
        imagen = request.FILES.get("txtImg")
        mas = Mascota(
            nombre=nombre,
            edad=edad,
            descripcion=desc,
            imagen= imagen,
            categoria=obj_cate
        )
        mas.save()
        context = {"categorias":categorias,"mensaje":"grabo"}

    return render(request, "registro.html", context)