from django.db import models

# Create your models here.
class Run(models.Model):
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Run {self.id} starting at {self.start_time}"

class RunData(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    water_level = models.FloatField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data for Run {self.run.id} at {self.time_stamp}"
    
