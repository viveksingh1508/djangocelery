from django.db import models

# Create your models here.


class Product(models.Model):
    asin = models.CharField(max_length=120, unique=True)
    title = models.CharField(max_length=220, blank=True, null=True)
    current_price = models.FloatField(blank=True, null=True, default=0.00)
    metadata = models.JSONField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductScanEventManager(models.Manager):
    def create_scrape_event(self, data, url=None):
        asin = data.get("asin") or None
        if not asin:
            return None
        product, _ = Product.objects.get_or_create(
            asin=asin,
            defaults={
                "title": data.get("title"),
                "current_price": data.get("price") or 0.00,
                "metadata": data,
            },
        )
        event = self.create(product=product, url=url, asin=asin, data=data)
        return event


class ProductScrapeEvent(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="scrape_events"
    )
    url = models.URLField(max_length=500, blank=True, null=True)
    data = models.JSONField(blank=True, null=True)
    asin = models.CharField(max_length=120, unique=True)
    # title = models.constraints(max_lenght=220, blank=True, null=True)
    # current_price = models.FloatField(blank=True, null=True, default=0.00)
    # metadata = models.JSONField(blank=True, null=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # metadata = models.JSONField(blank=True, null=True)

    objects = ProductScanEventManager()
