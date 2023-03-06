from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.



class AbstractUserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=155)
    role = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=155)
    user_uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        abstract = True



class RegionalDirector(AbstractUserProfile):
    area_code = models.CharField(max_length=155)
    
class MarketingManager(AbstractUserProfile):
    area_code = models.CharField(max_length=155)

class DistrictManager(AbstractUserProfile):
    area_code = models.CharField(max_length=155)
    marketing_manager = models.ForeignKey(MarketingManager, on_delete=models.SET_NULL, null=True, blank=True)

