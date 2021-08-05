from django.forms import CharField, ImageField 
from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
          'class': 'rounded-3 text-dark mt-3',
          'style': 'background-color: white;' ,
          'placeholder': ' title of the photo'
        })
        self.fields['image'].widget.attrs.update(
          {
            'class': 'mt-3'
          })