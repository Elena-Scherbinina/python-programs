from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    STATUS_CHOICES = [
        (0, 'to-do'),
        (1, 'in-progress'),
        (2, 'done'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cards'
    )

    def __str__(self):
        return '{}: {} ({}) - {} ({}) by {}'.format(
            self.id,
            self.title,
            self.description,
            self.status,
            self.get_status_display(),
            self.owner.username
        )

class Task(models.Model):
    description = models.CharField(max_length=255)  # Required string field
    done = models.BooleanField(default=False)  # Boolean field with default value
    card = models.ForeignKey(Card, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} for {}'.format(
            self.description,
            self.done,
            self.card
        )



