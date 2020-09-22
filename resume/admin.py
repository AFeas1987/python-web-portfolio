from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import About, SocialIcon, Experience, Education, SkillCategory, Skill, Interests, Award

class AboutAdmin(SingletonModelAdmin):
	# list_filter = ['created']
	# search_fields = ['title', 'description', 'technology']
	# list_display = ('title', 'technology', 'display_created', 'was_published_recently')
	fieldsets = [
		('Site', {'fields': ['site_url', 'site_title']}),
		('Appearance', {'fields': ['background_color', 'background_secondary_color', 'primary_color', 'secondary_color', 'text_color']}),
		('Name', {'fields': ['first_name', 'middle_name', 'last_name'], 'classes': ['extrapretty']}),
		('Contact info', {'fields': ['location', 'phone', 'email']}),
		('Description', {'fields': ['description']}),
	]

class SkillCategoryAdmin(admin.ModelAdmin):
	def get_model_perms(self, request): # hide from admin index
		return {}

class SkillAdmin(admin.ModelAdmin):
	search_fields = ['name', 'category', 'type']
	list_display = ("name", "category", "type")

class InterestsAdmin(SingletonModelAdmin):
	pass

admin.site.register(About, AboutAdmin)
admin.site.register(SocialIcon, admin.ModelAdmin)
admin.site.register(Experience, admin.ModelAdmin)
admin.site.register(Education, admin.ModelAdmin)
admin.site.register(SkillCategory, SkillCategoryAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Interests, InterestsAdmin)
admin.site.register(Award, admin.ModelAdmin)

admin.site.site_url = "/"