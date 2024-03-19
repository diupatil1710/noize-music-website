# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from .models import Song



def music(request):
    r=render(request,'music.html')
    return HttpResponse(r)

def about(request):
    r=render(request,'about.html')
    return HttpResponse(r)

def search(request):
    title=request.GET.get("search","")
    song=Song.objects.filter(singer=title).values() | Song.objects.filter(name=title).values()   
    return render(request,'search.html',{'song':song})
      

def songs(request):
    song=Song.objects.all()
    return render(request,'songs.html',{'song':song})

def recome(request):
    song=Song.objects.all()
    return render(request,'recome.html',{'song':song})

def songposts(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request,'songpost.html',{'song':song})

def songfront(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request,'songs.html',{'song':song})

def allsong(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request,'allsong.html',{'song':song})

def loginPage(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def login_view(request):
    useremail=request.POST["username"]
    password=request.POST["password"]
    user = authenticate(username=useremail,password=password)
    from django.contrib.auth import login
    login(request,user)
    return redirect('/')

    

def userregistration(request):
    if request.method == 'POST':
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          username = request.POST['username']
          email = request.POST['email']
          mobile_number = request.POST['phone']
          password= request.POST['password']

          my_user = User.objects.create_user(username,email,password)
          my_user.first_name = first_name
          my_user.last_name = last_name
          my_user.mobile_number = mobile_number
          my_user.save()
          user = authenticate(username=username,password=password)
          from django.contrib.auth import login
          login(request,user)
          return redirect('/')
    
    #     x.save()
    #     msg="data inserted"
    #     return render(request,'music.html',{"msg":msg})
        
def contact(request):
    r=render(request,'contact.html')
    return HttpResponse(r)

def contactus(request):
    # msg=''
    # if request.method=="POST":
        # logininfo = request.POST.get("login",)
        # name = request.POST["username"]
        # phone= request.POST["phone"]
        # email= request.POST["email"]
        # subject= request.POST["subject"]
        # message= request.POST["message"]
       
        # x = registration(username=name,phone=phone,email=email,subject=subject,message=message)
        # x.save()
        # form = contactForm(request.POST)
        # if form.is_valid():
            # form.save
            msg="data inserted"
            return render(request,'music.html',{"msg":msg})

# def viewEmployee(request):
#     user=registration.objects.all()
#     return render(request,'viewEmployee.html',{"user":user})

def logout_view(request):
    logout(request)
    return render(request,'signup.html')



