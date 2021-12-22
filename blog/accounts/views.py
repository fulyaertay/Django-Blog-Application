from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.views.generic import FormView
from .forms import LoginForm,RegisterForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout

class register_view(FormView):
    
  
    template_name="blogs/register.html"
    form_class=RegisterForm
    
    def form_valid(self,form):
        user=form.save(commit=False)
        password=form.cleaned_data.get("password1")
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username,password=password)
        login(self.request, new_user)
        return HttpResponseRedirect(reverse_lazy('blog_list'))
class login_view(FormView):
    
  
    template_name="blogs/login.html"
    form_class=LoginForm
    
    

    def form_valid(self,form):
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('blog_list'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('blog_list'))


       
