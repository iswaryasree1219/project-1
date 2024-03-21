from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader 
from app.models import JobPost


job_title=[
    "First Job",
    "Second Job",
    "Third Job"
]

job_description=[
    "First job description",
    "Second job description",
    "Third job description"
]

class TempClass:
    x=5

def hello(request):
    # template=loader.get_template("app/hello.html")
    list=["alpha","beta"]
    temp=TempClass()
    is_authenticated=True
    context={"name":"Django","age":30,"first_list":list,"temp_object":temp,"is_authenticated":is_authenticated}
    # return HttpResponse(template.render(context,request))
    return render(request,"app/hello.html",context)

# Create your views here.
def job_list(request):
    jobs=JobPost.objects.all()
    context={"jobs":jobs}
    return render(request,"app/index.html",context)

def job_detail(request,id):
    try:
        if id==0:
            return redirect(reverse('jobs_home'))
        job=JobPost.objects.get(slug=id)
        context={"job":job}
        return render(request,"app/job_detail.html",context)
        
    except:
        return HttpResponseNotFound("Not Found")
