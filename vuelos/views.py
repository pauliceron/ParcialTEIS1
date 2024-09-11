from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError
from .models import Flight

# Create your views here.
def home(request):
    return render(request,'home.html')

def crear(request):
    return render(request, 'crear.html')



class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name','type','price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError('Price must be greater than zero.')
        return price
    
class FlightCreateView(View):
    template_name = 'crear.html'
    def get(self, request):
        form = FlightForm()
        viewData = {}
        viewData["title"] = "CrearFlight"
        viewData["form"] = form
        return render(request, self.template_name, viewData)
    def post(self, request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('crear') 
        else:
            viewData = {}
            viewData["title"] = "CrearFlight"
            viewData["form"] = form
            return render(request, self.template_name, viewData)