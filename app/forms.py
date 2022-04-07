from django.forms import ModelForm
from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')


class BlogForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'body']

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control border border-primary'}),
        #     'category': forms.Select(choices=choices, attrs={'class': 'form-select border border-primary'}),
        #     'body': forms.Textarea(attrs={'class': 'form-control border border-primary'})
        # }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control border border-info'})
        }
