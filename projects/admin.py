from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
	list_filter = ['created']
	search_fields = ['title', 'description', 'technology']
	list_display = ('title', 'technology', 'display_created')
	fieldsets = [
		('Project information', {'fields': ['title', 'description', 'technology'], 'classes': ['extrapretty']}),
		('Project GIF', {'fields': ['image', ]}),
		('Project URLs', {'fields': ['github_link', 'codepen_link']}),
		('Date information', {'fields': ['created'], 'classes': ['collapse']}),
	]

admin.site.register(Project, ProjectAdmin)
admin.site.site_url = "/"