import datetime, calendar
from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "img")
    created = models.DateTimeField('created on', default=timezone.now, blank=True)
    github_link = models.URLField(blank=True, default='')
    codepen_link = models.URLField(blank=True, default='')
    def __str__(self):
        return self.title
    def display_created(self):
        return f'{calendar.month_name[self.created.month]} {self.created.year}'
    def was_published_recently(self):
        return True
        # now = timezone.now()
        # return now - datetime.timedelta(days=1) <= self.created <= now
    was_published_recently.admin_order_field = 'created'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'
    display_created.short_description = 'Date created'