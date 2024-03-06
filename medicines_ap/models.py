from django.db import models
from django.utils import timezone
import uuid
class Baseclass(models.Model):
    id=models.UUIDField(default=uuid.uuid4,editable=True,unique=True,primary_key=True)
    # id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    class Meta:
        abstract=True
       

# Create your models here.
class Medicine(Baseclass):
 
    
    med_price=models.IntegerField(default=100)
    name=models.CharField(max_length=50,default="r")
    batch_no=models.IntegerField(default=10)
    expiry_date=models.DateField(default=" ") 
    manufac_date = models.DateField(default=" ")
    shelf_number=models.CharField(max_length=255,default=2)
    description=models.CharField(max_length=50,default="none")
    in_stock_med=models.BooleanField(default=False)
    Medicine_type=models.CharField(max_length=50,default="none")
    Medicine_quantity=models.IntegerField(default=10)
    medicine_location=models.CharField(max_length=255,default="hospital")
    medicine_gst=models.FloatField(default=1.5)
    
    


class Customer_data(Baseclass):
    # cust_id=models.UUIDField(default=uuid.uuid4,editable=True,unique=True,primary_key=True)
    cust_name=models.CharField(default="none",max_length=200)
    cust_age=models.IntegerField(default=20)
    cust_problem=models.CharField(default=" ",max_length=255)
    cust_dateofvisit=models.DateTimeField(default=" ")
    cust_address=models.CharField(default=" ",max_length=255)
    medicine_quant=models.CharField(default=" ",max_length=255)
    cust_phn=models.IntegerField(default=1)
    cust_gender=models.CharField(default=None,max_length=255)
    cust_dob=models.DateField(default=" ")
    cust_email=models.EmailField(default=" ")
    class Meta:
        db_table="customer_data_table"
    


