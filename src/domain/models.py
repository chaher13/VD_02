from datetime import timezone
from django.db import models
from siteVitrine.models import Site
class DomainName(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    domain_name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('available', 'Disponible'), ('reserved', 'Réservé'), ('active', 'Actif')])
    expiration_date = models.DateField()

    def is_available(self):
        return self.status == 'available'

class SEOSettings(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE)
    site_title = models.CharField(max_length=255)
    site_description = models.TextField()
    keywords = models.TextField()
    update_date = models.DateField()

    def update_seo_settings(self, title, description, keywords):
        self.site_title = title
        self.site_description = description
        self.keywords = keywords
        self.update_date = timezone.now()
        self.save()


