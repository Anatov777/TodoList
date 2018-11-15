from django.db import models

class Task(models.Model):
    textString = models.CharField(max_length=250)
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.textString + ' / ' + str(self.completed)
