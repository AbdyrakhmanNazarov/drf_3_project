from django.db import models

class ProductManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)