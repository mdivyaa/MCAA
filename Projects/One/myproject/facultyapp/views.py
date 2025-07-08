from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import FacultyModel
from .forms import FacultyForm

class FacultyListView(ListView):
    model = FacultyModel
    template_name = 'faculty_list.html'

class FacultyDetailView(DetailView):
    model = FacultyModel
    template_name = 'faculty_detail.html'

class FacultyCreateView(CreateView):
    model = FacultyModel
    form_class = FacultyForm
    template_name = 'faculty_form.html'
    success_url = reverse_lazy('faculty_list')

class FacultyUpdateView(UpdateView):
    model = FacultyModel
    form_class = FacultyForm
    template_name = 'faculty_form.html'
    success_url = reverse_lazy('faculty_list')

class FacultyDeleteView(DeleteView):
    model = FacultyModel
    template_name = 'faculty_confirm_delete.html'
    success_url = reverse_lazy('faculty_list')

# Create your views here.
