# from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Project

# from django.contrib.contenttypes.admin import TabularInline

# class ProjectImageInline(TabularInline):
    # model = Project
    # readonly_fields = ('image_preview',)

    # def image_preview(self, obj):
        # if obj.image:
            # return '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.image.url)
        # else:
            # return '(No image)'

    # image_preview.short_description = 'Preview'
    
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ['created']
    search_fields = ['title', 'description', 'technology']
    list_display = ('title', 'technology', 'display_created', 'was_published_recently')
    fieldsets = [
        ('Project information', {'fields': ['title', 'description', 'technology'], 'classes': ['extrapretty']}),
        ('Project GIF', {'fields': ['image', ]}),
        ('Project URLs', {'fields': ['github_link', 'codepen_link']}),
        ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
    ]
    # inlines = [ ProjectImageInline, ]


admin.site.register(Project, ProjectAdmin)
admin.site.site_url = "/"