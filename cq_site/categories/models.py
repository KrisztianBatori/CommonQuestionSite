from django.db import models


class Category(models.Model):
    cat_id = models.BigIntegerField(primary_key=True)
    cat_name = models.CharField(max_length=15)

    class Meta:
        db_table = "category"
