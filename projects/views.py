from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Project
from .forms import ProjectForm


@login_required
def project_list_student(request):
    query = request.GET.get('q', '')
    domain = request.GET.get('domain', '')

    projects = Project.objects.filter(status='open')

    if query:
        projects = projects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if domain:
        projects = projects.filter(domain=domain)

    paginator = Paginator(projects, 10)
    page = request.GET.get('page')
    projects = paginator.get_page(page)

    context = {
        'projects': projects,
        'query': query,
        'domain': domain,
        'domain_choices': Project.DOMAIN_CHOICES,
    }
    return render(request, 'projects/list_student.html', context)


@login_required
def project_list_teacher(request):
    if not request.user.is_teacher:
        messages.error(request, 'Accès réservé aux enseignants.')
        return redirect('project_list_student')

    projects = Project.objects.filter(teacher=request.user)

    context = {'projects': projects}
    return render(request, 'projects/list_teacher.html', context)


@login_required
def project_create(request):
    if not request.user.is_teacher:
        messages.error(request, 'Accès réservé aux enseignants.')
        return redirect('project_list_student')

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.teacher = request.user
            project.save()
            messages.success(request, 'Projet créé avec succès.')
            return redirect('project_list_teacher')
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    else:
        form = ProjectForm()

    context = {
        'form': form,
        'action': 'Créer',
    }
    return render(request, 'projects/form.html', context)


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    user_application = None
    if request.user.is_student:
        from applications.models import Application
        user_application = Application.objects.filter(
            student=request.user,
            project=project,
        ).first()

    context = {
        'project': project,
        'user_application': user_application,
    }
    return render(request, 'projects/detail.html', context)


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk, teacher=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projet modifié avec succès.')
            return redirect('project_detail', pk=project.pk)
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    else:
        form = ProjectForm(instance=project)

    context = {
        'form': form,
        'action': 'Modifier',
        'project': project,
    }
    return render(request, 'projects/form.html', context)


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, teacher=request.user)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Projet supprimé.')
        return redirect('project_list_teacher')

    context = {'project': project}
    return render(request, 'projects/confirm_delete.html', context)