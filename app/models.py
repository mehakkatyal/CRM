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
    date=models.DateField()
    account_balances = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Allow NULL and blank


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
class TransactionAmount(models.Model):
    details = models.ForeignKey(details, related_name="transaction_amounts", on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return f"Transaction Amount for {self.details.user.username}"
class DisputedAmount(models.Model):
    details = models.ForeignKey(details, related_name="disputed_amounts", on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return f"Disputed Amount for {self.details.user.username}"
class Freeze(models.Model):
    details = models.ForeignKey(details, related_name="freezes", on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Freeze status for {self.details.user.username}"
class Layer(models.Model):
    details = models.ForeignKey(details, related_name="layers", on_delete=models.CASCADE)
    layer = models.CharField(max_length=100)

    def __str__(self):
        return f"Layer for {self.details.user.username}"
class InwardDate(models.Model):
    details = models.ForeignKey(details, related_name="inward_dates", on_delete=models.CASCADE)
    inward_date = models.DateField()

    def __str__(self):
        return f"Inward Date for {self.details.user.username}"
class Update(models.Model):
    details = models.ForeignKey(details, related_name="updates", on_delete=models.CASCADE)
    update_text = models.CharField(max_length=200)

    def __str__(self):
        return f"Update for {self.details.user.username}"




