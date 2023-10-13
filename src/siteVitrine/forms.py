from django import forms
from .models import Site, Page

class SiteForm(forms.ModelForm):

    class Meta:
        model = Site
        fields = ['site_name', 'description', 'site_status', 'publication_date']

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['page_title', 'page_content', 'page_status', 'publication_date']
