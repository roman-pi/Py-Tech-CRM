from django.db import models
import datetime
from opportunity.models import Opportunity

class my_data(models.Model):
    data=models.DateTimeField()
    suma=models.FloatField()
    category=models.TextField(max_length=20)

    def __str__(self):
        return "%s: %s %s" % (self.category, self.suma, self.data)