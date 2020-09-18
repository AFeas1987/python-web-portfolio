from django.shortcuts import render
from projects.models import Project
from resume.models import About, SocialIcon, Experience, Education, Skill, Interests, Award

def portfolio(request):
    projects = Project.objects.all()
    about = About.get_solo()
    social_icons = SocialIcon.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    interests = Interests.get_solo()
    awards = Award.objects.all()
    context = {
                "projects" : projects
                ,"about" : about
                ,"social_icons" : social_icons
                ,"experience" : experience
                ,"education" : education
                ,"skills" : skills
                ,"interests" : interests
                ,"awards" : awards
              }
    return render(request, "portfolio.html", context)

