import uuid
from django.db import models
from timeStapedModel import TimeStampedModel

class Teacher(TimeStampedModel):
    """
    Teacher model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.subject}"