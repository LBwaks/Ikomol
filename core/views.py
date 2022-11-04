from django.http import HttpResponse
from .models import Package, Service
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import ListView,CreateView,TemplateView
from django.contrib.messages.views import SuccessMessageMixin
# from core.tasks import testfunction
# from 

# Create your views here.
class HomeView(ListView):
    model = Package
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        pricings = Package.objects.all().order_by('-created_date')
        services = Service.objects.all()
        context['pricings'] = pricings
        context['services'] = services
        return context
# def HomeView(request):
#     return render(request,'core/home.html')

class PricingsView(ListView):
    model =  Package
    template_name = 'core/pricing.html'
    def get_context_data(self, **kwargs):
        context = super(PricingsView, self).get_context_data(**kwargs)
        pricings = Package.objects.all()
        context['pricings'] =pricings
        return context
class ServicesView(ListView):
    model  = Service
    template_name = 'core/services.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Service.objects.all()
        context["services"] = services
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactView(SuccessMessageMixin,CreateView):
    template_name ='core/contact.html'
    form_class = ContactForm
    success_message ='Your Message has been sent .Thank You'

    def form_valid(self,form):
        form.send()
        return super().form_valid(form)
        
def error_500(request):
    return render(request,'errors/500.html')
    
def error_404(request, exception):
    return render(request,'errors/404.html', status=404)
def check():
    pass

# def test(request):
#     testfunction.delay()
#     return HttpResponse('done')