from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from .models import BlogPost
from django.contrib.auth import authenticate 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
         username =request.POST['username']
         email=request.POST['email']
         fname=request.POST['fname']
         lname=request.POST['lname']
         pass1=request.POST['pass1']
         pass2=request.POST['pass2']        
    
         user = User.objects.create_user(username=username, email=email, password=pass1, first_name=fname, last_name=lname)

         messages.success(request, "Your account has been successfully created.")
         
         return redirect('login')
    else:
        messages.warning(request,"Something went wrong, please check your inputs")
        #return redirect('register')
     
    return render (request, 'register.html')

def login(request):
    posts = BlogPost.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            auth_login(request, user)
            fname=user.first_name
            return render(request,"home.html",{'fname': fname,'posts':posts})
            
        else:
            messages.error(request, "Invalid credentials")
            
    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")
    
         
def home(request):
    posts = BlogPost.objects.all()
    fname = request.user.first_name if request.user.is_authenticated else None
    return render(request, 'home.html', {'posts': posts , 'fname':fname})

@login_required
def createpost(request):
    fname = request.user.first_name if request.user.is_authenticated else None
    if request.method == 'POST':
        # Extract data from the request
        title = request.POST['title']
        content = request.POST['content']

        # Create a new BlogPost instance and save it
        blog_post = BlogPost(title=title, content=content,author=request.user)
        blog_post.save()
        
    
    return render(request, 'createpost.html',{'fname':fname})

@login_required
def post_detail(request, pk):
    fname = request.user.first_name if request.user.is_authenticated else None
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'post_detail.html', {'post': post,'fname':fname})

@login_required
def profile(request):
    fname = request.user.first_name
    lname = request.user.last_name
    username = request.user.username
    doj = request.user.date_joined
    return render(request, 'profile.html',{'fname':fname,'lname':lname,'username':username})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Handle the form submission and update the user's profile information.

        # Handle profile picture upload
        if 'profile_picture' in request.FILES:
            new_profile_picture = request.FILES['profile_picture']
            request.user.profile.profile_picture = new_profile_picture

        # Update other profile fields
        new_bio = request.POST.get('bio')
        new_dob = request.POST.get('date_of_birth')
        new_location = request.POST.get('location')

        request.user.profile.bio = new_bio
        request.user.profile.date_of_birth = new_dob
        request.user.profile.location = new_location
        request.user.profile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect('edit_profile')

    return render(request, 'edit_profile.html')
    
