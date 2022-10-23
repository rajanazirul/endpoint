from django.db import models

# Create your models here.
class Record(models.Model):
    user_id = models.CharField(max_length=200)
    input_one = models.DecimalField(max_digits=15, decimal_places=2)
    result = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def calculate_result(self):
        return "%.2f" %(float(self.input_one) * 0.8)

    def save(self, *args, **kwargs):
        self.result = self.calculate_result
        super(Record, self).save(*args, **kwargs)