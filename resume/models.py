from django.db import models
from solo.models import SingletonModel as singleton
from colorfield.fields import ColorField
import re, calendar

class About(singleton):
    site_url = models.URLField(blank=False, default='')
    site_title = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True)
    background_color = ColorField(default='#868E96')
    background_secondary_color = ColorField(default='#343a40')
    primary_color = ColorField(default='#138d69')
    secondary_color = ColorField(default='#d6d9dc')
    text_color = ColorField(default='#96999b')
    def full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}' if self.middle_name else f"{self.first_name} {self.last_name}"
    def site_display_name(self):
        return re.sub('http://', '', self.site_url)
    class Meta:
        pass

class SocialIcon(models.Model):
    def __str__(self):
        return self.fa_icon[3:].capitalize()
    link = models.URLField(blank=True, default='')
    fa_icon = models.CharField(max_length=50)
    class Meta:
        pass
    
class Experience(models.Model):
    def __str__(self):
        return self.title + ' - ' + self.company
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    current_job = models.BooleanField(default='False')
    description = models.TextField()
    class Meta:
        verbose_name_plural = 'experience'
    def start_month(self):
        return f'{calendar.month_name[self.start_date.month]} {self.start_date.year}'
    def end_month(self):
        return 'Present' if self.current_job else f'{calendar.month_name[self.end_date.month]} {self.end_date.year}'
    
class Education(models.Model):
    def __str__(self):
        return self.school
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    current_student = models.BooleanField()
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=3.5)
    description = models.TextField()
    class Meta:
        verbose_name_plural = 'education'
    def start_month(self):
        return f'{calendar.month_name[self.start_date.month]} {self.start_date.year}'
    def end_month(self):
        return 'Present' if self.current_student else f'{calendar.month_name[self.end_date.month]} {self.end_date.year}'
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'skill categories'
        
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Skill(models.Model):
    def __str__(self):
        return self.name
    @property
    def is_check(self):
        return self.fa_icon == 'fa_check';
    @property
    def is_icon(self):
        return not is_check(self) and not is_text(self);
    @property
    def is_text(self):
        return self.fa_icon == '';
    type = models.IntegerField(choices=[(1, "icon"), (2, "text"), (3, "check")], default=2);
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fa_icon = models.CharField(max_length=50, blank=True)
    class Meta:
        ordering = ['category', 'type']

class Interests(singleton):
    description = models.TextField(blank=True)
    show_section = models.BooleanField(default=False)

class Award(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    def month(self):
        return f'{calendar.month_name[self.date.month]} {self.date.year}'

