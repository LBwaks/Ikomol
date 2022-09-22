from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Blog,Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm,SearchForm
from django.contrib.postgres.search import SearchVector
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


class BlogsView(ListView):
    model = Blog
    paginate_by = 10
    template_name = 'blogs/blog.html'
    def get_context_data(self, **kwargs):
        context = super(BlogsView, self).get_context_data(**kwargs)
        blogs = Blog.published.all()
        context['blogs']=blogs
        return context
class BlogDetailView(DetailView):
    model = Blog 
    template_name = 'blogs/blog-details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # getting detail
        blog = get_object_or_404(Blog, slug=self.kwargs['slug'])
        context["blog"] = blog 
        # end of getting detail

        # comments
        blog_to_comment = get_object_or_404(Blog,slug=self.kwargs['slug'])
        form =CommentForm()
        comments =Comment.objects.filter(blog=blog_to_comment).order_by('-created_date')
        context['blog_to_comment'] = blog_to_comment
        context['comments']=comments
        return context
    def post(self,request,slug,**kwargs):
        blog = get_object_or_404(Blog,slug =slug)
        new_comment = None
        form =CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog =blog  
            new_comment.save()
        comments = Comment.objects.filter(blog=blog).order_by('-created_date')

        context={'blog':blog,'form':form,'comments':comments}
        return render(request,'blogs/blog-details.html',context)
def search(request):
    form =SearchForm()
    results =[]
    if request.method =='GET':
       q = request.GET.get('q')
       results = Blog.published.annotate(search=SearchVector('title','description','tag')).filter(search=q).order_by('created_date')
       page = request.GET.get('page',1)
       paginator =Paginator(results,10)
       try :
        results =paginator.page(page)
       except PageNotAnInteger:
        results=paginator.page(1)
       except EmptyPage:
            results=paginator.page(paginator.num_pages)
    return render( request,'blogs/search.html',{'form':form,'results':results,'q':q})