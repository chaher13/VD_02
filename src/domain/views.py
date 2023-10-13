from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Site, DomainName, SEOSettings
from .forms import  DomainNameForm, SEOSettingsForm

@login_required
def create_domain_name(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    if request.method == 'POST':
        form = DomainNameForm(request.POST)
        if form.is_valid():
            domain_name = form.save(commit=False)
            domain_name.site = site
            domain_name.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = DomainNameForm()
    return render(request, 'create_domain_name.html', {'form': form, 'site': site})

@login_required
def update_domain_name(request, domain_id):
    domain_name = get_object_or_404(DomainName, id=domain_id)
    if request.method == 'POST':
        form = DomainNameForm(request.POST, instance=domain_name)
        if form.is_valid():
            form.save()
            return redirect('site_detail', site_id=domain_name.site.id)
    else:
        form = DomainNameForm(instance=domain_name)
    return render(request, 'update_domain_name.html', {'form': form, 'domain_name': domain_name})

@login_required
def delete_domain_name(request, domain_id):
    domain_name = get_object_or_404(DomainName, id=domain_id)
    site_id = domain_name.site.id
    if request.method == 'POST':
        domain_name.delete()
        return redirect('site_detail', site_id=site_id)
    return render(request, 'delete_domain_name.html', {'domain_name': domain_name})

# Views for managing SEO settings
@login_required
def create_seo_settings(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    if request.method == 'POST':
        form = SEOSettingsForm(request.POST)
        if form.is_valid():
            seo_settings = form.save(commit=False)
            seo_settings.site = site
            seo_settings.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = SEOSettingsForm()
    return render(request, 'create_seo_settings.html', {'form': form, 'site': site})

@login_required
def update_seo_settings(request, seo_id):
    seo_settings = get_object_or_404(SEOSettings, id=seo_id)
    if request.method == 'POST':
        form = SEOSettingsForm(request.POST, instance=seo_settings)
        if form.is_valid():
            form.save()
            return redirect('site_detail', site_id=seo_settings.site.id)
    else:
        form = SEOSettingsForm(instance=seo_settings)
    return render(request, 'update_seo_settings.html', {'form': form, 'seo_settings': seo_settings})

@login_required
def delete_seo_settings(request, seo_id):
    seo_settings = get_object_or_404(SEOSettings, id=seo_id)
    site_id = seo_settings.site.id
    if request.method == 'POST':
        seo_settings.delete()
        return redirect('site_detail', site_id=site_id)
    return render(request, 'delete_seo_settings.html', {'seo_settings': seo_settings})

