from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from posts.models import Blog
# Create your views here.
def Home(request):
    try:
        blogs = Blog.objects.all()[0:5]
    except Blog.DoesNotExist:
        blogs = None
    user = None
    user_id = request.COOKIES.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None
    return render(request,'Home.html',{'user':user,'blogs':blogs})
def OnePost(request,post_slug):
    blog = get_object_or_404(Blog, slug=post_slug)
    user = None
    user_id = request.COOKIES.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None
    return render(request,'onePost.html',{'blog':blog,'user':user})
def all_Post(request):
    try:
        blog = Blog.objects.all()
    except Blog.DoesNotExist:
        blog = None
    return render(request,'allPosts.html',{'blogs':blog})
    
def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('SignUp')
        first = request.POST.get('first')
        last = request.POST.get('last')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name=first,last_name=last,username=username, email=email, password=password)
        user.save()
        response = HttpResponseRedirect('/')  # or your desired page after signup
        response.set_cookie('user_id', user.id, max_age=3600 * 24 * 7)  # 7 days
        return response  
    return render(request,'SignUp.html')
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login successful: set user_id cookie
            response = HttpResponseRedirect('/')  # or your desired page
            response.set_cookie('user_id', user.id, max_age=3600 * 24 * 7)  # 7 days
            messages.success(request, 'Login successful!')
            return response
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('Login')
    return render(request,'Login.html')
def Logout(request):
    response = HttpResponseRedirect('/')  # Redirect to login or home page
    response.delete_cookie('user_id')  # Remove the cookie
    messages.success(request, 'You have been logged out.')
    return response
def AboutMe(request):
    return render(request,'aboutMe.html')
def Contacts(request):
    return render(request,'contacts.html')
def PrivacyPolicy(request):
    return render(request,'privacyPolicy.html')