from django import forms
from .models import Evaluation

class EvaluationForm(forms.ModelForm):

    email_subject = forms.CharField(max_length=200)
    email_text = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Evaluation
        fields = "__all__"
