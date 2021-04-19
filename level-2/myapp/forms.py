from django import forms
from myapp import models


# form without model *****
#class student_form(forms.Form):
 #   name = forms.CharField()
  #  email = forms.EmailField()
#*******

class studentform(forms.ModelForm):
    class Meta:
        model = models.student
        fields = '__all__'
