from django.shortcuts import render
from projects.models import Project
from bootstrap_modal_forms.generic import BSModalReadView

def project_index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)

class ProjectReadView(BSModalReadView):
    model = Project
    template_name = 'project_detail.html'