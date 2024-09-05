from django.db import models

class Product_details(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_count = models.IntegerField()
    category = models.CharField(max_length=255)
    popularity_score = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def update_popularity(self, sales_count):
        self.popularity_score = sales_count / (self.inventory_count)
        self.save()

    def UpdateInventory(self, sales_count):
        self.inventory_count = self.inventory_count- sales_count
        self.save()


