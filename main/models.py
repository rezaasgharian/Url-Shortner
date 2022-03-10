from random import choice
from string import ascii_letters, digits
from datetime import datetime

from django.db import models


class ShortURL(models.Model):
    url = models.URLField(max_length=200)
    short_id = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    times_accessed = models.IntegerField(default=0)
    accessed_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True,
                             null=True)

    def save(self, *args, **kwargs):
        self.short_id = self.short_id or self.get_short_id()
        self.created_at = datetime.now()
        super().save(*args, **kwargs)

    def get_short_id(self):
        while True:
            short_id = ''.join(choice(ascii_letters+digits) for _ in range(7))
            try:
                ShortURL.objects.get(short_id=short_id)
            except ShortURL.DoesNotExist:
                return short_id
