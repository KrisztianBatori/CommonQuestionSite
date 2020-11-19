from django.db import models
from django.utils.timezone import now


class User(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_name = models.CharField(max_length=18)
    usr_registrationdate = models.DateTimeField(default=now)
    usr_totalupvotes = models.IntegerField(default=0)
    usr_totaldownvotes = models.IntegerField(default=0)

    class Meta:
        db_table = "usr"
