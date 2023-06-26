from django.db import models

# Create your models here.


class Tenat(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(verbose_name='机构名称', max_length=20)
    qrcode = models.CharField(verbose_name='二维码', max_length=50, null=True, blank=True)
    paycode = models.CharField(verbose_name='二维码', max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'tenat'