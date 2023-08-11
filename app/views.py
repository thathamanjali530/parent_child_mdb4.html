from django.shortcuts import render

# Create your views here.

def parent_mdb4(request):
    return render(request,'parent_mdb4.html')

def child(request):
    return render(request,'child.html')
    
