from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import registerAdmin
from .forms import REGISTERform




def home(request):
    return render(request,"home.html")


# login === name and password
# --------------------------------

def login_view(request):
    message=None
    if request.POST:
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(name=name,password=password)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
                messages.info(request,"invalid credentials")
                return redirect('signup')
    else:
        return render(request, 'login.html')


# login === email and password
# --------------------------------------------------------

# def login_view(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user_obj = User.objects.get(email=email)
#             user = authenticate(request, username=user_obj.username, password=password)
#         except User.DoesNotExist:
#             user = None

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid email or password'})
    
#     return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect ('/')
   
    return render(request,"logout.html")




def signup(request):  

    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['confirm_password']


        if password==password2:

            if registerAdmin.objects.filter(name=name).exists():
                messages.info(request, "Username already taken")
                return redirect('signup')
            
            elif registerAdmin.objects.filter(email=email).exists():
                    messages.info(request, "Email already registered")
                    return redirect('signup')
        
            else:
                user=User.objects.create_user(name=name,email=email,password=password)
                user.save();
                return redirect('login')
            
        else:
             messages.info(request, "password not matching")
             return redirect('signup')

    else:
        
    
        return render(request,'signup.html')



def member(request):
     user=registerAdmin.objects.all()   
     return render(request,"adminn.html",{'user':user})


def add(request):
   
    return render(request,"add.html",)


def addrec(request):
    if request.method == "POST":
        form = REGISTERform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member")
        else:
            return render(request, "add.html", {'form': form})


def delete(request,id):
    user=registerAdmin.objects.get(id=id)
    user.delete()
    return redirect ("member")



def update(request, id):
    user = registerAdmin.objects.get(id=id)
    if request.method == "POST":
        form = REGISTERform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('member')
    else:
        form = REGISTERform(instance=user)
    return render(request, 'update.html', {'form': form, 'user': user})


