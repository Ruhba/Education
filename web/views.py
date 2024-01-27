from django.shortcuts import render
from . models import Facilities,School,Teachers,Clients,Contact
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    context = {
        'facilities': Facilities.objects.all(),
        'school' : School.objects.all(),
        'teachers' : Teachers.objects.all(),
        'clients' : Clients.objects.all()
        }
    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)


        gname = request.POST.get("G_name")
        gemail = request.POST.get("G_email")
        cname = request.POST.get("C_name")
        cage = request.POST.get("C_age")
        message = request.POST.get("message")

        contact2=Contact(
            user=user,
            g_name =gname,
            g_email =gemail,
            c_name = cname,
            c_age = cage,
            message = message,
        )
        contact2.save()
    
    return render(request,'web/index.html',context)

def about(request):
    return render(request,'web/about.html')
def appointment(request):
    return render(request,'web/appointment.html')
def call(request):
    return render(request,'web/call-to-action.html')
def classes(request):
    return render(request,'web/classes.html')
def contact(request):
    return render(request,'web/contact.html')
def facility(request):
    return render(request,'web/facility.html')
def team(request):
    return render(request,'web/team.html')
def testimonial(request):
    return render(request,'web/testimonial.html')
def error(request):
    return render(request,'web/404.html')