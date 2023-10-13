from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Site, SiteTemplate, SiteSection
from .forms import SiteTemplateForm, SiteSectionForm

@login_required
def create_template(request):
    if request.method == 'POST':
        form = SiteTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_templates')
    else:
        form = SiteTemplateForm()
    return render(request, 'create_template.html', {'form': form})

@login_required
def update_template(request, template_id):
    template = get_object_or_404(SiteTemplate, id=template_id)
    if request.method == 'POST':
        form = SiteTemplateForm(request.POST, instance=template)
        if form.is_valid():
            form.save()
            return redirect('manage_templates')
    else:
        form = SiteTemplateForm(instance=template)
    return render(request, 'update_template.html', {'form': form, 'template': template})

@login_required
def delete_template(request, template_id):
    template = get_object_or_404(SiteTemplate, id=template_id)
    if request.method == 'POST':
        template.delete()
        return redirect('manage_templates')
    return render(request, 'delete_template.html', {'template': template})

# Views for managing site sections
@login_required
def create_section(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    if request.method == 'POST':
        form = SiteSectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.site = site
            section.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = SiteSectionForm()
    return render(request, 'create_section.html', {'form': form, 'site': site})

@login_required
def update_section(request, section_id):
    section = get_object_or_404(SiteSection, id=section_id)
    if request.method == 'POST':
        form = SiteSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('site_detail', site_id=section.site.id)
    else:
        form = SiteSectionForm(instance=section)
    return render(request, 'update_section.html', {'form': form, 'section': section})

@login_required
def delete_section(request, section_id):
    section = get_object_or_404(SiteSection, id=section_id)
    site_id = section.site.id
    if request.method == 'POST':
        section.delete()
        return redirect('site_detail', site_id=site_id)
    return render(request, 'delete_section.html', {'section': section})
