from django.db import models

# Create your models here.
class KeyTable(models.Model):
    rootNote = models.CharField(max_length=2)
    scale = models.CharField(max_length=5)
    note2 = models.CharField(max_length=2)
    note3 = models.CharField(max_length=2)
    note4 = models.CharField(max_length=2)
    note5 = models.CharField(max_length=2)
    note6 = models.CharField(max_length=2)
    note7 = models.CharField(max_length=2)

    def __str__(self):
        return f"Key: {self.rootNote} {self.scale} Notes: {self.rootNote} {self.note2} {self.note3} {self.note4} {self.note5} {self.note6} {self.note7}"