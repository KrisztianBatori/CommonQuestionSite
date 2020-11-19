from django.db import models
from categories.models import Category
from users.models import User
from django.db import models
from django.utils.timezone import now


class Thread(models.Model):
    thr_id = models.AutoField(primary_key=True)
    thr_title = models.CharField(max_length=100)
    thr_content = models.TextField()
    thr_keywords = str(models.JSONField())
    thr_postdate = models.DateField(default=now)
    thr_upvotes = models.IntegerField(default=0)
    thr_downvotes = models.IntegerField(default=0)
    thr_category = models.ForeignKey(Category, default=1, db_column='thr_category', on_delete=models.SET_DEFAULT)
    thr_author = models.ForeignKey(User, default=1, db_column='thr_author', on_delete=models.SET_DEFAULT)

    class Meta:
        db_table = "thread"
