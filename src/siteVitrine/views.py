from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import  Site, Page
from .forms import  SiteForm, PageForm

@login_required
def create_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = SiteForm()
    return render(request, 'create_site.html', {'form': form})

@login_required
def update_site(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = SiteForm(instance=site)
    return render(request, 'update_site.html', {'form': form, 'site': site})

@login_required
def delete_site(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    if request.method == 'POST':
        site.delete()
        return redirect('manage_sites')
    return render(request, 'delete_site.html', {'site': site})

def view_site(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    return render(request, 'view_site.html', {'site': site})

def view_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'view_page.html', {'page': page})


@login_required
def create_page(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.site = site
            page.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = PageForm()
    return render(request, 'create_page.html', {'form': form, 'site': site})

@login_required
def update_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('site_detail', site_id=page.site.id)
    else:
        form = PageForm(instance=page)
    return render(request, 'update_page.html', {'form': form, 'page': page})

@login_required
def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    site_id = page.site.id
    if request.method == 'POST':
        page.delete()
        return redirect('site_detail', site_id=site_id)
    return render(request, 'delete_page.html', {'page': page})
