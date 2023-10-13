from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ColorPalette, Font
from .forms import ColorPaletteForm, FontForm

@login_required
def create_palette(request):
    if request.method == 'POST':
        form = ColorPaletteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_palettes')
    else:
        form = ColorPaletteForm()
    return render(request, 'create_palette.html', {'form': form})

@login_required
def update_palette(request, palette_id):
    palette = get_object_or_404(ColorPalette, id=palette_id)
    if request.method == 'POST':
        form = ColorPaletteForm(request.POST, instance=palette)
        if form.is_valid():
            form.save()
            return redirect('manage_palettes')
    else:
        form = ColorPaletteForm(instance=palette)
    return render(request, 'update_palette.html', {'form': form, 'palette': palette})

@login_required
def delete_palette(request, palette_id):
    palette = get_object_or_404(ColorPalette, id=palette_id)
    if request.method == 'POST':
        palette.delete()
        return redirect('manage_palettes')
    return render(request, 'delete_palette.html', {'palette': palette})

# Views for managing fonts
@login_required
def create_font(request):
    if request.method == 'POST':
        form = FontForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_fonts')
    else:
        form = FontForm()
    return render(request, 'create_font.html', {'form': form})

@login_required
def update_font(request, font_id):
    font = get_object_or_404(Font, id=font_id)
    if request.method == 'POST':
        form = FontForm(request.POST, instance=font)
        if form.is_valid():
            form.save()
            return redirect('manage_fonts')
    else:
        form = FontForm(instance=font)
    return render(request, 'update_font.html', {'form': form, 'font': font})

@login_required
def delete_font(request, font_id):
    font = get_object_or_404(Font, id=font_id)
    if request.method == 'POST':
        font.delete()
        return redirect('manage_fonts')
    return render(request, 'delete_font.html', {'font': font})
