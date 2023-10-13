from django.db import models


class ColorPalette(models.Model):
    name = models.CharField(max_length=255)
    colors = models.TextField()  # Store colors as a comma-separated string
    creation_date = models.DateField()

class Font(models.Model):
    name = models.CharField(max_length=255)
    font_file = models.FileField(upload_to='fonts/')
    creation_date = models.DateField()

