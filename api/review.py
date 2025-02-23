import uuid
from django.db import models
from timeStapedModel import TimeStampedModel
from teacher import Teacher
from user import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(TimeStampedModel):
    """
    Review model for teacher ratings
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ['teacher', 'user']  # Один пользователь - один отзыв на учителя

    def __str__(self):
        return f"Review by {self.user.username} for {self.teacher.name}"