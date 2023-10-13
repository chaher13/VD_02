from django import forms
from .models import ColorPalette, Font

class ColorPaletteForm(forms.ModelForm):

    class Meta:
        model = ColorPalette
        fields = ['name', 'colors']

class FontForm(forms.ModelForm):

    class Meta:
        model = Font
        fields = ['name']
