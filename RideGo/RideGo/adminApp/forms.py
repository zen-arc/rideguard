from django import forms
from .models import Category



class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'image'
        ]
        labels = {
            'name': 'Name',
            'image': 'Image'
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Category', 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
