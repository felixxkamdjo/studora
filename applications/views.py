from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from projects.models import Project
from .models import Application
from .forms import ApplicationForm


@login_required
def apply(request, project_pk):
    if not request.user.is_student:
        messages.error(request, 'Seuls les étudiants peuvent postuler.')
        return redirect('project_list_student')

    project = get_object_or_404(Project, pk=project_pk, status='open')

    # Déjà postulé
    if Application.objects.filter(student=request.user, project=project).exists():
        messages.warning(request, 'Vous avez déjà postulé à ce projet.')
        return redirect('project_detail', pk=project_pk)

    # Projet complet
    if project.is_full:
        messages.error(request, 'Ce projet est complet.')
        return redirect('project_detail', pk=project_pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user
            application.project = project
            application.save()
            messages.success(request, 'Votre candidature a été envoyée avec succès.')
            return redirect('my_applications')
        else:
            messages.error(request, 'Veuillez corriger les erreurs.')
    else:
        form = ApplicationForm()

    context = {
        'form': form,
        'project': project,
    }
    return render(request, 'applications/apply.html', context)


@login_required
def my_applications(request):
    if not request.user.is_student:
        messages.error(request, 'Accès réservé aux étudiants.')
        return redirect('project_list_teacher')

    applications = Application.objects.filter(
        student=request.user
    ).select_related('project', 'project__teacher')

    context = {'applications': applications}
    return render(request, 'applications/my_applications.html', context)


@login_required
def review_application(request, pk):
    if not request.user.is_teacher:
        messages.error(request, 'Accès réservé aux enseignants.')
        return redirect('project_list_student')

    application = get_object_or_404(
        Application,
        pk=pk,
        project__teacher=request.user,
    )

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'accept':
            if application.project.is_full:
                messages.error(request, 'Le projet est complet, impossible d\'accepter.')
                return redirect('project_detail', pk=application.project.pk)
            application.status = 'accepted'
            application.save()
            messages.success(
                request,
                f'Candidature de {application.student.get_full_name()} acceptée.'
            )

        elif action == 'reject':
            application.status = 'rejected'
            application.save()
            messages.warning(
                request,
                f'Candidature de {application.student.get_full_name()} refusée.'
            )

        return redirect('project_detail', pk=application.project.pk)

    context = {'application': application}
    return render(request, 'applications/review.html', context)