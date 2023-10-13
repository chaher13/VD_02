from django import forms
from .models import SiteTemplate, SiteSection

class SiteTemplateForm(forms.ModelForm):

    class Meta:
        model = SiteTemplate
        fields = ['name', 'description']

class SiteSectionForm(forms.ModelForm):

    class Meta:
        model = SiteSection
        fields = ['section_name', 'section_content']
