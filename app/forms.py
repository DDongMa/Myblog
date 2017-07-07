from django import forms
from .models import Category


class ArticleForm(forms.Form):

    title = forms.CharField(widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
