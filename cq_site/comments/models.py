from django.db import models
from users.models import User
from threads.models import Thread


class Comment(models.Model):
    com_id = models.BigIntegerField(primary_key=True)
    com_text = models.CharField(max_length=1000)
    com_postdate = models.DateField()
    com_upvotes = models.IntegerField()
    com_downvotes = models.IntegerField()
    com_author = models.ForeignKey(User, default=1, db_column='com_author', on_delete=models.SET_DEFAULT)
    com_thrlocation = models.ForeignKey(Thread, default=1, db_column='com_thrlocation', on_delete=models.SET_DEFAULT)

    class Meta:
        db_table = "comment"
