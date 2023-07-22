from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse
from django.template import loader

# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound
from app.models import JobPost





def job_list (request):

    jobs=JobPost.objects.all()
    context={
        "jobs":jobs,

    }
 
    return render(request,'app/index.html',context)

def job_detail(request,id):

    try:
        if id==0:
            return redirect('Jobs_home')

        job=JobPost.objects.get(id=id)
        context={"job":job}
        return render(request,'app/job_detail.html',context)

    except:

        return HttpResponseNotFound("Not Found")


class TempClass:
    x=5

def hello(request):
    # template=loader.get_template('app/hello.html')
    lis_t=["alpha","beta"]
    temp_obj=TempClass()
    is_authenticated=False
    context={"name":"Django","first_list":lis_t,"temp_object":temp_obj,"age":18,"is_authenticated":is_authenticated}
    # return HttpResponse(template.render(context,request))

    return render(request,'app/hello.html',context)