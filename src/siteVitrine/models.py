from datetime import timezone
from django.db import models
from utilisateur.models import CustomUser

class Site(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=255)
    creation_date = models.DateField()
    site_url = models.URLField()
    description = models.TextField()
    site_status = models.CharField(max_length=10, choices=[('draft', 'Brouillon'), ('published', 'Publié')])
    publication_date = models.DateField(null=True, blank=True)

class Page(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    page_title = models.CharField(max_length=255)
    page_content = models.TextField()
    display_order = models.IntegerField()
    page_status = models.CharField(max_length=10, choices=[('draft', 'Brouillon'), ('published', 'Publié')])
    publication_date = models.DateField(null=True, blank=True)

    def publish(self):
        self.page_status = 'published'
        self.publication_date = timezone.now()
        self.save()


