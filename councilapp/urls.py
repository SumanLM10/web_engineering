
from django.contrib import admin
from django.urls import path
from .views import HomeView,ContactView,SignUpView,LogInView,TaxView,RoadView,BirthView,BenefitsView,BusinessView,CulturalView,HealthView,HousingView,SchoolView,TrafficView,WasteView,WaterView,AboutView
app_name = 'councilapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('tax/', TaxView.as_view(), name='tax'),
    path('road/', RoadView.as_view(), name='road'),
    path('birth/', BirthView.as_view(), name='birth'),
    path('benefits/', BenefitsView.as_view(), name='benefits'),
    path('business/', BusinessView.as_view(), name='business'),
    path('cultural/', CulturalView.as_view(), name='cultural'),
    path('health/', HealthView.as_view(), name='health'),
    path('housing/', HousingView.as_view(), name='housing'),
    path('school/', SchoolView.as_view(), name='school'),
    path('traffic/', TrafficView.as_view(), name='traffic'),
    path('waste/', WasteView.as_view(), name='waste'),
    path('water/', WaterView.as_view(), name='water'),
    path('about/', AboutView.as_view(), name='about'),
    path('create/', ContactView.as_view(), name='create'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', LogInView.as_view(), name='login'),

]
