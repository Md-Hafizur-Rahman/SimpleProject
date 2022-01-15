from os import name
from django.shortcuts import render 
from tuition.models import Contact

def home(req):
    if req.method=='POST':
        name=req.POST['name']
        phone=req.POST['phone']
        content=req.POST['content']
        obj=Contact(name=name,phone=phone,content=content)
        obj.save()
    return render(req,'home.html')
    