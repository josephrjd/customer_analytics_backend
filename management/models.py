from django.db import models

# Create your models here.

class OrgCategories(models.Model):
    class Meta:
        db_table = 'tb_org_categories'
        managed = True
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

    id = models.AutoField('CategoryId', primary_key=True)
    category = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=100, blank=False)

class OrgSubCategories(models.Model):
    class Meta:
        db_table = 'tb_org_sub_categories'
        managed = True
        verbose_name = 'Sub categories'
        verbose_name_plural = 'Sub categories'

    id = models.AutoField('SubCategoryId', primary_key=True)
    sub_category = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(OrgCategories, on_delete=models.CASCADE)
    description = models.TextField(max_length=100, blank=False)

class OrgZone(models.Model):
    class Meta:
        db_table = 'tb_org_zone'
        managed = True
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'

    id = models.AutoField('ZoneId', primary_key=True)
    zone = models.CharField(max_length=50, blank=False)
    sub_category = models.ForeignKey(OrgSubCategories, on_delete=models.CASCADE)
    device_id = models.CharField(verbose_name='Device id', max_length=50, blank=False)
    description = models.TextField(max_length=100, blank=False)