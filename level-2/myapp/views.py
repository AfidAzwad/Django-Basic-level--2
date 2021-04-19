from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import student
from myapp import forms
# Create your views here.

def home(request):
   #return HttpResponse("Love Rice");
   studentlists = student.objects.order_by('name')
   diction = {'student': studentlists}
   return render(request, 'myapp/index.html', context = diction)

def form(request):
   student_form = forms.studentform()
   if request.method == "POST":
      student_form = forms.studentform(request.POST)

      if student_form.is_valid():
         student_form.save(commit=True)
         return home(request)
   diction = {'studentform': student_form}
   return render(request, 'myapp/form.html', context = diction)

# def azwad(request):
  #   return HttpResponse("Azwad is okay");***