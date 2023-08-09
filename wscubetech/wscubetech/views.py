from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={

        'title':'home New',
        'bdata':'welcome to techify',
        'clist':['php','java','Django'],
        'numbers':[10,20,30,40,50,60,70,80],
        'student_details':[
            {'name':'Rishi S.Kolhe','phone':987667876},
            {'name':'Jay G.Kolhe','phone':345675667},
            {'name':'Shubham A. Kolhe','phone':345677654}

        ]
    }
    return render(request,"index.html",data)


def aboutUs(request):
    return HttpResponse("welcome to techify",)


def course(request):
    return HttpResponse("welcome to techify")


def courseDetails(request,courseid):
    return HttpResponse(courseid)



