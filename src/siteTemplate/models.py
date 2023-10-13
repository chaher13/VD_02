from django.db import models
from siteVitrine.models import Site

class SiteTemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    template_file = models.FileField(upload_to='templates/')
    author = models.CharField(max_length=255)
    creation_date = models.DateField()

class SiteSection(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    section_name = models.CharField(max_length=255)
    section_content = models.TextField()
    display_order = models.IntegerField()

    def add_to_site(self, site):
        self.site = site
        self.save()
