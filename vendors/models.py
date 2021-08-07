from django.db import models

class Vendor(models.Model):
    company_name = models.CharField(max_length = 100)
    company_number = models.CharField(max_length = 15)
    rep_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.company_name
