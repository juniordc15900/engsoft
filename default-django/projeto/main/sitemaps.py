from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    
    def items(self):
        return ['home','contact','about']

    def location(self,item):
        return reverse(item)
        