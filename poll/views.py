from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from poll.models import Person
from django.views.decorators.csrf import csrf_exempt

# def home(request):
#     t=loader.get_template("home.html")
#     context={
#         'name':'John',
#         'age':21
#     }
#     return HttpResponse(t.render(context,request))

def home(request):
    return render(request,'home.html',{
        'name':'John',
        'age':21
        })




def persons(request):
    t=loader.get_template("persons.html")
    p=Person.objects.all()
    context={
        'p':p
    }
    return HttpResponse(t.render(context,request))



def persondetails(request,id):
    t=loader.get_template("persondetails.html")
    p=Person.objects.get(id=id)
    context={
        'p':p
    }
    return HttpResponse(t.render(context,request))


def addpersonpage(request):
    t=loader.get_template("addperson.html")
   
    return HttpResponse(t.render())

@csrf_exempt
def addpersonpageprocess(request):
    t=loader.get_template("addsuccess.html")
    if request.method=='POST':
        name=request.POST['name']
        eid=request.POST['eid']
        dob=request.POST['dob']
        address=request.POST['address']
        email=request.POST['email']
        mobno=request.POST['mobno']
        # print(name,eid,dob,address,email,mobno)
        p=Person(name=name,eid=eid,dob=dob,address=address,email=email,mobno=mobno)
        p.save()






   
    return HttpResponse(t.render())


def delete(request,id):
    t=loader.get_template("deletesuccess.html")
    p=Person.objects.get(id=id)
    p.delete()
  
    return HttpResponse(t.render())



def updatepage(request,id):
    t=loader.get_template("updatepage.html")
    p=Person.objects.get(id=id)
    context={
        'p':p
    }
   
    return HttpResponse(t.render(context,request))



@csrf_exempt
def updatepageprocess(request,id):
    t=loader.get_template("updatesuccess.html")
    if request.method=='POST':
        name=request.POST['name']
        eid=request.POST['eid']
        dob=request.POST['dob']
        address=request.POST['address']
        email=request.POST['email']
        mobno=request.POST['mobno']
        # print(name,eid,dob,address,email,mobno)
        p=Person.objects.get(id=id)

        p.name=name
        p.eid=eid
        p.dob=dob
        p.address=address
        p.email=email
        p.mobno=mobno


        p.save()






   
    return HttpResponse(t.render())






def test(request):
    t=loader.get_template("test.html")
   
    return HttpResponse(t.render())

