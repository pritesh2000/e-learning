from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from LearningApp.models import Contact, Category, Video
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    if not request.user.is_anonymous:
        return redirect("/")
    return render(request, 'home.html')

def index(request):
    if request.user.is_anonymous:
        return redirect("/home")
    data = Category.objects.all()
    cats = {"category_data" : data}
    return render(request, 'index.html', cats)

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "Invalid Username or Password")
            return redirect("/home")
    return redirect("/home")

def logoutuser(request):
    logout(request)
    return redirect("/home")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)
            user.last_name = lname
            user.first_name = fname
            user.save()
            messages.success(request, 'Your data are registered successfully')
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "Please Enter same password in both field.")
            return redirect('/home')
    return redirect('/home')

def contact(request):
    if request.user.is_anonymous:
        return redirect("/home")
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        email = request.POST.get('email')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your Responce is Saved')
    return render(request, 'contact.html')

def myaccount(request):
    if request.user.is_anonymous:
        return redirect("/home")
    return render(request, 'myaccount.html') 

def catinfo(request, myid):
    if request.user.is_anonymous:
        return redirect("/home")
    cat = Category.objects.filter(c_id=myid)
    allvid =Paginator(Video.objects.filter(v_cat=cat[0].cat), 10)
    page = request.GET.get('page')
    try:
        vid = allvid.page(page) 
    except PageNotAnInteger:
        vid = allvid.page(1)
    except EmptyPage:
        vid = allvid.page(allvid.num_pages)
    return render(request, 'catinfo.html', {"cat" : cat[0], "vi" : vid})

def about(request):
    if request.user.is_anonymous:
        return redirect("/home")
    return render(request, 'about.html')

def vplay(request, myid):
    if request.user.is_anonymous:
        return redirect("/home")
    vid = Video.objects.filter(v_id=myid)
    cat = Category.objects.filter(cat=vid[0].v_cat)
    return render(request, 'vplay.html', {"vi" : vid[0], "cat" : cat[0]})

def search(request):
    if request.user.is_anonymous:
        return redirect("/home")
    if request.method == "GET":
        query = request.GET.get('search')
    if len(query) >= 100:
        messages.warning(request, 'Please Enter Valid Search Query')
        return render(request, 'search.html', {"query": query})
    vid = Video.objects.filter(v_title__icontains=query)
    videsc = Video.objects.filter(v_desc__icontains=query)
    cat = Category.objects.filter(c_title__icontains=query)
    catdesc = Category.objects.filter(c_desc__icontains=query)
    allVid = vid.union(videsc)
    allCat = cat.union(catdesc)
    if allVid.count() == 0 and allCat.count()==0:
        messages.warning(request, 'Please Enter Valid Search Query')
    return render(request, 'search.html', {"vi": allVid, "cat": allCat, "query":query})
