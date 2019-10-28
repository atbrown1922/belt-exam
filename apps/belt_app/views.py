from django.shortcuts import render, redirect
from .models import Job, User
from django.contrib import messages

def home(request):
    return render(request, "login.html")

def dashboard(request):
    context = {
        'all_jobs' : Job.objects.all()
    }
    return render(request, "index.html", context)

def index(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'all_jobs' : Job.objects.all(),
        "user" : user
    }

    return render(request, 'index.html', context)

def add_job(request):
    
    return render (request, "add_job.html")

def create_job(request):
    errors = Job.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/addJob')
    else:
        Job.objects.create(title=request.POST['title'], description=request.POST['description'], location=request.POST['location'])
        return redirect("/dashboard")

def view(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {
        "job" : job
    }
    return render(request, "view_job.html", context)

def edit(request, job_id): 
        job = Job.objects.get(id=job_id)
        context = {
            "job" : job
        }
        return render(request, "edit.html", context )

def update(request, job_id):
    job = Job.objects.get(id=job_id)
    errors = Job.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{job.id}')
    else: 
        job.title = request.POST["title"]
        job.location = request.POST['location']
        job.description = request.POST['description']
        job.save()
        messages.success(request, "Job successfully updated")
        return redirect('/dashboard')

def destroy(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect('/dashboard')

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'] )
        user = User.objects.last()
        return redirect(f'/dashboard/{user.id}')

def login(request):
    user =User.objects.get(email=request.POST["email"])
    context = {
        "user" : user
    }
    return redirect(f'/dashboard/{user.id}')
def logout(request):
    return redirect('/')





# Create your views here.
