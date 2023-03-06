from django.db import models
from accounts.models import RegionalDirector, MarketingManager, DistrictManager
# Create your models here.
import uuid


class Store(models.Model):
    store_name = models.CharField(max_length=155, null=True, blank=True)
    store_uuid = models.UUIDField(default=uuid.uuid4)
    area_code = models.CharField(max_length=155)
    district_manager = models.ForeignKey(DistrictManager, on_delete=models.SET_NULL, null=True, blank=True)
    marketing_manager = models.ForeignKey(MarketingManager, on_delete=models.SET_NULL, null=True, blank=True)
    regional_director = models.ForeignKey(RegionalDirector, on_delete=models.SET_NULL, null=True, blank=True)
    store_latitude = models.CharField(max_length=155)
    store_longitude = models.CharField(max_length=155)



    def __str__(self) -> str:
        return self.store_name