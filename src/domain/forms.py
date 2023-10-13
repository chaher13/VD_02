from django import forms
from .models import DomainName, SEOSettings

class DomainNameForm(forms.ModelForm):

    class Meta:
        model = DomainName
        fields = ['domain_name', 'status', 'expiration_date']

class SEOSettingsForm(forms.ModelForm):

    class Meta:
        model = SEOSettings
        fields = ['site_title', 'site_description']
