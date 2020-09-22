import datetime, calendar
from django.db import models
from django.utils import timezone, safestring

class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	technology = models.CharField(max_length=50)
	image = models.URLField(blank=True, default='')
	created = models.DateTimeField('created on', default=timezone.now, blank=True)
	github_link = models.URLField(blank=True, default='')
	codepen_link = models.URLField(blank=True, default='')
	def __str__(self):
		return self.title
	def display_created(self):
		return f'{calendar.month_name[self.created.month]} {self.created.year}'
	display_created.short_description = 'Date created'
	class Meta:
		ordering = ['-created']