from django.shortcuts import render,Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import request
from django.views.generic.edit import UpdateView
from .models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic.detail import DetailView
from django.views.generic import ListView,FormView,DeleteView
from .forms import CreateForm,CommentForm
from django.urls import reverse_lazy
from django.contrib import messages

from django.utils.decorators import method_decorator
# Creating MyPaginator 
class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


# Creating ListView 
class BlogList(ListView):
    template_name="blogs/blog_list.html"
    paginate_by = 8
    paginator_class = MyPaginator
    model=Blog

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        # Get first blog
        first_blog=Blog.objects.all().order_by('-created_date').first()
        # Getting blogs order by createdDate DESC
        blogs_data = Blog.objects.exclude(id=first_blog.id).order_by('-created_date')

        # Get 3 populer blogs
        populer_blogs = Blog.objects.filter(populer=True).exclude(id=first_blog.id).order_by('-created_date')[:3]
        page = self.request.GET.get('page',1)
        #8 blogs per page
        paginator = self.paginator_class(blogs_data, self.paginate_by)     
        blog_lists=  paginator.page(page)
        context['blogs'] = blog_lists
        context['first_blog']=first_blog
        context['populer_blogs']=populer_blogs
        return context




# Creating search_view 
def search_view(request):
    search_results=Blog.objects.filter(description__contains=request.GET['search'])
    context={"search_results":search_results}
    return render(request,'blogs/search.html',context)



# Creating DetailBlog

class DetailBlog(DetailView,FormView):
    template_name="blogs/blog_detail.html"
    model=Blog
    context_object_name="blog"
    form_class=CommentForm
    success_url="/"
    def form_valid(self,form):
        comment=form.save(commit=False)
        comment.post=super().get_object()
        comment.save()
        return super().form_valid(form)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["author_blogs"] =Blog.objects.filter(blog_author=self.object.blog_author).exclude(description=self.object.description)[:2]
        context['form'] = self.get_form()
        context["comments"]=self.object.comments.all()
        return context



@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateForm(FormView):
    
    template_name="blogs/create.html"
    form_class=CreateForm
    
    success_url=reverse_lazy("blog_list")

    
    def form_valid(self,form):
        post=form.save(commit=False)
        post.blog_author=self.request.user
        post.save()     
        return super().form_valid(form)
   
       
    
class UpdateForm(UpdateView):
    model = Blog
    fields=["description","blog_content","blog_author","cover_photo","populer"]
    template_name="blogs/update.html"
    success_url="/"
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
   

class DeleteForm(DeleteView):
    model=Blog
    template_name="blogs/delete.html"
    success_url="/"

   


