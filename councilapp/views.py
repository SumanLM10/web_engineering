
from django.views import generic
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from . forms import ContactForm, SignUpForm



class HomeView(View):
    template_name = 'councilapp/home.html'
    def get(self, request):
        return render(request, self.template_name)
    
class TaxView(View):
    template_name = 'councilapp/tax.html'
    def get(self, request):
        return render(request, self.template_name)
    
class RoadView(View):
    template_name = 'councilapp/road.html'
    def get(self, request):
        return render(request, self.template_name)
    
class BirthView(View):
    template_name = 'councilapp/birth.html'
    def get(self, request):
        return render(request, self.template_name)
    
class BenefitsView(View):
    template_name = 'councilapp/benefits.html'
    def get(self, request):
        return render(request, self.template_name)

class BusinessView(View):
    template_name = 'councilapp/business.html'
    def get(self, request):
        return render(request, self.template_name)

class CulturalView(View):
    template_name = 'councilapp/cultural.html'
    def get(self, request):
        return render(request, self.template_name)
    
class HealthView(View):
    template_name = 'councilapp/health.html'
    def get(self, request):
        return render(request, self.template_name)

class HousingView(View):
    template_name = 'councilapp/housing.html'
    def get(self, request):
        return render(request, self.template_name)

class SchoolView(View):
    template_name = 'councilapp/school.html'
    def get(self, request):
        return render(request, self.template_name)
    
class TrafficView(View):
    template_name = 'councilapp/traffic.html'
    def get(self, request):
        return render(request, self.template_name)

class WasteView(View):
    template_name = 'councilapp/waste.html'
    def get(self, request):
        return render(request, self.template_name)

class WaterView(View):
    template_name = 'councilapp/water.html'
    def get(self, request):
        return render(request, self.template_name)
    
class AboutView(View):
    template_name = 'councilapp/about.html'
    def get(self, request):
        return render(request, self.template_name)
    



class ContactView(View):
    template_name = 'councilapp/contact.html'
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('councilapp:home')
        return render(request, self.template_name, context={'form':form})
    


class SignUpView(generic.CreateView):
    template_name = 'councilapp/register.html'
    form_class = SignUpForm
    def get_success_url(self):
        return reverse('councilapp:login')


class LogInView(View):
    template_name = 'councilapp/login.html'
    form_class = AuthenticationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form':form})

    def post(self, request):
        form = self.form_class(request.POST, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('councilapp:home')
        return render(request, self.template_name, context={'form':form})



class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('councilapp:login')

