from django.db import models
from django.utils import timezone
# Create your models here.

class Objects(models.Model):
	comName = models.CharField(max_length=36,blank=True,null=True)
	category = models.CharField(max_length=20,blank=True,null=True)
	partNum = models.CharField(max_length=20,blank=True,null=True)
	supplier = models.CharField(max_length=20,blank=True,null=True)
	uom = models.CharField(max_length=20,blank=True,null=True)
	image = models.ImageField(upload_to='tec-spec', blank=True)
	drawing = models.CharField(max_length=20,blank=True,null=True)
	weight = models.CharField(max_length=20,blank=True,null=True)
	dtCreate = models.DateTimeField(default=timezone.now)

	def __str__(self):
	  return self.category

	class Meta:
	  db_table ='objects'