from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post

app_name = "home"

def home(request):
    posts = Post.objects.all()
    content = {'posts':posts}
    return render(request, "home/home.html", content)

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        desc = request.POST['desc']
     
        if len(name) < 3 or len(email) < 6 or len(city) < 3 or len(state) < 4 or len(desc) < 3:
            messages.warning(request, "Please fill the details correctly.") 
        else:
            contact = Contact(name = name, email = email, city = city, state = state, desc = desc)
            contact.save()
            messages.success(request, "Your form has been successfully submited.")


        return redirect("/contact")

    return render(request, "home/contact.html")



def usersignup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if  User.objects.filter(username = username).exists():
            messages.warning(request, "This username already exists, Please choose another username")
            return redirect("/")

        if not username.isalnum():
            messages.warning(request, "Username should be alphanumeric.")
            return redirect("/")
        
        if not username.islower():
            messages.warning(request, "Username should be in lowercase.")
            return redirect("/")
        
        if len(username) > 10:
            messages.warning(request, "Username should be less than 10 characters.")
            return redirect("/")
        
        if password1 != password2:
            messages.warning(request, "Password did not match.")
            return redirect("/")        
        
        user = User.objects.create_user(username, email, password1)      
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect("/")
    
    else:
        return HttpResponse("404 : Error")


def userlogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(request, username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully Logged In.")
            return redirect("/")
        else:
            messages.warning(request, "Bad Credentials, Please try again.")
            return redirect("/")

    else:
        return HttpResponse("404 : Error")

def userlogout(request):
    logout(request)
    messages.success(request, "You are successfully Logged Out.")
    return redirect("/")


def search(request):
    if request.method == "GET":
        word = request.GET['search']

        if word == "":
            messages.warning(request, "Please write something in the search box.")
            allpost = []

        if len(word) > 20:
            messages.warning(request, "Please seach in less the 20 characters.")
            allpost = []
        
        else:
            posttitle = Post.objects.filter(title__contains = word)
            postauthor = Post.objects.filter(author__contains = word)
            postcontent = Post.objects.filter(content__contains = word)
            postdatetime = Post.objects.filter(datetime__contains = word)
            allpost = posttitle.union(postauthor)
            allpost = allpost.union(postcontent)
            allpost = allpost.union(postdatetime)

        content = {'posts': allpost, "word": word}
        return render(request, "home/search.html", content)
    
    
    
    else:
        return HttpResponse("404 : Error")







