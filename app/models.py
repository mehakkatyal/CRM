from django.db import models
from django.contrib.auth.models import User


class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    is_vendor=models.BooleanField(default=False)

    def __str__(self):
        return super().__str__()
    
class details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    client_details=models.CharField(max_length=200,null=True)
    # complaint_details=models.CharField(max_length=100)
    # ps_io_number=models.CharField(max_length=100)
    account_balances=models.IntegerField()
    transaction_amount=models.IntegerField()
    disputed_amount=models.CharField(max_length=100)
    frezz=models.CharField(max_length=100)
    layer=models.CharField(max_length=100)
    date=models.DateField()
    update=models.CharField(max_length=200)

    def __str__(self):
        return super().__str__()
        
class complaint(models.Model):
    detail=models.ForeignKey(details,on_delete=models.CASCADE,null=True)
    complaint_details=models.CharField(max_length=100)
    # ps_io_number = models.CharField(max_length=100)

    def __str__(self):
        return super().__str__()
class PSIONumber(models.Model):
    complaint = models.ForeignKey(complaint, on_delete=models.CASCADE, related_name='ps_io_numbers')
    ps_io_number = models.CharField(max_length=100)

    def __str__(self):
        return self.ps_io_number


