from django.shortcuts import render,get_object_or_404,redirect
from .forms import FormPost,IpeForm,CustomUserForm
from .models import Post,Ipe
from django.contrib.auth.decorators import login_required
from ipware import get_client_ip
from django.contrib.auth import login, authenticate

# Create your views here.

def home(request):
    ip,public_or_private=get_client_ip(request)
    Posti=Post.objects.all()
    data={
        'post':Posti,
        'ip':ip,
    }
    ip=Ipe(ipe=ip)
    ip.save()


    return render(request,'post/home.html', data)

def detalle(request,id):
    post=Post.objects.get(id=id)
    data={
        'post':post
    }
    return render(request,'post/detalle.html',data)

@login_required
def newPost(request):
    data={
        'form':FormPost()
    }

    if request.method == 'POST':
        formulario=FormPost(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Guardado correcto'
        data['form']=formulario
    
    return render(request, 'post/newpost.html',data)

@login_required
def modPost(request,id):
    Posti=Post.objects.get(id=id)
    data={
        'form':FormPost(instance=Posti),
        'p':Post(id)
    }

    if request.method == 'POST':
        formulario=FormPost(data=request.POST,instance=Posti,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Se modifico correctamente'
        data['form']=formulario
    
    return render(request, 'post/modpost.html',data)

def eliminar(request,id):
    posti=Post.objects.get(id=id)
    posti.delete()

    return redirect(to='')
    

def registro_usuario(request):
    data={
        'form':CustomUserForm
    }

    if request.method == 'POST':
        formulario=CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user= authenticate(username=username,password=password)
            login(request,user)
            return redirect(to='')

    return render(request, 'registration/registrar.html',data)



