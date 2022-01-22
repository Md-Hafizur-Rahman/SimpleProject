from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy

from tuition.models import Post,Subject
from .forms import ContactForm,PostForm
from django.views import View
from django.views.generic import FormView

# Create your views here.

class ContactFormView(FormView):
    template_name = 'home.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    def form_Ivalid(self, form):
        return super().form_Ivalid(form)
    def get_success_url(self):
        return reverse_lazy('homeview')

""" class ContactFormView(View):
    template_name = 'home.html'
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        form=self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():  
            form.save()
            return HttpResponse('sucess')
        return render(request,self.template_name,{'form':form})   
         """
def home(req):
    if req.method=='POST':
        form=ContactForm(req.POST)
        if form.is_valid():  
            form.save()
    else:
        form =ContactForm()
    return render(req,'home.html',{'form':form})

def Postview(req):
    post=Post.objects.all()
    return render(req,'tuition/postview.html',{'post':post})
def Subview(req):
    sub=Subject.objects.get(name='bangla')
    post=sub.subject_set.all()
    return render(req,'tuition/subview.html',{'sub':sub,'post':post})
def postcreate(req):
    if req.method=="POST":
        form=PostForm(req.POST,req.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=req.user
            obj.save()
            sub=form.cleaned_data['subject']
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in=form.cleaned_data['class_in']
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("succesfull")
                
    else:
        form=PostForm()
    return render(req,'tuition/postcreate.html',{'form':form})
        
    