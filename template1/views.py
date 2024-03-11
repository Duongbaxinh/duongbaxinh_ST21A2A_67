from django.shortcuts import render,redirect, get_object_or_404
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Music,Hobby,NhatKy
from django.contrib.auth import authenticate, login, logout
from .models import Post


def blogPage(request):
    Data  = {'Posts':Post.objects.all().order_by('-date')}
    first_post = Data['Posts'][0] 
    print('post::: ',first_post.audio, first_post.image)
    return render(request,'pages/blog.html')

def homePage(request):
    data = request.user
    nhatky = NhatKy.objects.all()
    print('nhat ky check :::: ', nhatky[0].image.url)
    return render(request,'pages/blog.html',{"user":data,"nhatky":nhatky})
def loginPage(request):
    return render(request,'pages/login.html')

def signupPage(request):
    return render(request,'pages/signup.html')

def postDetail(request, pk):
    post = get_object_or_404(NhatKy, pk=pk)
    return render(request, 'pages/nhatky.html', {'post': post})
def musicPage(request):
    Data = Music.objects.all()
    print('Check data music ::: ', Data[0].musicfile)
    return render(request,'pages/playmusic.html',{"musics":Data})
    

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/blog')
    Data  = {'form':form}
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if(pass1 != pass2):
  
            messages.error(request,'confirm password must match password!')
            redirect('/')
        try:
        
            # check user existed
            if User.objects.filter(username=username):
                messages.error(request, "Username already exist! Please try some other username.")
                return redirect('/')
          
            User.objects.create_user(username=username,email=email,password=pass1,first_name=firstname,last_name=lastname,is_active=True,is_staff=True)
            user = User.objects.all()
        
        except: User.DoesNotExist
    else:
        HttpResponseRedirect('/')
    return render(request, "pages/login.html")
def sigin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        print('check user 1 :::: ',username,pass1)
        user = authenticate(request,username=username, password=pass1)
        print('check user :::: ',user)
        if user is not None:
            login(request,user)
            fname = user.first_name
            print('checkfname',)
            hobbies = Hobby.objects.all()
            # messages.success(request, "Logged In Sucessfully!!")
            return redirect('/homepage')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('/')
    return render(request, "pages/login.html")
# Create your views here.
