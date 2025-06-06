from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterUserForm 


def home(request):
    return render(request,'home.html')



def login_user(request):
    if request.method == "POST":
        print(request.POST)
        print('REQUEEEEEEEEEEEEEEEEST!!!!!!!!!!!!')
        email = request.POST['email']
        print(f'email ----> {email}')
        password = request.POST['password']
        print(f'password ----->> {password}')
        User = get_user_model()
        #form = AuthenticationForm(data=request.POST)
        #print(f'form---->> {form}')
        try:
                user_obj = User.objects.get(email=email)
                print(user_obj.username)
                user = authenticate(request,username = user_obj.username, password = password)  
                print(user)
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    print('User is None')
                    messages.error(request,'Ha habido un error con el inicio de sesion')
        except User.DoesNotExist:
                messages.error(request,"The user doesnt exist")
        
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,'Se ha desconectado del sistema')
    return redirect('login')


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            print('El formulario es valido')
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request,'Ha sido registrado correctamente')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('login')
        else:
            print('El formulario no es valido',form.errors)
            messages.error(request,'Error en el formulario')
    else:
        form = RegisterUserForm()
    return render(request,'register.html',{'form':form})